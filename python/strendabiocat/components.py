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
class Components:
    name: str
    smiles: str
    persistent_identifier_PID: str
    concentration: float
    concentration_unit: str
    supplier: str
    purity: float
    formulation: str
    solubility_limit: float
    solubility_limit_unit: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Components/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Components",
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
class StorageConditions:
    temperature: float
    temperature_unit: str
    storage_start: date
    additives: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:StorageConditions/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:StorageConditions",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )