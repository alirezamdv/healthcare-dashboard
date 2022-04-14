import {
  RowComponent,
  SelectComponent,
  listToSelectOptions,
  selectDefaultOptions,
  defaultSelectYes as defaultSelectTrue,
  defaultSelectNo as defaultSelectFalse,
  defaultSelectNull,
  JsonRowItem
} from "./reportHelper";

export class SmileEngineSelectComponent extends SelectComponent {
  toSMILEEngine() {
    console.debug("to smile engine not implemented: SmileEngineSelectComponent");
    console.debug(this);
  }
}

export class SmileEngineJsonRowItem extends JsonRowItem {
  toSMILEEngine() {
    console.debug("to smile engine not implemented: SmileEngineJsonRowItem");
    console.debug(this);
  }
}

export class SmileEngineRowComponent extends RowComponent {
  toSMILEEngine() {
    console.debug("to smile engine not implemented: SmileEngineJsonRowItem");
    console.debug(this);
  }
}

export class DefaultSmileSelectComponent extends SmileEngineSelectComponent {
  constructor(backend_id, name, placeholder, value) {
    super(backend_id, name, placeholder, value, selectDefaultOptions());
  }

  toSMILEEngine() {
    switch (this.value) {
      case defaultSelectTrue:
        return 'Yes';
      case defaultSelectFalse:
        return 'No';
      case defaultSelectNull:
      case null:
        return null;
      default:
        console.debug(`Unknown value: ${this.value} in component ${this.name}!`);
        return null;
    }
  }
}

export const ast_altEnum = Object.freeze({ r1_13: "r1_13", r13_45: "r13_45" });
export class AST_ALT extends SmileEngineJsonRowItem {
  constructor(ast, alt) {
    super("ast_alt", "AST ALT", null, null);
    this.ast = ast;
    this.alt = alt;
  }

  getJsonValue() {
    console.debug("ast_alt getJsonValue");
    return this.ast.value + this.alt.value;
  }

  toSMILEEngine() {
    if (this.ast.value && this.alt.value && this.alt.value !== 0) {
      const ratio = this.ast.value / this.alt.value;
      if (!ratio || ratio < 0) {
        console.debug(`${this.name} out of range. Value: ${ratio}.`);
        return null;
      } else if (ratio <= 1.3) {
        return ast_altEnum.r1_13;
      } else if (ratio <= 4.5) {
        return ast_altEnum.r13_45;
      } else {
        console.debug(`${this.name} out of range. Value: ${ratio}.`);
        return null;
      }
    } else {
      console.debug(
        `${this.name} missing values. AST: ${this.ast.value}. ALT: ${this.ast.value}.`
      );
      return null;
    }
  }
}

// TODO how does this work in the BE?
export const bleedingCategoriesEnum = Object.freeze({
  gum_bleeding: "gum_bleeding",
  gastrointestinal_bleeding: "gastrointestinal_bleeding",
  epistaxis: "epistaxis",
  menstrual_bleeding: "menstrual_bleeding",
  other_mucosal_bleeding: "other_mucosal_bleeding",
  other_bleeding: "other_bleeding"
});
export class BleedingCategories extends SmileEngineJsonRowItem {
  constructor(
    gum_bleeding,
    gastrointestinal_bleeding,
    epistaxis,
    menstrual_bleeding,
    other_mucosal_bleeding,
    other_bleeding
  ) {
    super("bleeding_categories", "Bleeding Categories", null, null);
    this.gum_bleeding = gum_bleeding;
    this.gastrointestinal_bleeding = gastrointestinal_bleeding;
    this.epistaxis = epistaxis;
    this.menstrual_bleeding = menstrual_bleeding;
    this.other_mucosal_bleeding = other_mucosal_bleeding;
    this.other_bleeding = other_bleeding;
  }

  getJsonValue() {
    const result = [
      this.gum_bleeding.value ? this.gum_bleeding.backend_id : null,
      this.gastrointestinal_bleeding.value ? this.gastrointestinal_bleeding.backend_id : null,
      this.epistaxis.value ? this.epistaxis.backend_id : null,
      this.menstrual_bleeding.value ? this.menstrual_bleeding.backend_id : null,
      this.other_mucosal_bleeding.value ? this.other_mucosal_bleeding.backend_id : null,
      this.other_bleeding.value ? this.other_bleeding.backend_id : null,
    ].filter(value => value);
    if (result.length > 0) {
      return result;
    } else {
      return null;
    }
  }

