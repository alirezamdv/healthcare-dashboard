from enum import IntEnum
from typing import Any, Dict, List, Text, Union
import json
import numpy
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.types import ConstrainedFloat, ConstrainedInt, PositiveFloat, PositiveInt


class NonNegativeInt(ConstrainedInt):
    ge = 0


class NonNegativeFloat(ConstrainedFloat):
    ge = 0.0


class AgeInt(NonNegativeInt):
    pass


class DayOffsetInt(ConstrainedInt):
    ge = -1  # TODO: Does -1 has a meaning
    lt = 10


class Gender(IntEnum):
    male = 1
    female = 2


class Boolean(IntEnum):
    no = 1
    yes = 2


class BooleanWithUnknown(IntEnum):
    no = 1
    yes = 2
    unknown = 3


class ExtendedBooleanWithUnknown(IntEnum):
    no = 1
    yes = 2
    unknown = 3
    not_done = 4
    not_available = 5


class HumanHeightInCentimeters(ConstrainedInt):
    gt = 0
    lt = 300


class TourniquetTestQuantity(IntEnum):
    not_provided = 0
    less_than_10 = 1
    from_10_to_20 = 2
    greater_than_20 = 3

class TourniquetTestQuality(IntEnum):
    not_provided = 0
    fine = 1
    medium = 2
    coarse = 3
    mixed = 4
    unknown = 5


class HumanTemperatureFloat(ConstrainedFloat):
    gt = 13.0
    lt = 47.0


class HumanSystolicBloodPressure(ConstrainedInt):
    lt = 200


class HumanDiastolicBloodPressure(ConstrainedInt):
    lt = 150


class HumanPulse(ConstrainedInt):
    lt = 220
    gt = 20


class Hematocrit(ConstrainedInt):
    ge = 0
    le = 100


class MentalStatus(IntEnum):
    alert = 1
    drowsy = 2
    lethargic = 3
    restless_or_agitated = 4
    stuporous = 5  # awakens only with vigorous stimulation
    comatose = 6


