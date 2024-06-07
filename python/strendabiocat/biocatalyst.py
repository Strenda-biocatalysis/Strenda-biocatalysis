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
class BiocatalystPurchased:
    name: str
    ec_number: str
    molecular_weight: float
    molecular_weight_unit: str
    catalyzed_reaction: str
    sequence_amino_acid: str
    sequence_DNA: str
    origin_organism: str
    supplier: str
    production_organism: str
    posttranslational_modification: str
    purity: float
    purity_specification: str
    formulation: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:BiocatalystPurchased/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:BiocatalystPurchased",
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
class BiocatalystSelfProduced:
    name: str
    ec_number: str
    molecular_weight: float
    molecular_weight_unit: str
    catalyzed_reaction: str
    sequence_amino_acid: str
    sequence_DNA: str
    sequence_plasmid: str
    plasmid_specifications: str
    origin_organism: str
    production_organism: str
    posttranslational_modification: str
    purity: float
    purity_specification: str
    purification_method: str
    formulation: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:BiocatalystSelfProduced/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:BiocatalystSelfProduced",
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
class PurifiedBiocatalyst:
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    activity: float
    activity_unit: str
    activity_determination_method: str
    formulation: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:PurifiedBiocatalyst/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:PurifiedBiocatalyst",
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
class CrudeCellExtract:
    cell_disruption_process: str
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:CrudeCellExtract/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:CrudeCellExtract",
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
class WholeCellBiocatalyst:
    harvesting_method: str
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    formulation: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:WholeCellBiocatalyst/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:WholeCellBiocatalyst",
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
class SecretedEnzyme:
    separation_method: str
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:SecretedEnzyme/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:SecretedEnzyme",
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
class CellFreeProduction:
    source_of_cellfree_extract: str
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:CellFreeProduction/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:CellFreeProduction",
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
class Immobilised:
    biocatalyst: str
    immobilisation_chemistry: str
    carrier_material: str
    linkers: str
    immobilisation_method: str
    purification_method: str
    concentration: float
    concentration_unit: str
    concentration_determination_method: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:Immobilised/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:Immobilised",
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
class StorageConditions:
    temperature: float
    temperature_unit: str
    storage_start: date
    additives: str
    drying_method: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:StorageConditions/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:StorageConditions",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )
