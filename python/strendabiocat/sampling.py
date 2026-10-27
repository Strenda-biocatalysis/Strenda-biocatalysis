"""
This file contains Pydantic model definitions for data validation.

Pydantic is a data validation library that uses Python type annotations.
It allows you to define data models with type hints that are validated
at runtime while providing static type checking.

Usage example:
```python
from my_model import MyModel

# Validates data at runtime
my_model = MyModel(name="John", age=30)

# Type-safe - my_model has correct type hints
print(my_model.name)

# Will raise error if validation fails
try:
    MyModel(name="", age=30)
except ValidationError as e:
    print(e)
```

For more information see:
https://docs.pydantic.dev/

WARNING: This is an auto-generated file.
Do not edit directly - any changes will be overwritten.
"""


## This is a generated file. Do not modify it manually!

from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional, Generic, TypeVar, Union
from enum import Enum
from uuid import uuid4
from datetime import date, datetime

# Filter Wrapper definition used to filter a list of objects
# based on their attributes
Cls = TypeVar("Cls")


class FilterWrapper(Generic[Cls]):
    """Wrapper class to filter a list of objects based on their attributes"""

    def __init__(self, collection: list[Cls], **kwargs):
        self.collection = collection
        self.kwargs = kwargs

    def filter(self) -> list[Cls]:
        for key, value in self.kwargs.items():
            self.collection = [
                item for item in self.collection if self._fetch_attr(key, item) == value
            ]
        return self.collection

    def _fetch_attr(self, name: str, item: Cls):
        try:
            return getattr(item, name)
        except AttributeError:
            raise AttributeError(f"{item} does not have attribute {name}")


# JSON-LD Helper Functions

# JSON-LD 1.1 only uses a plain string term as a prefix if its IRI ends in one of these
GEN_DELIMS = (":", "/", "?", "#", "[", "]", "@")


def add_namespace(obj, prefix: str | None, iri: str | None):
    """Adds a namespace to the JSON-LD context

    Args:
        prefix (str): The prefix to add
        iri (str): The IRI to add
    """
    if prefix is None and iri is None:
        return
    elif prefix and iri is None:
        raise ValueError("If prefix is provided, iri must also be provided")
    elif iri and prefix is None:
        raise ValueError("If iri is provided, prefix must also be provided")

    if iri.endswith(GEN_DELIMS):  # type: ignore
        obj.ld_context[prefix] = iri  # type: ignore
    else:
        obj.ld_context[prefix] = {"@id": iri, "@prefix": True}  # type: ignore


def validate_prefix(term: str | dict, prefix: str):
    """Validates that a term is prefixed with a given prefix

    Args:
        term (str): The term to validate
        prefix (str): The prefix to validate against

    Returns:
        bool: True if the term is prefixed with the prefix, False otherwise
    """

    if isinstance(term, dict) and not term["@id"].startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")
    elif isinstance(term, str) and not term.startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")


def merge_ld_type(defaults: list[str], value: str | list | None) -> list[str]:
    """Keeps the generated types and appends extra types read from a document;
    a bare string (compacted JSON-LD) is treated as a single type"""
    if value is None:
        return defaults
    if isinstance(value, str):
        value = [value]
    return defaults + [t for t in value if t not in defaults]


def merge_ld_context(defaults: dict, value: dict | list | str | None) -> dict:
    """Keeps extra prefixes and terms read from a document; generated mappings win,
    so documents written with an older context get the current term definitions.
    Lists are merged element-wise; remote context URLs are ignored"""
    if isinstance(value, dict):
        value = [value]
    elif not isinstance(value, list):
        return defaults
    extras = {k: v for d in value if isinstance(d, dict) for k, v in d.items()}
    return {**defaults, **{k: v for k, v in extras.items() if k not in defaults}}


# Model Definitions


