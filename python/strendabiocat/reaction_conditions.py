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


class ReactionConditions(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    reactor: ReactorSetup = Field(
        default=...,
        description="""Configuration and specifications of the reactor
        used for the biocatalytic reaction.""",
    )
    system: ReactionSystem = Field(
        default=...,
        description="""Characterization of the reaction system as
        monoliquid or multiphasic.""",
    )
    phases: list[Phase] = Field(
        default_factory=list,
        description="""Individual phases present in the reaction system
        (liquid, solid, gas).""",
    )
    temperature: Optional[TemperatureProfile] = Field(
        default=None,
        description="""Temperature conditions throughout the reaction,
        which can be constant, event-based, or
        follow a gradient.""",
    )
    pH: Optional[PHProfile] = Field(
        default=None,
        description="""pH conditions throughout the reaction, which
        can be constant, event-based, or follow
        a gradient.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes or comments about the reaction
        conditions.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ReactionConditions/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ReactionConditions",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "ReactorSetup": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ReactorSetup/",
            "ReactionSystem": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ReactionSystem/",
            "Phase": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Phase/",
            "TemperatureProfile": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#TemperatureProfile/",
            "PHProfile": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PHProfile/",
            "reactor": "stbc:ReactionConditions/reactor",
            "system": "stbc:ReactionConditions/system",
            "phases": {
                "@id": "stbc:ReactionConditions/phases",
                "@container": "@list",
            },
            "temperature": "stbc:ReactionConditions/temperature",
            "pH": "stbc:ReactionConditions/pH",
            "notes": "stbc:ReactionConditions/notes",
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

    def filter_phases(self, **kwargs) -> list[Phase]:
        """Filters the phases attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Phase]: The filtered list of Phase objects
        """

        return FilterWrapper[Phase](self.phases, **kwargs).filter()

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

    def add_to_phases(
        self,
        phase_type: PhaseType,
        material_description: Optional[str] = None,
        amount: Optional[float] = None,
        amount_unit: Optional[str] = None,
        notes: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "phase_type": phase_type,
            "material_description": material_description,
            "amount": amount,
            "amount_unit": amount_unit,
            "notes": notes,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.phases.append(Phase(**params))

        return self.phases[-1]


class ReactorSetup(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    reactor_type: ReactorType = Field(
        default=...,
        description="""Type of reactor configuration used (well-mixed or
        tubular flow).""",
    )
    flow: Optional[FlowConditions] = Field(
        default=None,
        description="""Flow rate specifications for continuous or fed-
        batch operations.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the reactor setup.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ReactorSetup/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ReactorSetup",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "ReactorType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ReactorType/",
            "FlowConditions": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#FlowConditions/",
            "reactor_type": "stbc:ReactorSetup/reactor_type",
            "flow": "stbc:ReactorSetup/flow",
            "notes": "stbc:ReactorSetup/notes",
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


class FlowConditions(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    flow_rate: Optional[float] = Field(
        default=None,
        description="""Numerical value of the flow rate.""",
    )
    flow_rate_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the flow rate.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:FlowConditions/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:FlowConditions",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "flow_rate": "stbc:FlowConditions/flow_rate",
            "flow_rate_unit": "stbc:FlowConditions/flow_rate_unit",
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


class ReactionSystem(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    system_type: SystemType = Field(
        default=...,
        description="""Classification of the system as monoliquid or
        multiphasic.""",
    )
    monoliquid: Optional[MonoliquidSystem] = Field(
        default=None,
        description="""Specifications for single-phase liquid systems.""",
    )
    multiphasic: Optional[MultiphasicSystem] = Field(
        default=None,
        description="""Specifications for systems containing multiple
        phases.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the reaction system.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ReactionSystem/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ReactionSystem",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "SystemType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SystemType/",
            "MonoliquidSystem": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#MonoliquidSystem/",
            "MultiphasicSystem": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#MultiphasicSystem/",
            "system_type": "stbc:ReactionSystem/system_type",
            "monoliquid": "stbc:ReactionSystem/monoliquid",
            "multiphasic": "stbc:ReactionSystem/multiphasic",
            "notes": "stbc:ReactionSystem/notes",
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


class MonoliquidSystem(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    solvent_description: Optional[str] = Field(
        default=None,
        description="""Detailed description of the solvent or solvent
        mixture used.""",
    )
    ionic_strength: Optional[float] = Field(
        default=None,
        description="""Ionic strength of the solution, affecting enzyme
        activity and stability.""",
    )
    further_additives: Optional[str] = Field(
        default=None,
        description="""Description of any additional additives present in
        the system.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the monoliquid system.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:MonoliquidSystem/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:MonoliquidSystem",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "solvent_description": "stbc:MonoliquidSystem/solvent_description",
            "ionic_strength": "stbc:MonoliquidSystem/ionic_strength",
            "further_additives": "stbc:MonoliquidSystem/further_additives",
            "notes": "stbc:MonoliquidSystem/notes",
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


class MultiphasicSystem(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    phases_number: Optional[int] = Field(
        default=None,
        description="""Total number of distinct phases present in the
        system.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the multiphasic system.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:MultiphasicSystem/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:MultiphasicSystem",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "phases_number": "stbc:MultiphasicSystem/phases_number",
            "notes": "stbc:MultiphasicSystem/notes",
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


class Phase(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    phase_type: PhaseType = Field(
        default=...,
        description="""Physical state of the phase (liquid, solid, or
        gas).""",
    )
    material_description: Optional[str] = Field(
        default=None,
        description="""Detailed description of the materials comprising
        this phase.""",
    )
    amount: Optional[float] = Field(
        default=None,
        description="""Quantity of material in this phase.""",
    )
    amount_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the amount.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about this specific phase.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Phase/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Phase",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "PhaseType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PhaseType/",
            "phase_type": "stbc:Phase/phase_type",
            "material_description": "stbc:Phase/material_description",
            "amount": "stbc:Phase/amount",
            "amount_unit": "stbc:Phase/amount_unit",
            "notes": "stbc:Phase/notes",
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


class TemperatureProfile(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    profile_type: ProfileType = Field(
        default=...,
        description="""Type of temperature profile used (constant, event-
        based, multipoint, or gradient).""",
    )
    temperature_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for temperature values.""",
    )
    constant_temperature: Optional[float] = Field(
        default=None,
        description="""Temperature value for constant temperature
        profiles.""",
    )
    profile_points: list[ProfilePoint] = Field(
        default_factory=list,
        description="""Series of temperature points for event-based or
        multipoint profiles.""",
    )
    gradient: Optional[Gradient] = Field(
        default=None,
        description="""Gradient specifications for temperature ramp
        profiles.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the temperature profile.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:TemperatureProfile/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:TemperatureProfile",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "ProfileType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ProfileType/",
            "ProfilePoint": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ProfilePoint/",
            "Gradient": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Gradient/",
            "profile_type": "stbc:TemperatureProfile/profile_type",
            "temperature_unit": "stbc:TemperatureProfile/temperature_unit",
            "constant_temperature": "stbc:TemperatureProfile/constant_temperature",
            "profile_points": {
                "@id": "stbc:TemperatureProfile/profile_points",
                "@container": "@list",
            },
            "gradient": "stbc:TemperatureProfile/gradient",
            "notes": "stbc:TemperatureProfile/notes",
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

    def filter_profile_points(self, **kwargs) -> list[ProfilePoint]:
        """Filters the profile_points attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[ProfilePoint]: The filtered list of ProfilePoint objects
        """

        return FilterWrapper[ProfilePoint](self.profile_points, **kwargs).filter()

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

    def add_to_profile_points(
        self,
        value: Optional[float] = None,
        time: Optional[float] = None,
        time_unit: Optional[str] = None,
        event_description: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "value": value,
            "time": time,
            "time_unit": time_unit,
            "event_description": event_description,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.profile_points.append(ProfilePoint(**params))

        return self.profile_points[-1]


class ProfilePoint(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    value: Optional[float] = Field(
        default=None,
        description="""Temperature value at this point.""",
    )
    time: Optional[float] = Field(
        default=None,
        description="""Time at which this temperature is measured or set.""",
    )
    time_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the time value.""",
    )
    event_description: Optional[str] = Field(
        default=None,
        description="""Description of any specific event associated with
        this temperature point.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ProfilePoint/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ProfilePoint",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "value": "stbc:ProfilePoint/value",
            "time": "stbc:ProfilePoint/time",
            "time_unit": "stbc:ProfilePoint/time_unit",
            "event_description": "stbc:ProfilePoint/event_description",
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


class Gradient(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    start_value: Optional[float] = Field(
        default=None,
        description="""Initial temperature value at the beginning of
        the gradient.""",
    )
    end_value: Optional[float] = Field(
        default=None,
        description="""Final temperature value at the end of the
        gradient.""",
    )
    length: Optional[float] = Field(
        default=None,
        description="""Duration or distance over which the gradient is
        applied.""",
    )
    length_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the gradient length (time
        or distance).""",
    )
    measurement_points: Optional[str] = Field(
        default=None,
        description="""Description of how temperature is measured along
        the gradient.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Gradient/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Gradient",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "start_value": "stbc:Gradient/start_value",
            "end_value": "stbc:Gradient/end_value",
            "length": "stbc:Gradient/length",
            "length_unit": "stbc:Gradient/length_unit",
            "measurement_points": "stbc:Gradient/measurement_points",
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


class PHProfile(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    profile_type: ProfileType = Field(
        default=...,
        description="""Type of pH profile used (constant, event-based,
        multipoint, or gradient).""",
    )
    constant_pH: Optional[float] = Field(
        default=None,
        description="""pH value for constant pH profiles.""",
    )
    profile_points: list[PHPoint] = Field(
        default_factory=list,
        description="""Series of pH points for event-based or multipoint
        profiles.""",
    )
    gradient: Optional[PHGradient] = Field(
        default=None,
        description="""Gradient specifications for pH ramp profiles.""",
    )
    detection: Optional[PHDetection] = Field(
        default=None,
        description="""Methods and conditions used for pH detection and
        measurement.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the pH profile.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:PHProfile/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:PHProfile",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "ProfileType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ProfileType/",
            "PHPoint": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PHPoint/",
            "PHGradient": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PHGradient/",
            "PHDetection": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PHDetection/",
            "profile_type": "stbc:PHProfile/profile_type",
            "constant_pH": "stbc:PHProfile/constant_pH",
            "profile_points": {
                "@id": "stbc:PHProfile/profile_points",
                "@container": "@list",
            },
            "gradient": "stbc:PHProfile/gradient",
            "detection": "stbc:PHProfile/detection",
            "notes": "stbc:PHProfile/notes",
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

    def filter_profile_points(self, **kwargs) -> list[PHPoint]:
        """Filters the profile_points attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[PHPoint]: The filtered list of PHPoint objects
        """

        return FilterWrapper[PHPoint](self.profile_points, **kwargs).filter()

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

    def add_to_profile_points(
        self,
        value: Optional[float] = None,
        time: Optional[float] = None,
        time_unit: Optional[str] = None,
        event_description: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "value": value,
            "time": time,
            "time_unit": time_unit,
            "event_description": event_description,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.profile_points.append(PHPoint(**params))

        return self.profile_points[-1]


class PHPoint(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    value: Optional[float] = Field(
        default=None,
        description="""pH value at this point.""",
    )
    time: Optional[float] = Field(
        default=None,
        description="""Time at which this pH is measured or set.""",
    )
    time_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the time value.""",
    )
    event_description: Optional[str] = Field(
        default=None,
        description="""Description of any specific event associated with
        this pH point.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:PHPoint/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:PHPoint",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "value": "stbc:PHPoint/value",
            "time": "stbc:PHPoint/time",
            "time_unit": "stbc:PHPoint/time_unit",
            "event_description": "stbc:PHPoint/event_description",
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


class PHGradient(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    start_value: Optional[float] = Field(
        default=None,
        description="""Initial pH value at the beginning of the gradient.""",
    )
    end_value: Optional[float] = Field(
        default=None,
        description="""Final pH value at the end of the gradient.""",
    )
    length: Optional[float] = Field(
        default=None,
        description="""Duration over which the pH gradient is applied.""",
    )
    length_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the gradient duration.""",
    )
    measurement_points: list[float] = Field(
        default_factory=list,
        description="""Measurement points along the gradient.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:PHGradient/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:PHGradient",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "start_value": "stbc:PHGradient/start_value",
            "end_value": "stbc:PHGradient/end_value",
            "length": "stbc:PHGradient/length",
            "length_unit": "stbc:PHGradient/length_unit",
            "measurement_points": {
                "@id": "stbc:PHGradient/measurement_points",
                "@container": "@list",
            },
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


class PHDetection(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    detected_when: Optional[str] = Field(
        default=None,
        description="""Timing or conditions under which pH is detected.""",
    )
    detected_how: Optional[str] = Field(
        default=None,
        description="""Method or instrument used for pH detection.""",
    )
    temperature: Optional[float] = Field(
        default=None,
        description="""Temperature at which pH measurements are
        calibrated or performed.""",
    )
    temperature_unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the calibration
        temperature.""",
    )
    calibration_pH_electrode: Optional[str] = Field(
        default=None,
        description="""Details about pH electrode calibration procedures
        and standards.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:PHDetection/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:PHDetection",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "detected_when": "stbc:PHDetection/detected_when",
            "detected_how": "stbc:PHDetection/detected_how",
            "temperature": "stbc:PHDetection/temperature",
            "temperature_unit": "stbc:PHDetection/temperature_unit",
            "calibration_pH_electrode": "stbc:PHDetection/calibration_pH_electrode",
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


class SystemType(Enum):
    MONOLIQUID = "monoliquid"
    MULTIPHASIC = "multiphasic"


class ProfileType(Enum):
    CONSTANT = "constant"
    EVENT_BASED = "event_based"
    GRADIENT = "gradient"
    MULTIPOINT = "multipoint"


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