class D01Data(BaseModel):

    # d01 Fields
    sex: Gender = Field(
        alias="d01_sex",
        title="Gender / sex of the patient",
        examples=[Gender.male, Gender.female]
    )

    je: BooleanWithUnknown = Field(
        alias="d01_je",
        title="Has patient ever received JE vaccine?",  # TODO: JE?,
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    height: HumanHeightInCentimeters = Field(
        alias="d01_height",
        title="height of patient in cm",
        examples=[107, 131]
    )

    febrile: BooleanWithUnknown = Field(
        alias="d01_febrile",
        title="Any other febrile illness during the past 2 months?",  # TODO: JE?,
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    headache_day: DayOffsetInt = Field(
        alias="d01_headache_day",
        title="Headache for how many days?",
        examples=[2]
    )

    myalgia_day: DayOffsetInt = Field(
        alias="d01_myalgia_day",
        title="Myalgia for how many days?",
        examples=[-1, 3]
    )

    bone_day: DayOffsetInt = Field(
        alias="d01_bone_day",
        title="Bone pain for how many days?",
        examples=[-1]
    )

    retro_day: DayOffsetInt = Field(
        alias="d01_retro_day",
        title="Retro-orbital pain for how many days?",
        examples=[-1]
    )

    flushed_day: DayOffsetInt = Field(
        alias="d01_flushed_day",
        title="Flushed face for how many days?",
        examples=[2, 1]
    )

    rashwithout_day: DayOffsetInt = Field(
        alias="d01_rashwithout_day",
        title="Rash without itching for how many days?",
        examples=[-1]
    )

    rashwith_day: DayOffsetInt = Field(
        alias="d01_rashwith_day",
        title="Rash with itching for how many days?",
        examples=[-1]
    )

    anorexia_day: DayOffsetInt = Field(
        alias="d01_anorexia_day",
        title="Anorexia for how many days?",
        examples=[2, 3]
    )

    nausea_day: DayOffsetInt = Field(
        alias="d01_nausea_day",
        title="Nausea for how many days?",
        examples=[-1, 1]
    )

    vomiting_day: DayOffsetInt = Field(
        alias="d01_vomiting_day",
        title="Vomiting for how many days?",
        examples=[2, 3]
    )

    abdominal_day: DayOffsetInt = Field(
        alias="d01_abdominal_day",
        title="Abdominal pain for how many days?",
        examples=[-1, 1]
    )

    drowsiness_day: DayOffsetInt = Field(
        alias="d01_drowsiness_day",
        title="Drowsiness for how many days?",
        examples=[-1]
    )

    spont_day: DayOffsetInt = Field(
        alias="d01_spont_day",
        title="Spontaneous petechiae for how many days?",
        examples=[-1]
    )

    gum_day: DayOffsetInt = Field(
        alias="d01_gum_day",
        title="Gum bleeding for how many days?",
        examples=[-1]
    )

    nose_day: DayOffsetInt = Field(
        alias="d01_nose_day",
        title="Nose bleeding for how many days?",
        examples=[-1]
    )
    vomit_bleed_day: DayOffsetInt = Field(
        alias="d01_vomit_bleed_day",
        title="Vomiting blood for how many days?",
        examples=[-1]
    )

    stool_day: DayOffsetInt = Field(
        alias="d01_stool_day",
        title="Melena / Red stool for how many days?",
        examples=[-1]
    )

    exud_day: DayOffsetInt = Field(
        alias="d01_exud_day",
        title="Exudative rhinorrhea for how many days?",
        examples=[-1]
    )

    clear_day: DayOffsetInt = Field(
        alias="d01_clear_day",
        title="Clear rhinorrhea for how many days?",
        examples=[-1]
    )

    prod_day: DayOffsetInt = Field(
        alias="d01_prod_day",
        title="Productive cough for how many days?",
        examples=[-1]
    )

    non_prod_day: DayOffsetInt = Field(
        alias="d01_non_prod_day",
        title="Non-productive cough for how many days?",
        examples=[-1]
    )

    feeling_day: DayOffsetInt = Field(
        alias="d01_feeling_day",
        title="Feeling of sore throat for how many days?",
        examples=[-1]
    )

    diarrhea_day: DayOffsetInt = Field(
        alias="d01_diarrhea_day",
        title="Diarrhea for how many days?",
        examples=[-1]
    )

    # d01, d04
    bleeding: BooleanWithUnknown = Field(
        alias="d01_bleeding",
        title="Bleeding",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    quantity: TourniquetTestQuantity = Field(
        alias="d01_quantity",
        title="Quantity Data of Tourniquet test",
        examples=[
            TourniquetTestQuantity.less_than_10,
            TourniquetTestQuantity.from_10_to_20,
            TourniquetTestQuantity.greater_than_20
        ]
    )

    quality: TourniquetTestQuality = Field(
        alias="d01_quality",
        title="Quality Data of Tourniquet test",
        examples=[
            TourniquetTestQuality.fine,
            TourniquetTestQuality.medium,
            TourniquetTestQuality.coarse,
            TourniquetTestQuality.mixed,
            TourniquetTestQuality.unknown
        ]
    )

    uri: BooleanWithUnknown = Field(
        alias="d01_uri",
        title="Upper respiratory infection",
        examples=[1]
    )


class D03Data(BaseModel):

    # d03 Temperatures

    temp_min: HumanTemperatureFloat = Field(
        alias="d03_temp_min",
        title="Minimum daily body temperature in °C",
        examples=[36.3, 37.9]
    )

    temp_max: HumanTemperatureFloat = Field(
        alias="d03_temp_max",
        title="Maximum daily body temperature in °C",
        examples=[38.5, 39.6]
    )

    temp_avg: HumanTemperatureFloat = Field(
        alias="d03_temp_avg",
        title="Daily average body temperature in °C",
        examples=[37.4, 38.75]
    )

    temp_range: PositiveFloat = Field(
        alias="d03_temp_range",
        title="Temperature range (max - min) in K",
        examples=[2.2, 1.7]
    )

    # d03 Blood Pressure

    sbp: HumanSystolicBloodPressure = Field(
        alias="d03_sbp",
        title="Minimum daily blood Pressure (Systolic)",
        examples=[90, 100]
    )

    dbp: HumanDiastolicBloodPressure = Field(
        alias="d03_dbp",
        title="Minimum daily blood Pressure (Diastolic)",
        examples=[60]
    )

    # d03 Pulse

    pulse_pre_min: PositiveInt = Field(
        alias="d03_pulse_pre_min",
        title="Minimum daily pulse pressure",
        examples=[30]
    )

    pulse_rate_min: HumanPulse = Field(
        alias="d03_pulse_rate_min",
        title="Minimum daily pulse rate",
        examples=[100, 88]
    )

    pulse_rate_max: HumanPulse = Field(
        alias="d03_pulse_rate_max",
        title="Maximum daily pulse rate",
        examples=[110, 108]
    )

    pulse_rate_avg: HumanPulse = Field(
        alias="d03_pulse_rate_avg",
        title="Daily average pulse rate",
        examples=[105, 98]
    )

    pulse_rate_range: PositiveInt = Field(
        alias="d03_pulse_rate_range",
        title="Pulse Rate Range",
        examples=[10, 20]
    )

    # d03: Hematocrit (HCT)

    hct_min: Hematocrit = Field(
        alias="d03_hct_min",
        title="Minimum Hematocrit (HCT) (Ward, fingertip, peripheral)",
        examples=[34, 36]
    )

    hct_max: Hematocrit = Field(
        alias="d03_hct_max",
        title="Maximum Hematocrit (HCT) (Ward, fingertip, peripheral)",
        examples=[38, 40]
    )

    hct_avg: Hematocrit = Field(
        alias="d03_hct_avg",
        title="Daily average Hematocrit (HCT)",
        examples=[36, 38]
    )

    hct_range: PositiveInt = Field(
        alias="d03_hct_range",
        title="Hematocrit (HCT) range (max - min)",
        examples=[4]
    )

    # d03: Fluid differences

    intake_diff: int = Field(
        alias="d03_intake_diff",
        title="Daily Fluid difference (intake - output)",
        examples=[0]
    )

    max_fluid_diff: int = Field(  # TODO: ?
        alias="d03_max_fluid_diff",
        title="Maximum Fluid difference (intake - output)",
        examples=[0]
    )


class D04Data(BaseModel):

    # d01, d04
    bleeding: BooleanWithUnknown = Field(
        alias="d04_bleeding",
        title="Bleeding",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    quantity: TourniquetTestQuantity = Field(
        alias="d04_quantity",
        title="Quantity Data of Tourniquet test",
        examples=[
            TourniquetTestQuantity.less_than_10,
            TourniquetTestQuantity.from_10_to_20,
            TourniquetTestQuantity.greater_than_20
        ]
    )

    quality: TourniquetTestQuality = Field(
        alias="d04_quality",
        title="Quality Data of Tourniquet test",
        examples=[
            TourniquetTestQuality.fine,
            TourniquetTestQuality.medium,
            TourniquetTestQuality.coarse,
            TourniquetTestQuality.mixed,
            TourniquetTestQuality.unknown
        ]
    )

    uri: BooleanWithUnknown = Field(
        alias="d04_uri",
        title="Upper respiratory infection",
        examples=[1]
    )

    # d04: Mental Status

    mental: MentalStatus = Field(
        alias="d04_mental",
        title="Mental Status",
        examples=[
            MentalStatus.alert,
            MentalStatus.drowsy,
            MentalStatus.lethargic,
            MentalStatus.restless_or_agitated,
            MentalStatus.stuporous,
            MentalStatus.comatose
        ]
    )

    # d04: Booleans

    rash: BooleanWithUnknown = Field(
        alias="d04_rash",
        title="Rash",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    conflu: Boolean = Field(
        alias="d04_conflu",
        title="Confluent petechial",
        examples=[
            Boolean.no,
            Boolean.yes
        ]
    )

    maculo: Boolean = Field(
        alias="d04_maculo",
        title="Maculoapular",
        examples=[
            Boolean.no,
            Boolean.yes
        ]
    )

    itching: BooleanWithUnknown = Field(
        alias="d04_itching",
        title="Itching related to rash",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    bruising: BooleanWithUnknown = Field(
        alias="d04_bruising",
        title="Bruising with venipuncture",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )


    spont: BooleanWithUnknown = Field(
        alias="d04_spont",
        title="Spontaneous petechiae",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    ecchy: BooleanWithUnknown = Field(
        alias="d04_ecchy",
        title="Ecchymosis",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    gum: BooleanWithUnknown = Field(
        alias="d04_gum",
        title="Gum",  # TODO: Bleeding?
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    nose: BooleanWithUnknown = Field(
        alias="d04_nose",
        title="Nose",  # TODO: Bleeding?
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    vomiting: BooleanWithUnknown = Field(
        alias="d04_vomiting",
        title="Vomiting blood",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    stool: BooleanWithUnknown = Field(
        alias="d04_stool",
        title="Melena / red stool",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    diarrhea: BooleanWithUnknown = Field(
        alias="d04_diarrhea",
        title="Diarrhea",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    clear: BooleanWithUnknown = Field(
        alias="d04_clear",
        title="Clear Rhinorrhea",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    prod: BooleanWithUnknown = Field(
        alias="d04_prod",
        title="Productive cough",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    non_prod: BooleanWithUnknown = Field(
        alias="d04_non_prod",
        title="Non-productive cough",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    feeling: BooleanWithUnknown = Field(
        alias="d04_feeling",
        title="Feeling of sore throat",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    # d04: Extended Booleans with Unknown

    abdominal: ExtendedBooleanWithUnknown = Field(
        alias="d04_abdominal",
        title="Abdominal pain",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )

    ab_circum: PositiveFloat = Field(
        alias="d04_ab_circum",
        title="Abdominal Circumference (in cm)",
        examples=[59.251, 58.924]
    )

    dyspnea: ExtendedBooleanWithUnknown = Field(
        alias="d04_dyspnea",
        title="Dyspnea",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )
    juandice: ExtendedBooleanWithUnknown = Field(
        alias="d04_juandice",
        title="Juandice",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )

    liver: ExtendedBooleanWithUnknown = Field(
        alias="d04_liver",
        title="Liver tenderness",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )

    liver_size: NonNegativeFloat = Field(
        alias="d04_liver_size",
        title="Liver size (> RCM) / span (in cm)",
        examples=[0]
    )

    lymph: ExtendedBooleanWithUnknown = Field(
        alias="d04_lymph",
        title="Lymph node enlargement",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )

    cervical: PositiveFloat = Field(
        alias="d04_cervical",
        title="Cervical (max. diameter in cm)",
        examples=[1]
    )

    epitro: PositiveFloat = Field(
        alias="d04_epitro",
        title="Epitrochea (max. diameter in cm)",
        examples=[1]
    )

    inguinal: PositiveFloat = Field(
        alias="d04_inguinal",
        title="Inguinal (max. diameter in cm)",
        examples=[1]
    )

    injected: ExtendedBooleanWithUnknown = Field(
        alias="d04_injected",
        title="Injected conjunctivae",
        examples=[
            ExtendedBooleanWithUnknown.no,
            ExtendedBooleanWithUnknown.yes,
            ExtendedBooleanWithUnknown.unknown,
            ExtendedBooleanWithUnknown.not_done,
            ExtendedBooleanWithUnknown.not_available
        ]
    )

    limbus: BooleanWithUnknown = Field(
        alias="d04_limbus",
        title="Limbus",
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    bilbar: BooleanWithUnknown = Field(
        alias="d04_bilbar",
        title="Bulbar",  # TODO: Bilbar seems to be a typo
        examples=[
            BooleanWithUnknown.no,
            BooleanWithUnknown.yes,
            BooleanWithUnknown.unknown
        ]
    )

    weight: PositiveInt = Field(
        alias="d04_weight",
        title="Weight (in kg)",
        examples=[15, 42]
    )


class D05Data(BaseModel):

    # d05

    hct: Hematocrit = Field(
        alias="d05_hct",
        title="Hematocrit (in %)",
        examples=[36, 41]
    )

    wbc: PositiveFloat = Field(
        alias="d05_wbc",
        title="White blood cells (in 1,000 cells / mm^3)",
        examples=[4.2, 4.1]
    )

    pmn: PositiveFloat = Field(
        alias="d05_pmn",
        title="Polymorphonuclear Leukocytes",
        examples=[5.766, 5.659]
    )

    band: PositiveFloat = Field(
        alias="d05_band",
        title="Band cells",
        examples=[1.435, 3.020]
    )

    lymp: PositiveFloat = Field(
        alias="d05_lymp",
        title="Lymphocytes",
        examples=[4.431, 4.301]
    )

    atyp: PositiveFloat = Field(
        alias="d05_atyp",
        title="Atyp Lymphocytes",
        examples=[1.435, 1.411]
    )

    mono: PositiveFloat = Field(
        alias="d05_mono",
        title="Monocytes",
        examples=[2.128, 3.203]
    )

    baso: NonNegativeFloat = Field(
        alias="d05_baso",
        title="Basophil",
        examples=[0]
    )

    eosin: NonNegativeFloat = Field(
        alias="d05_eosin",
        title="Eosinophil",
        examples=[0]
    )

    platelet: PositiveFloat = Field(
        alias="d05_platelet",
        title="Platelet count (in 1,000 cells / mm^3)",
        examples=[166, 138]
    )

    lft_protein: PositiveFloat = Field(
        alias="d05_lft_protein",
        title="Protein (g / L)",
        examples=[7.7, 6.3]
    )

    lft_albumin: PositiveFloat = Field(
        alias="d05_lft_albumin",
        title="Albumin (g / L)",
        examples=[5, 3.6]
    )

    lft_ast: PositiveFloat = Field(
        alias="d05_lft_ast",
        title="AST (IU / L)",
        examples=[105, 180]
    )

    lft_alt: PositiveFloat = Field(
        alias="d05_lft_alt",
        title="ALT (IU / L)",
        examples=[17, 19]
    )

    # d05: Unknown fields

    alb_globn_ratio: PositiveFloat = Field(
        alias="d05_alb_globn_ratio",
        title="Alb Globn Ratio",  # TODO: ?
        examples=[0.649, 0.571]
    )

    sgot_sgpt_ratio: PositiveFloat = Field(
        alias="d05_sgot_sgpt_ratio",
        title="Sgot Sgpt Ratio",  # TODO: ?
        examples=[6.176, 9.474]
    )

    sgot_platelet_ratio: PositiveFloat = Field(
        alias="d05_sgot_platelet_ratio",
        title="Sgot Platelet Ratio",  # TODO: ?
        examples=[0.633, 1.304]
    )


class DengueHemorrhagicFeverModelData(BaseModel):

    # General Fields

    age: AgeInt = Field(
        title="Patient age in years",
        examples=[5, 9]
    )

    fever_day: DayOffsetInt = Field(
        title="Number of days from the fever day to admission day",
        examples=[2, 3]
    )

    d01: D01Data

    d03: D03Data

    d04: D04Data

    d05: D05Data

    def dict(
            self, *, include, exclude, by_alias: bool, skip_defaults: bool,
            exclude_unset: bool, exclude_defaults: bool, exclude_none: bool
    ) -> Dict:
        representation = super().dict(
            include=include, exclude=exclude, by_alias=by_alias,
            skip_defaults=skip_defaults, exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults, exclude_none=exclude_none
        )

        result = dict()

        for key, value in representation.items():
            if isinstance(value, dict):
                result = {**result, **value}
            else:
                result[key] = value

        return result

    @classmethod
    def from_flat_dict(cls, flat_dict: Dict[Text, Any]) -> "DengueHemorrhagicFeverModelData":
        nested_dict = {
            "d01": {},
            "d03": {},
            "d04": {},
            "d05": {}
        }

        for key, value in flat_dict.items():
            if key.startswith("d01_"):
                nested_dict["d01"][key] = value
            elif key.startswith("d03_"):
                nested_dict["d03"][key] = value
            elif key.startswith("d04_"):
                nested_dict["d04"][key] = value
            elif key.startswith("d05_"):
                nested_dict["d05"][key] = value
            else:
                nested_dict[key] = value

        return cls(**nested_dict)


    def to_data_sequence(self) -> List[Any]:
        return numpy.array(
            [
                self.d03.temp_max,
                self.d03.temp_min,
                self.d03.sbp,
                self.d03.dbp,
                self.d03.pulse_pre_min,
                self.d03.pulse_rate_max,
                self.d03.pulse_rate_min,
                self.d03.hct_max,
                self.d03.hct_min,
                self.d04.mental.value,
                self.d04.quantity.value,
                self.d04.quality.value,
                self.d04.rash.value,
                self.d04.conflu.value,
                self.d04.maculo.value,
                self.d04.itching.value,
                self.d04.bruising.value,
                self.d04.bleeding.value,
                self.d04.spont.value,
                self.d04.ecchy.value,
                self.d04.gum.value,
                self.d04.nose.value,
                self.d04.vomiting.value,
                self.d04.stool.value,
                self.d04.diarrhea.value,
                self.d04.uri.value,
                self.d04.clear.value,
                self.d04.non_prod.value,
                self.d04.prod.value,
                self.d04.feeling.value,
                self.d04.abdominal.value,
                self.d04.dyspnea.value,
                self.d04.juandice.value,
                self.d04.liver.value,
                self.d04.liver_size,
                self.d04.ab_circum,
                self.d04.lymph.value,
                self.d04.cervical,
                self.d04.epitro,
                self.d04.inguinal,
                self.d04.injected.value,
                self.d04.limbus.value,
                self.d04.bilbar.value,
                self.d04.weight,
                self.d05.hct,
                self.d05.wbc,
                self.d05.pmn,
                self.d05.band,
                self.d05.lymp,
                self.d05.atyp,
                self.d05.mono,
                self.d05.baso,
                self.d05.eosin,
                self.d05.platelet,
                self.d05.lft_protein,
                self.d05.lft_albumin,
                self.d05.lft_ast,
                self.d05.lft_alt,
                self.d01.sex.value,
                self.d01.je.value,
                self.d01.height,
                self.d01.febrile.value,
                self.d01.headache_day,
                self.d01.myalgia_day,
                self.d01.bone_day,
                self.d01.retro_day,
                self.d01.flushed_day,
                self.d01.rashwithout_day,
                self.d01.rashwith_day,
                self.d01.anorexia_day,
                self.d01.nausea_day,
                self.d01.vomiting_day,
                self.d01.abdominal_day,
                self.d01.drowsiness_day,
                self.d01.bleeding,
                self.d01.spont_day,
                self.d01.gum_day,
                self.d01.nose_day,
                self.d01.vomit_bleed_day,
                self.d01.stool_day,
                self.d01.quantity.value,
                self.d01.quality.value,
                self.d01.uri.value,
                self.d01.exud_day,
                self.d01.clear_day,
                self.d01.non_prod_day,
                self.d01.prod_day,
                self.d01.feeling_day,
                self.d01.diarrhea_day,
                self.age,
                self.d03.temp_avg,
                self.d03.temp_range,
                self.d03.pulse_rate_avg,
                self.d03.pulse_rate_range,
                self.d03.hct_avg,
                self.d03.hct_range,
                self.d03.intake_diff,
                self.fever_day,
                self.d05.alb_globn_ratio,
                self.d05.sgot_sgpt_ratio,
                self.d05.sgot_platelet_ratio,
                self.d03.max_fluid_diff
            ]
        ).reshape(1, -1)