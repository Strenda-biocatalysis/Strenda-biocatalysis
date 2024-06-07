## This is a generated file. Do not modify it manually!

from __future__ import annotations
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import List, Optional
from enum import Enum
from uuid import uuid4
from datetime import date, datetime


@dataclass_json
@dataclass
class KineticParameters:
    michaelis_constant: float
    michaelis_constant_unit: str
    maximum_reaction_rate: float
    maximum_reaction_rate_unit: str
    turnover_number: float
    turnover_number_unit: str
    catalytic_efficiency: float
    catalytic_efficiency_unit: str
    dissociation_constant: float
    dissociation_constant_unit: str
    inhibition_type: str
    inhibition_constant: float
    inhibition_constant_unit: str
    hill_coefficient: float
    enzyme_stability: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:KineticParameters/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:KineticParameters",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )


@dataclass_json
@dataclass
class YieldAndConversion:
    c_yield: float
    yield_unit: str
    space_time_yield: float
    space_time_yield_unit: str
    conversion: float
    conversion_unit: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:YieldAndConversion/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:YieldAndConversion",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )


@dataclass_json
@dataclass
class ActivityAndInitialReactionRate:
    specific_activity: float
    specific_activity_unit: str
    initial_reaction_rate: float
    initial_reaction_rate_unit: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:ActivityAndInitialReactionRate/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:ActivityAndInitialReactionRate",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )


@dataclass_json
@dataclass
class SelectivityAndSpecificity:
    stereoselectivity: str
    enantioselectivity: float
    enantiomeric_excess: float
    enantiomeric_excess_unit: str
    diastereomeric_excess: float
    diasteriomeric_excess_unit: str
    isomeric_content: float
    isomeric_content_unit: str
    chemoselectivity: str
    regioselectivity: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:SelectivityAndSpecificity/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:SelectivityAndSpecificity",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )


@dataclass_json
@dataclass
class ThermodynamicParameters:
    gibbs_free_energy_change: str
    enthalpy_change: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:ThermodynamicParameters/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:ThermodynamicParameters",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )
