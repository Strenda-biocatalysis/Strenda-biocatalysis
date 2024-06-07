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
class SamplingDescription:
    volume_per_sample: float
    volume_per_sample_unit: str
    mixing_during_sampling: str
    vessel_opened_for_sampling: str
    gas_phase: str
    time: float

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:SamplingDescription/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:SamplingDescription",
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
class SamplingFromHeterogeneousReactionSolutions:
    phase: str
    biocatalyst_in_phase: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:SamplingFromHeterogeneousReactionSolutions/"
        + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:SamplingFromHeterogeneousReactionSolutions",
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
class SamplePreprocessing:
    quenching_method: str
    quenching_ratio: str
    treatment_procedure: str
    special_treatment: str

    # JSON-LD fields
    id: str = field(
        metadata=config(field_name="@id"),
        default_factory=lambda: "stbc:SamplePreprocessing/" + str(uuid4()),
    )
    __type__: list[str] = field(
        metadata=config(field_name="@type"),
        default_factory=lambda: [
            "stbc:SamplePreprocessing",
        ],
    )
    __context__: dict[str, str | dict] = field(
        metadata=config(field_name="@context"),
        default_factory=lambda: {
            "stbc": "https://www.github.com/my/repo/",
        },
    )
