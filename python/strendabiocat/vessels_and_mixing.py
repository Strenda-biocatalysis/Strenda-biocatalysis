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


class VesselAndMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    vessel: Vessel = Field(
        default=...,
        description="""Physical container or reactor used for the
        enzymatic reaction.""",
    )
    mixing: Optional[Mixing] = Field(
        default=None,
        description="""Mixing system and parameters employed during the
        reaction.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes or comments about the vessel and
        mixing setup.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:VesselAndMixing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:VesselAndMixing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "Vessel": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Vessel/",
            "Mixing": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Mixing/",
            "vessel": "stbc:VesselAndMixing/vessel",
            "mixing": "stbc:VesselAndMixing/mixing",
            "notes": "stbc:VesselAndMixing/notes",
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


class Vessel(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    vessel_type: VesselType = Field(
        default=...,
        description="""Type of vessel or reactor configuration used for
        the reaction.""",
    )
    material: Optional[str] = Field(
        default=None,
        description="""Material composition of the vessel (e.g., glass,
        plastic, stainless steel).""",
    )
    size: Optional[float] = Field(
        default=None,
        description="""Volume or capacity of the vessel.""",
    )
    size_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the size.""",
    )
    geometry: Optional[str] = Field(
        default=None,
        description="""Geometric shape and dimensions of the vessel.""",
    )
    closure: Optional[Closure] = Field(
        default=None,
        description="""Sealing and closure system for the vessel.""",
    )
    supplier: Optional[str] = Field(
        default=None,
        description="""Manufacturer or supplier of the vessel.""",
    )
    lot_number: Optional[str] = Field(
        default=None,
        description="""Batch or lot number for traceability.""",
    )
    reactor_specifics: Optional[ReactorSpecifics] = Field(
        default=None,
        description="""Additional reactor-specific configurations and
        features.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the vessel specifications.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Vessel/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Vessel",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "VesselType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#VesselType/",
            "Closure": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Closure/",
            "ReactorSpecifics": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ReactorSpecifics/",
            "vessel_type": "stbc:Vessel/vessel_type",
            "material": "stbc:Vessel/material",
            "size": "stbc:Vessel/size",
            "size_unit": "stbc:Vessel/size_unit",
            "geometry": "stbc:Vessel/geometry",
            "closure": "stbc:Vessel/closure",
            "supplier": "stbc:Vessel/supplier",
            "lot_number": "stbc:Vessel/lot_number",
            "reactor_specifics": "stbc:Vessel/reactor_specifics",
            "notes": "stbc:Vessel/notes",
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


class Closure(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    closure_type: Optional[str] = Field(
        default=None,
        description="""Type of closure mechanism (e.g., screw cap,
        septum, crimp cap).""",
    )
    sealing_material: Optional[str] = Field(
        default=None,
        description="""Material used for sealing (e.g., PTFE, silicone,
        rubber).""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the closure system.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Closure/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Closure",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "closure_type": "stbc:Closure/closure_type",
            "sealing_material": "stbc:Closure/sealing_material",
            "notes": "stbc:Closure/notes",
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


class ReactorSpecifics(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    gas_handling: Optional[GasHandling] = Field(
        default=None,
        description="""Gas supply and handling system for the reactor.""",
    )
    tubing: Optional[str] = Field(
        default=None,
        description="""Tubing specifications and connections used in the
        reactor setup.""",
    )
    catalyst_localisation: Optional[str] = Field(
        default=None,
        description="""Method or system for localizing or immobilizing
        the catalyst within the reactor.""",
    )
    temperature_control: Optional[str] = Field(
        default=None,
        description="""Temperature control and regulation system
        employed.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ReactorSpecifics/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ReactorSpecifics",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "GasHandling": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#GasHandling/",
            "gas_handling": "stbc:ReactorSpecifics/gas_handling",
            "tubing": "stbc:ReactorSpecifics/tubing",
            "catalyst_localisation": "stbc:ReactorSpecifics/catalyst_localisation",
            "temperature_control": "stbc:ReactorSpecifics/temperature_control",
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


class GasHandling(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    gas_type: Optional[str] = Field(
        default=None,
        description="""Type of gas used (e.g., nitrogen, oxygen, argon,
        air).""",
    )
    supply_method: Optional[str] = Field(
        default=None,
        description="""Method of gas supply (e.g., continuous flow,
        headspace purging, bubbling).""",
    )
    supply_rate: Optional[float] = Field(
        default=None,
        description="""Rate of gas supply or flow into the reactor.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:GasHandling/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:GasHandling",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "gas_type": "stbc:GasHandling/gas_type",
            "supply_method": "stbc:GasHandling/supply_method",
            "supply_rate": "stbc:GasHandling/supply_rate",
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


class Mixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    mixing_type: MixingType = Field(
        default=...,
        description="""Primary type of mixing employed in the reaction
        system.""",
    )
    shaking: Optional[ShakingMixing] = Field(
        default=None,
        description="""Shaking-based mixing parameters and configuration.""",
    )
    mechanical: Optional[MechanicalMixing] = Field(
        default=None,
        description="""Mechanical stirring parameters and equipment
        specifications.""",
    )
    fluid: Optional[FluidImpelledMixing] = Field(
        default=None,
        description="""Fluid-driven mixing parameters for flow-based
        systems.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the mixing strategy and
        implementation.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Mixing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Mixing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "MixingType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#MixingType/",
            "ShakingMixing": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ShakingMixing/",
            "MechanicalMixing": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#MechanicalMixing/",
            "FluidImpelledMixing": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#FluidImpelledMixing/",
            "mixing_type": "stbc:Mixing/mixing_type",
            "shaking": "stbc:Mixing/shaking",
            "mechanical": "stbc:Mixing/mechanical",
            "fluid": "stbc:Mixing/fluid",
            "notes": "stbc:Mixing/notes",
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


class ShakingMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    shaking_type: Optional[str] = Field(
        default=None,
        description="""Type of shaking motion (e.g., orbital, linear,
        reciprocal).""",
    )
    deflection: Optional[float] = Field(
        default=None,
        description="""Amplitude or deflection distance of the shaking
        motion.""",
    )
    speed: Optional[float] = Field(
        default=None,
        description="""Frequency or speed of the shaking motion.""",
    )
    vessel_position: Optional[str] = Field(
        default=None,
        description="""Orientation or position of the vessel during
        shaking.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the shaking mixing setup.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ShakingMixing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ShakingMixing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "shaking_type": "stbc:ShakingMixing/shaking_type",
            "deflection": "stbc:ShakingMixing/deflection",
            "speed": "stbc:ShakingMixing/speed",
            "vessel_position": "stbc:ShakingMixing/vessel_position",
            "notes": "stbc:ShakingMixing/notes",
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


class MechanicalMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    stirring_type: Optional[str] = Field(
        default=None,
        description="""Type of mechanical stirring (e.g., overhead,
        magnetic, impeller).""",
    )
    stirrer_material: Optional[str] = Field(
        default=None,
        description="""Material composition of the stirrer or impeller.""",
    )
    supplier: Optional[str] = Field(
        default=None,
        description="""Manufacturer or supplier of the stirring
        equipment.""",
    )
    number_of_stirrers: Optional[int] = Field(
        default=None,
        description="""Number of stirrers or impellers used in the
        system.""",
    )
    stirrer_geometry: Optional[str] = Field(
        default=None,
        description="""Geometric design and shape of the stirrer or
        impeller.""",
    )
    blade_pitch_angle: Optional[float] = Field(
        default=None,
        description="""Angle of the stirrer blades relative to the
        horizontal plane.""",
    )
    blade_size: Optional[float] = Field(
        default=None,
        description="""Dimensions or size of the stirrer blades.""",
    )
    stirrer_speed: Optional[float] = Field(
        default=None,
        description="""Rotational speed of the stirrer or impeller.""",
    )
    height_above_base: Optional[float] = Field(
        default=None,
        description="""Distance of the stirrer from the bottom of the
        vessel.""",
    )
    power_per_volume: Optional[float] = Field(
        default=None,
        description="""Power input per unit volume of the reaction
        mixture.""",
    )
    stir_bar: Optional[StirBar] = Field(
        default=None,
        description="""Magnetic stir bar specifications for magnetic
        stirring systems.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the mechanical mixing
        setup.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:MechanicalMixing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:MechanicalMixing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "StirBar": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#StirBar/",
            "stirring_type": "stbc:MechanicalMixing/stirring_type",
            "stirrer_material": "stbc:MechanicalMixing/stirrer_material",
            "supplier": "stbc:MechanicalMixing/supplier",
            "number_of_stirrers": "stbc:MechanicalMixing/number_of_stirrers",
            "stirrer_geometry": "stbc:MechanicalMixing/stirrer_geometry",
            "blade_pitch_angle": "stbc:MechanicalMixing/blade_pitch_angle",
            "blade_size": "stbc:MechanicalMixing/blade_size",
            "stirrer_speed": "stbc:MechanicalMixing/stirrer_speed",
            "height_above_base": "stbc:MechanicalMixing/height_above_base",
            "power_per_volume": "stbc:MechanicalMixing/power_per_volume",
            "stir_bar": "stbc:MechanicalMixing/stir_bar",
            "notes": "stbc:MechanicalMixing/notes",
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


class StirBar(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    size: Optional[float] = Field(
        default=None,
        description="""Length and diameter of the magnetic stir bar.""",
    )
    shape: Optional[str] = Field(
        default=None,
        description="""Shape of the stir bar (e.g., cylindrical,
        octagonal, cross-shaped).""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:StirBar/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:StirBar",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "size": "stbc:StirBar/size",
            "shape": "stbc:StirBar/shape",
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


class FluidImpelledMixing(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    phase_volume_description: Optional[str] = Field(
        default=None,
        description="""Description of phase volumes and their
        distribution in the flow system.""",
    )
    residence_time: Optional[float] = Field(
        default=None,
        description="""Average residence time of the fluid in the mixing
        zone.""",
    )
    reynolds_number: Optional[str] = Field(
        default=None,
        description="""Reynolds number characterizing the flow regime and
        mixing intensity.""",
    )
    passive_mixing: Optional[str] = Field(
        default=None,
        description="""Description of passive mixing elements or
        structures used.""",
    )
    active_mixer: Optional[str] = Field(
        default=None,
        description="""Description of active mixing devices or mechanisms
        employed.""",
    )
    pulsing: Optional[str] = Field(
        default=None,
        description="""Pulsing or oscillatory flow patterns used to
        enhance mixing.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the fluid-impelled mixing
        system.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:FluidImpelledMixing/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:FluidImpelledMixing",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "phase_volume_description": "stbc:FluidImpelledMixing/phase_volume_description",
            "residence_time": "stbc:FluidImpelledMixing/residence_time",
            "reynolds_number": "stbc:FluidImpelledMixing/reynolds_number",
            "passive_mixing": "stbc:FluidImpelledMixing/passive_mixing",
            "active_mixer": "stbc:FluidImpelledMixing/active_mixer",
            "pulsing": "stbc:FluidImpelledMixing/pulsing",
            "notes": "stbc:FluidImpelledMixing/notes",
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


class VesselType(Enum):
    OTHER = "other"
    PLATE = "plate"
    STIRRED_TANK = "stirred_tank"
    TUBULAR_FLOW = "tubular_flow"
    VIAL = "vial"


class MixingType(Enum):
    COMBINED = "combined"
    FLUID_IMPELLED = "fluid_impelled"
    MECHANICAL = "mechanical"
    NONE = "none"
    SHAKING = "shaking"


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
