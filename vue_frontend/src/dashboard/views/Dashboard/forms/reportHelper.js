export class RowItem {
  backend_id;
  name;
  placeholder;
  value;
  validators = [];

  constructor(backend_id, name, placeholder = null, value = null) {
    this.backend_id = backend_id;
    this.name = name;
    this.placeholder = placeholder;
    this.value = value;
  }

  clearData() {
    this.value = null;
  }

  validator() {
    const errors = this.validators
      .map(validator => validator(this))
      .filter(error => error);

    const errorsObject = {};
    errorsObject[this.name] = errors;
    
    return errors.length === 0
      ? null
      : errorsObject;
  }
}

export class JsonRowItem extends RowItem {
  getJsonName() {
    return this.name;
  }
  getJsonValue() {
    return this.value;
  }
  setJsonValue(value) {
    this.value = value;
  }
}

export class RowComponent extends JsonRowItem {
  get data() {
    return {
      name: this.name,
      backend_id: this.backend_id,
      placeholder: this.placeholder
    };
  }
}

export class SelectComponent extends RowComponent {
  statusOptions;

  constructor(backend_id, name, placeholder, value, statusOptions) {
    super(backend_id, name, placeholder, value);
    this.statusOptions = statusOptions;
  }

  get data() {
    return {
      name: this.name,
      statusOptions: this.statusOptions,
      placeholder: this.placeholder
    };
  }
}

export function listToSelectOptions(data) {
  return data.map(element => {
    return {
      option: element
    };
  });
}

export function selectDefaultOptions() {
  return listToSelectOptions([defaultSelectYes, defaultSelectNo, defaultSelectNull]);
}

export const defaultSelectYes = 'Positive';
export const defaultSelectNo = 'Negative';
export const defaultSelectNull = "---";

export class TotalComponent extends RowComponent {
  items;

  constructor(backend_id, name, placeholder, value, items) {
    super(backend_id, name, placeholder, value);
    this.items = items;
  }

  getJsonValue() {
    let total = 0;
    for (const key of this.items) {
      total += +key.value || 0;
    }
    return total;
  }
}

export function isRowItem(item) {
  return item instanceof RowItem;
}

export function hasJsonNameAndValue(item) {
  return item instanceof JsonRowItem;
}