class Sampling(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    sampling_applied: bool = Field(
        default=...,
        description="""Indicates whether physical sampling was performed
        at all.""",
    )
    strategy: Optional[SamplingStrategy] = Field(
        default=None,
        description="""Details about the sampling strategy and
        methodology used.""",
    )
    samples: list[Sample] = Field(
        default_factory=list,
        description="""Collection of individual samples taken during
        the reaction.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes or comments about the sampling
        procedure.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Sampling/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Sampling",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "SamplingStrategy": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SamplingStrategy/",
            "Sample": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Sample/",
            "sampling_applied": "stbc:Sampling/sampling_applied",
            "strategy": "stbc:Sampling/strategy",
            "samples": {
                "@id": "stbc:Sampling/samples",
                "@container": "@list",
            },
            "notes": "stbc:Sampling/notes",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def filter_samples(self, **kwargs) -> list[Sample]:
        """Filters the samples attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Sample]: The filtered list of Sample objects
        """

        return FilterWrapper[Sample](self.samples, **kwargs).filter()

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)

    def add_to_samples(
        self,
        time: Optional[float] = None,
        time_unit: Optional[str] = None,
        amount: Optional[float] = None,
        amount_unit: Optional[str] = None,
        phase: Optional[PhaseType] = None,
        biocatalyst_in_sample: Optional[str] = None,
        preprocessing: Optional[SamplePreprocessing] = None,
        notes: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "time": time,
            "time_unit": time_unit,
            "amount": amount,
            "amount_unit": amount_unit,
            "phase": phase,
            "biocatalyst_in_sample": biocatalyst_in_sample,
            "preprocessing": preprocessing,
            "notes": notes,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.samples.append(Sample(**params))

        return self.samples[-1]


class SamplingStrategy(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    strategy_type: SamplingStrategyType = Field(
        default=...,
        description="""Type of sampling strategy employed (default or
        specialized).""",
    )
    mixing_during_sampling: Optional[str] = Field(
        default=None,
        description="""Description of mixing conditions maintained during
        sample collection.""",
    )
    vessel_opened: Optional[bool] = Field(
        default=None,
        description="""Indicates whether the reaction vessel was opened
        during sampling.""",
    )
    gas_phase: Optional[str] = Field(
        default=None,
        description="""Description of gas phase conditions or handling
        during sampling.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the sampling strategy.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:SamplingStrategy/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:SamplingStrategy",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "SamplingStrategyType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SamplingStrategyType/",
            "strategy_type": "stbc:SamplingStrategy/strategy_type",
            "mixing_during_sampling": "stbc:SamplingStrategy/mixing_during_sampling",
            "vessel_opened": "stbc:SamplingStrategy/vessel_opened",
            "gas_phase": "stbc:SamplingStrategy/gas_phase",
            "notes": "stbc:SamplingStrategy/notes",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Sample(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    time: Optional[float] = Field(
        default=None,
        description="""Time point at which the sample was collected.""",
    )
    time_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the sampling time.""",
    )
    amount: Optional[float] = Field(
        default=None,
        description="""Amount or volume of sample collected.""",
    )
    amount_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the amount.""",
    )
    phase: Optional[PhaseType] = Field(
        default=None,
        description="""Phase from which the sample was collected (liquid,
        solid, gas, etc.).""",
    )
    biocatalyst_in_sample: Optional[str] = Field(
        default=None,
        description="""Description of biocatalyst presence or handling in
        the sample.""",
    )
    preprocessing: Optional[SamplePreprocessing] = Field(
        default=None,
        description="""Any preprocessing steps applied to the sample
        before analysis.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the individual sample.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Sample/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Sample",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "PhaseType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PhaseType/",
            "SamplePreprocessing": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SamplePreprocessing/",
            "time": "stbc:Sample/time",
            "time_unit": "stbc:Sample/time_unit",
            "amount": "stbc:Sample/amount",
            "amount_unit": "stbc:Sample/amount_unit",
            "phase": "stbc:Sample/phase",
            "biocatalyst_in_sample": "stbc:Sample/biocatalyst_in_sample",
            "preprocessing": "stbc:Sample/preprocessing",
            "notes": "stbc:Sample/notes",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SamplePreprocessing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    quenching_method: Optional[str] = Field(
        default=None,
        description="""Method used to quench or stop the reaction in
        the sample.""",
    )
    quenching_ratio: Optional[float] = Field(
        default=None,
        description="""Ratio or proportion of quenching agent to sample.""",
    )
    treatment_procedure: Optional[str] = Field(
        default=None,
        description="""Additional treatment procedures applied to the
        sample.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about sample preprocessing.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:SamplePreprocessing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:SamplePreprocessing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "quenching_method": "stbc:SamplePreprocessing/quenching_method",
            "quenching_ratio": "stbc:SamplePreprocessing/quenching_ratio",
            "treatment_procedure": "stbc:SamplePreprocessing/treatment_procedure",
            "notes": "stbc:SamplePreprocessing/notes",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Quantity(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    value: Optional[float] = Field(
        default=None,
        description="""Numerical value of the measurement.""",
    )
    unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the value.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Quantity/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Quantity",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "value": "stbc:Quantity/value",
            "unit": "stbc:Quantity/unit",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class StorageConditions(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    temperature: Optional[float] = Field(
        default=None,
        description="""Storage temperature value.""",
    )
    temperature_unit: Optional[str] = Field(
        default=None,
        description="""Unit for the storage temperature (e.g., °C, K).""",
    )
    storage_start: Optional[date] = Field(
        default=None,
        description="""Date when storage under these conditions began or
        material was received.""",
    )
    additives: list[str] = Field(
        default_factory=list,
        description="""Any additives or stabilizers used during
        storage (e.g., glycerol, stabilizers,
        preservatives).""",
    )
    drying_method: list[str] = Field(
        default_factory=list,
        description="""Method used to dry the material if stored
        in dry form (optional, primarily for
        biocatalysts).""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about storage conditions or
        requirements.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:StorageConditions/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:StorageConditions",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "temperature": "stbc:StorageConditions/temperature",
            "temperature_unit": "stbc:StorageConditions/temperature_unit",
            "storage_start": {
                "@id": "stbc:StorageConditions/storage_start",
                "@type": "http://www.w3.org/2001/XMLSchema#date",
            },
            "additives": {
                "@id": "stbc:StorageConditions/additives",
                "@container": "@list",
            },
            "drying_method": {
                "@id": "stbc:StorageConditions/drying_method",
                "@container": "@list",
            },
            "notes": "stbc:StorageConditions/notes",
        },
    )

    @field_validator("ld_id", mode="before")
    @classmethod
    def _default_ld_id(cls, value):
        return cls.model_fields["ld_id"].default_factory() if value is None else value  # type: ignore

    @field_validator("ld_type", mode="before")
    @classmethod
    def _merge_ld_type(cls, value: str | list | None) -> list[str]:
        return merge_ld_type(cls.model_fields["ld_type"].default_factory(), value)  # type: ignore

    @field_validator("ld_context", mode="before")
    @classmethod
    def _merge_ld_context(
        cls, value: dict | list | str | None
    ) -> dict[str, str | dict]:
        return merge_ld_context(cls.model_fields["ld_context"].default_factory(), value)  # type: ignore

    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None,
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, (
            f"Attribute {attr} not found in {self.__class__.__name__}"
        )

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self, term: str, prefix: str | None = None, iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SamplingStrategyType(Enum):
    DEFAULT = "default"
    SPECIALISED = "specialised"


class FormulationType(Enum):
    DISSOLVED = "dissolved"
    GAS = "gas"
    LIQUID = "liquid"
    OTHER = "other"
    POWDER = "powder"
    SOLUTION = "solution"


class PhaseType(Enum):
    GAS = "gas"
    LIQUID = "liquid"
    MIXED = "mixed"
    OTHER = "other"
    SOLID = "solid"


class ReactorType(Enum):
    OTHER = "other"
    TUBULAR_FLOW = "tubular_flow"
    WELL_MIXED = "well_mixed"