  toSMILEEngine() {
    const result = [];
    if (this.gum_bleeding.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.gum_bleeding);
    } else if (this.gastrointestinal_bleeding.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.gastrointestinal_bleeding);
    } else if (this.epistaxis.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.gastroinepistaxistestinal_bleeding);
    } else if (this.menstrual_bleeding.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.menstrual_bleeding);
    } else if (this.other_mucosal_bleeding.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.other_mucosal_bleeding);
    } else if (this.other_bleeding.value === defaultSelectTrue) {
      result.push(bleedingCategoriesEnum.other_bleeding);
    }
    if (result.length > 0) {
      return result;
    } else {
      return null;
    }
  }
}

export const ageEnum = Object.freeze({
  a15_20: "a15_20",
  a21_55: "a21_55",
  a56_80: "a56_80"
});
export class Age extends SmileEngineRowComponent {
  constructor(value = null) {
    super("age", "Age", null, value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 15) {
      console.debug(`Age is out of range, too young, value: ${this.value}.`);
      return null;
    } else if (this.value <= 20) {
      return ageEnum.a15_20;
    } else if (this.value <= 55) {
      return ageEnum.a21_55;
    } else if (this.value <= 80) {
      return ageEnum.a56_80;
    } else {
      console.debug(`Age is out of range, too old, value: ${this.value}.`);
      return null;
    }
  }
}

export const occupationEnum = Object.freeze({
  Employee: "Employee",
  Officer: "Officer",
  Student: "Student",
  Other: "Other"
});
export class Occupation extends SmileEngineSelectComponent {
  constructor(value = null) {
    super(
      "occ2",
      "Occupation",
      null,
      value,
      listToSelectOptions([
        occupationEnum.Employee,
        occupationEnum.Officer,
        occupationEnum.Student,
        occupationEnum.Other
      ])
    );
  }

  toSMILEEngine() {
    switch (this.value) {
      case occupationEnum.Employee:
        return occupationEnum.Employee;
      case occupationEnum.Officer:
        return occupationEnum.Officer;
      case occupationEnum.Student:
        return occupationEnum.Student;
      case occupationEnum.Other:
        return occupationEnum.Other;
      case null:
        return null;
      default:
        console.debug(`Unknown value: ${this.value} in component ${this.name}!`);
        return null;
    }
  }
}

export class UnderlyingDesease extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("UD2", "Underlying Disease", null, value);
  }
}

// TODO we don't show this in dengue
export class Incidencerate extends SmileEngineRowComponent {
  constructor(value = null) {
    super("incidencerate", "Incidence Rate", null, value);
  }
}

export class Nausea extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("nausea", "Nausea", null, value);
  }
}

export class Petechiae extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("petechiae", "Petechiae", null, value);
  }

  toSMILEEngine() {
    switch (this.value) {
      case defaultSelectTrue:
        return "s1";
      case defaultSelectFalse:
        return "s0";
      case defaultSelectNull:
      case null:
        return null;
      default:
        console.debug(`Unknown value: ${this.value} in component ${this.name}!`);
        return null;
    }
  }
}

export class Myalgia extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("myalgia", "Myalgia", null, value);
  }
}

export class Bleeding extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("bleeding", "Bleeding", null, value);
  }
}

export class GumBleeding extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("gum_bleeding", "Gum bleeding", null, value);
  }
}

export class GastrointestinalBleeding extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("gastrointestinal_bleeding", "Gastrointestinal bleeding", null, value);
  }
}

export class Epistaxis extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("epistaxis", "Epistaxis", null, value);
  }
}

export class MenstrualBleeding extends DefaultSmileSelectComponent {
  constructor() {
    super("menstrual_bleeding", "Menstrual bleeding", null, null);
  }
}

export class OtherMucosalBleeding extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("other_mucosal_bleeding", "Other mucosal bleeding", null, value);
  }
}

export class OtherBleeding extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("other_bleeding", "Other bleeding", null, value);
  }
}

export class TourniquetTest extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("tourniquettest", "Tourniquet Test", null, value);
  }

  toSMILEEngine() {
    switch (this.value) {
      case defaultSelectTrue:
        return "s1";
      case defaultSelectFalse:
        return "s0";
      case defaultSelectNull:
      case null:
        return null;
      default:
        console.debug(
          `Unknown value: ${this.value} in component ${this.name}!`
        );
        return null;
    }
  }
}

export class NS1 extends DefaultSmileSelectComponent {
  constructor(value = null) {
    super("NS1", "NS1 Rapid Test", null, value);
  }

  toSMILEEngine() {
    switch (this.value) {
      case defaultSelectTrue:
        return "Positive";
      case defaultSelectFalse:
        return "Negative";
      case defaultSelectNull:
      case null:
        return null;
      default:
        console.debug(`Unknown value: ${this.value} in component ${this.name}!`);
        return null;
    }
  }
}

export class AST extends RowComponent {
  constructor(value = null) {
    super("ast", "AST", "IU/L", value);
  }
}

export class ALT extends RowComponent {
  constructor(value = null) {
    super("alt", "ALT", "IU/L", value);
  }
}

