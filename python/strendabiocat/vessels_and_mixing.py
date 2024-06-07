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
class Vial:
    vial_size: float
    vial_size_unit: str
    vial_material: str
    closure_type: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Vial/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Vial",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
@dataclass_json
@dataclass
class Plate:
    plate_type: str
    plate_material: str
    number_of_wells: str
    well_shape: str
    well_volume: str
    well_arrangement: str
    supplier: str
    lot_number: float
    sealing_method: str
    sealing_material: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Plate/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Plate",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
    
    
    
    
    
    
@dataclass_json
@dataclass
class StirredTankReactor:
    type: str
    material: str
    volume: float
    volume_unit: str
    geometry: str
    bottom_type: str
    gas_consumption: str
    gas_supply: str
    gas_supply_rate: float
    gas_supply_rate_unit: str
    temperature_control: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:StirredTankReactor/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:StirredTankReactor",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
@dataclass_json
@dataclass
class TubularFlowContinuousReactor:
    volume: float
    volume_unit: str
    geometry: str
    reactor_type: str
    material: str
    tubing: str
    localisation_of_the_catalyst: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:TubularFlowContinuousReactor/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:TubularFlowContinuousReactor",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
    
    
    
@dataclass_json
@dataclass
class Shaking:
    shaking_type: str
    deflection: float
    deflection_unit: str
    speed: float
    speed_unit: str
    position: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Shaking/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Shaking",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
    
    
@dataclass_json
@dataclass
class MechanicallyImpelledMixing:
    stirring_type: str
    stirrer_material: str
    supplier: str
    number_of_stirrers: float
    distance_between_stirrers: float
    distance_between_stirrers_unit: str
    stirrer_blade_pitch_angle: float
    number_of_stirrer_blades: float
    stirrer_blade_size: float
    stirrer_blade_size_unit: str
    stirrer_geometry: str
    stirrer_speed: float
    speed_unit: str
    height_of_stirrer_above_vessel_base: float
    height_of_stirrer_above_vessel_base_unit: str
    power_per_volume: float
    power_per_volume_unit: str
    stir_bar_size: float
    stir_bar_size_unit: float
    stir_bar_shape: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:MechanicallyImpelledMixing/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:MechanicallyImpelledMixing",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
@dataclass_json
@dataclass
class LiquidOrGasImpelledMixing:
    volume_of_liquid_solid_phase: str
    residence_time: float
    residence_time_unit: str
    reynolds_number: str
    passive_mixing: str
    active_T_or_Y_mixer: str
    pulsing: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:LiquidOrGasImpelledMixing/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:LiquidOrGasImpelledMixing",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )