from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class IncidenceNolag(str, Enum):
    incidencerate1 = 'incidencerate1'
    incidencerate2 = 'incidencerate2'
    null = ""


class Occ2(str, Enum):
    Employee = 'Employee'
    Officer = 'Officer'
    Student = 'Student'
    Other = 'Other'
    null = ""


class Age(str, Enum):
    a15_20 = 'a15_20'
    a21_55 = 'a21_55'
    a56_80 = 'a56_80'
    null = ""


class UD2(str, Enum):
    Yes = 'Yes'
    No = 'No'
    null = ""


class Feverdays(str, Enum):
    d1_3 = 'd1_3'
    d3_5 = 'd3_5'
    d5_14 = 'd5_14'
    null = ""


class NS1(str, Enum):
    Positive = 'Positive'
    Negative = 'Negative'
    null = ""


class WbcD0(str, Enum):
    r0_35 = 'r0_35'
    r35_45 = 'r35_45'
    r45_73 = 'r45_73'
    r73_260 = 'r73_260'
    null = ""


class Plt(str, Enum):
    r0_106 = 'r0_106'
    r106_178 = 'r106_178'
    r178_590 = 'r178_590'
    null = ""


class LympD0(str, Enum):
    r0_17 = 'r0_17'
    r17_61 = 'r17_61'
    null = ""


class HctD0(str, Enum):
    r0_328 = 'r0_328'
    r328_560 = 'r328_560'
    null = ""


class AtyplD0(str, Enum):
    r0_1 = 'r0_1'
    r1_5 = 'r1_5'
    r5_45 = 'r5_45'
    null = ""


class ASTALT(str, Enum):
    r1_13 = 'r1_13'
    r13_45 = 'r13_45'
    null = ""


class Tourniquettest(str, Enum):
    s1 = 's1'
    s0 = 's0'
    null = ""


class Nausea(str, Enum):
    Yes = 'Yes'
    No = 'No'
    null = ""


class Bleeding(str, Enum):
    Yes = 'Yes'
    No = 'No'
    null = ""


class Petechiae(str, Enum):
    s1 = 's1'
    s0 = 's0'
    null = ""


class Myalgia(str, Enum):
    Yes = 'Yes'
    No = 'No'
    null = ""


class Model(BaseModel):
    incidence_nolag: Optional[IncidenceNolag] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples=['incidencerate1'],
        title='The incidence_nolag schema',
    )
    occ2: Optional[Occ2] = Field(
        "", description='Occupation', examples=['Employee'], title='The occ2 schema'
    )
    age: Optional[Age] = Field(
        "", description='age', examples=['a15_20'], title='The age schema'
    )
    UD2: Optional[UD2] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='Yes',
        title='The UD2 schema',
    )
    feverdays: Optional[Feverdays] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='d1_3',
        title='The feverdays schema',
    )
    NS1: Optional[NS1] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='Positive',
        title='The NS1 schema',
    )
    wbc_d0: Optional[WbcD0] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='r0_35',
        title='The wbc_d0 schema',
    )
    plt: Optional[Plt] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='r0_106',
        title='The plt schema',
    )
    lymp_d0: Optional[LympD0] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='',
        title='The lymp_d0 schema',
    )
    hct_d0: Optional[HctD0] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='r0_328',
        title='The hct_d0 schema',
    )
    atypl_d0: Optional[AtyplD0] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='',
        title='The atypl_d0 schema',
    )
    AST_ALT: Optional[ASTALT] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='r1_13',
        title='The AST_ALT schema',
    )
    tourniquettest: Optional[Tourniquettest] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='s1',
        title='The tourniquettest schema',
    )
    nausea: Optional[Nausea] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='Yes',
        title='The nausea schema',
    )
    bleeding: Optional[Bleeding] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='Yes',
        title='The bleeding schema',
    )
    petechiae: Optional[Petechiae] = Field(
        '',
        description='An explanation about the purpose of this instance.',
        examples='s0',
        title='The petechiae schema',
    )
    myalgia: Optional[Myalgia] = Field(
        "",
        description='An explanation about the purpose of this instance.',
        examples='Yes',
        title='The myalgia schema',
    )