export const plateletsEnum = Object.freeze({
  r0_106: "r0_106",
  r106_178: "r106_178",
  r178_590: "r178_590"
});
export class Platelets extends SmileEngineRowComponent {
  constructor(value = null) {
    super("plt", "Platelets", "Cell/mm³", value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 0) {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    } else if (this.value <= 106) {
      return plateletsEnum.r0_106;
    } else if (this.value <= 178) {
      return plateletsEnum.r106_178;
    } else if (this.value <= 590) {
      return plateletsEnum.r178_590;
    } else {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    }
  }
}

export const hematocritEnum = Object.freeze({
  r0_328: "r0_328",
  r328_560: "r328_560"
});
export class Hematocrit extends SmileEngineRowComponent {
  constructor(value = null) {
    super("hct_d0", "Hematocrit", "%", value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 0) {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    } else if (this.value <= 32.8) {
      return hematocritEnum.r0_328;
    } else if (this.value <= 56) {
      return hematocritEnum.r328_560;
    } else {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    }
  }
}

export const whiteBloodCellsEnum = Object.freeze({
  r0_35: "r0_35",
  r35_45: "r35_45",
  r45_73: "r45_73",
  r73_260: "r73_260"
});
export class WhiteBloodCells extends SmileEngineRowComponent {
  constructor(value = null) {
    super("wbc_d0", "White blood cells", "10³/μL", value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 0) {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    } else if (this.value <= 3.5) {
      return whiteBloodCellsEnum.r0_35;
    } else if (this.value <= 4.5) {
      return whiteBloodCellsEnum.r35_45;
    } else if (this.value <= 7.3) {
      return whiteBloodCellsEnum.r45_73;
    } else if (this.value <= 26) {
      return whiteBloodCellsEnum.r73_260;
    } else {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    }
  }
}

export const lymphocytesEnum = Object.freeze({
  r0_17: "r0_17",
  r17_61: "r17_61"
});
export class Lymphocytes extends SmileEngineRowComponent {
  constructor(value = null) {
    super("lymp_d0", "Lymphocytes", "%", value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 0) {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    } else if (this.value <= 17) {
      return lymphocytesEnum.r0_17;
    } else if (this.value <= 61) {
      return lymphocytesEnum.r17_61;
    } else {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    }
  }
}

export const atypicalLymphocytesEnum = Object.freeze({
  r0_1: "r0_1",
  r1_5: "r1_5",
  r5_45: "r5_45"
});
export class AtypicalLymphocytes extends SmileEngineRowComponent {
  constructor(value = null) {
    super("atypl_d0", "Atypical Lymphocytes", "%", value);
  }

  toSMILEEngine() {
    if (!this.value || this.value < 0) {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    } else if (this.value <= 1) {
      return atypicalLymphocytesEnum.r0_1;
    } else if (this.value <= 5) {
      return atypicalLymphocytesEnum.r1_5;
    } else if (this.value <= 45) {
      return atypicalLymphocytesEnum.r5_45;
    } else {
      console.debug(`${this.name} out of range. Value: ${this.value}.`);
      return null;
    }
  }
}

export class RowItemFactory {
    static create(backend_id, value) {
      switch (backend_id) {
        case 'occ2':
          return new Occupation(value);
        case 'age':
          return new Age(value);
        case 'bleeding':
          return new Bleeding(value);
        case 'gum_bleeding':
          return new GumBleeding(value);
        case 'gastrointestinal_bleeding':
          return new GastrointestinalBleeding(value);
        case 'epistaxis':
          return new Epistaxis(value);
        case 'other_mucosal_bleeding':
          return new OtherMucosalBleeding(value);
        case 'other_bleeding':
          return new OtherBleeding(value);
        case 'incidence_nolag':
          return new Incidencerate(value);
        case 'UD2':
          return new UnderlyingDesease(value);
        case 'NS1':
          return new NS1(value);
        case 'wbc_d0':
          return new WhiteBloodCells(value);
        case 'plt':
          return new Platelets(value);
        case 'lymp_d0':
          return new Lymphocytes(value);
        case 'hct_d0':
          return new Hematocrit(value);
        case 'atypl_d0':
          return new AtypicalLymphocytes(value);
        case 'ast':
          return new AST(value);
        case 'alt':
          return new ALT(value);
        case 'tourniquettest':
          return new TourniquetTest(value);
        case 'nausea':
          return new Nausea(value);
        case 'petechiae':
          return new Petechiae(value);
        case 'myalgia':
          return new Myalgia(value);
        case 'AST_ALT':
          return {
            ...new AST_ALT(),
            value: value,
          };
        case 'feverdays':
          return null; // TODO?!
        default:
          throw Error('Cannot find backend_id: ' + backend_id);
      }
    }
}
