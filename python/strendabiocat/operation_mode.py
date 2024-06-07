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
class Batch:
    reactor_type: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Batch/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Batch",
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
class FedBatch:
    reactor_type: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:FedBatch/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:FedBatch",
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
class Continuous:
    reactor_type: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Continuous/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:Continuous",
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
class CombinatorialMode:
    reactor_type: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:CombinatorialMode/" + str(uuid4())
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory = lambda: [
            "stbc:CombinatorialMode",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory = lambda: {
            "stbc": "https://www.github.com/my/repo/",
        }
    )