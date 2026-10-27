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


class ExperimentalResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    kinetics: Optional[KineticResults] = Field(
        default=None,
        description="""Kinetic parameters and enzyme behavior
        characteristics.""",
    )
    yield_and_conversion: Optional[YieldAndConversionResults] = Field(
        default=None,
        description="""Product yield and substrate conversion
        measurements.""",
    )
    activity: Optional[ActivityResults] = Field(
        default=None,
        description="""Enzyme activity and initial reaction rate data.""",
    )
    selectivity: Optional[SelectivityResults] = Field(
        default=None,
        description="""Selectivity measurements including
        stereoselectivity and enantioselectivity.""",
    )
    thermodynamics: Optional[ThermodynamicResults] = Field(
        default=None,
        description="""Thermodynamic parameters of the reaction.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes or comments about the
        experimental results.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ExperimentalResults/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ExperimentalResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "KineticResults": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#KineticResults/",
            "YieldAndConversionResults": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#YieldAndConversionResults/",
            "ActivityResults": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ActivityResults/",
            "SelectivityResults": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SelectivityResults/",
            "ThermodynamicResults": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ThermodynamicResults/",
            "kinetics": "stbc:ExperimentalResults/kinetics",
            "yield_and_conversion": "stbc:ExperimentalResults/yield_and_conversion",
            "activity": "stbc:ExperimentalResults/activity",
            "selectivity": "stbc:ExperimentalResults/selectivity",
            "thermodynamics": "stbc:ExperimentalResults/thermodynamics",
            "notes": "stbc:ExperimentalResults/notes",
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


class KineticResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    michaelis_constant: Optional[float] = Field(
        default=None,
        description="""Michaelis constant (Km) representing the substrate
        concentration at half-maximum reaction
        rate.""",
    )
    maximum_reaction_rate: Optional[float] = Field(
        default=None,
        description="""Maximum reaction rate (Vmax) achieved under
        saturating substrate conditions.""",
    )
    turnover_number: Optional[float] = Field(
        default=None,
        description="""Turnover number (kcat) representing the maximum
        number of substrate molecules converted
        per enzyme molecule per unit time.""",
    )
    catalytic_efficiency: Optional[float] = Field(
        default=None,
        description="""Catalytic efficiency (kcat/Km) indicating the
        enzyme's effectiveness at low substrate
        concentrations.""",
    )
    dissociation_constant: Optional[float] = Field(
        default=None,
        description="""Dissociation constant (Kd) for enzyme-substrate or
        enzyme-inhibitor binding.""",
    )
    inhibition: Optional[InhibitionParameters] = Field(
        default=None,
        description="""Parameters describing enzyme inhibition
        characteristics.""",
    )
    hill_coefficient: Optional[float] = Field(
        default=None,
        description="""Hill coefficient indicating cooperativity in
        substrate binding or enzyme kinetics.""",
    )
    enzyme_stability: Optional[str] = Field(
        default=None,
        description="""Qualitative or quantitative description of enzyme
        stability under reaction conditions.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about kinetic measurements or
        observations.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:KineticResults/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:KineticResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "InhibitionParameters": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#InhibitionParameters/",
            "michaelis_constant": "stbc:KineticResults/michaelis_constant",
            "maximum_reaction_rate": "stbc:KineticResults/maximum_reaction_rate",
            "turnover_number": "stbc:KineticResults/turnover_number",
            "catalytic_efficiency": "stbc:KineticResults/catalytic_efficiency",
            "dissociation_constant": "stbc:KineticResults/dissociation_constant",
            "inhibition": "stbc:KineticResults/inhibition",
            "hill_coefficient": "stbc:KineticResults/hill_coefficient",
            "enzyme_stability": "stbc:KineticResults/enzyme_stability",
            "notes": "stbc:KineticResults/notes",
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


class InhibitionParameters(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    inhibition_type: Optional[InhibitionType] = Field(
        default=None,
        description="""Type of inhibition mechanism observed.""",
    )
    inhibition_constant: Optional[float] = Field(
        default=None,
        description="""Inhibition constant (Ki) quantifying the strength
        of inhibitor binding.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:InhibitionParameters/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:InhibitionParameters",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "InhibitionType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#InhibitionType/",
            "inhibition_type": "stbc:InhibitionParameters/inhibition_type",
            "inhibition_constant": "stbc:InhibitionParameters/inhibition_constant",
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


class YieldAndConversionResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    product_yield: list[float] = Field(
        default_factory=list,
        description="""Product yield as percentage or fraction of
        theoretical maximum.""",
    )
    space_time_yield: Optional[float] = Field(
        default=None,
        description="""Space-time yield representing product formation
        rate per unit reactor volume.""",
    )
    conversion: Optional[float] = Field(
        default=None,
        description="""Substrate conversion as percentage or fraction of
        initial substrate consumed.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about yield and conversion
        measurements.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id",
        default_factory=lambda: "stbc:YieldAndConversionResults/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:YieldAndConversionResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "product_yield": {
                "@id": "stbc:YieldAndConversionResults/product_yield",
                "@container": "@list",
            },
            "space_time_yield": "stbc:YieldAndConversionResults/space_time_yield",
            "conversion": "stbc:YieldAndConversionResults/conversion",
            "notes": "stbc:YieldAndConversionResults/notes",
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


class ActivityResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    specific_activity: Optional[float] = Field(
        default=None,
        description="""Specific activity representing enzyme activity per
        unit mass of enzyme protein.""",
    )
    initial_reaction_rate: Optional[float] = Field(
        default=None,
        description="""Initial reaction rate measured at the beginning of
        the reaction.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about activity measurements.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ActivityResults/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ActivityResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "specific_activity": "stbc:ActivityResults/specific_activity",
            "initial_reaction_rate": "stbc:ActivityResults/initial_reaction_rate",
            "notes": "stbc:ActivityResults/notes",
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


class SelectivityResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    stereoselectivity: Optional[str] = Field(
        default=None,
        description="""Qualitative or quantitative description of
        stereoselectivity in the reaction.""",
    )
    enantioselectivity: Optional[float] = Field(
        default=None,
        description="""Enantioselectivity ratio (E-value) indicating
        preference for one enantiomer over
        another.""",
    )
    enantiomeric_excess: Optional[float] = Field(
        default=None,
        description="""Enantiomeric excess (ee) as percentage indicating
        optical purity of the product.""",
    )
    diastereomeric_excess: Optional[float] = Field(
        default=None,
        description="""Diastereomeric excess (de) as percentage for
        reactions producing diastereomers.""",
    )
    isomeric_content: Optional[float] = Field(
        default=None,
        description="""Content or ratio of specific isomers in the
        product mixture.""",
    )
    chemoselectivity: Optional[str] = Field(
        default=None,
        description="""Description of chemoselectivity when multiple
        reaction pathways are possible.""",
    )
    regioselectivity: Optional[str] = Field(
        default=None,
        description="""Description of regioselectivity indicating
        preference for specific reaction sites.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about selectivity measurements.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:SelectivityResults/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:SelectivityResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stereoselectivity": "stbc:SelectivityResults/stereoselectivity",
            "enantioselectivity": "stbc:SelectivityResults/enantioselectivity",
            "enantiomeric_excess": "stbc:SelectivityResults/enantiomeric_excess",
            "diastereomeric_excess": "stbc:SelectivityResults/diastereomeric_excess",
            "isomeric_content": "stbc:SelectivityResults/isomeric_content",
            "chemoselectivity": "stbc:SelectivityResults/chemoselectivity",
            "regioselectivity": "stbc:SelectivityResults/regioselectivity",
            "notes": "stbc:SelectivityResults/notes",
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


class ThermodynamicResults(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    gibbs_free_energy_change: Optional[str] = Field(
        default=None,
        description="""Gibbs free energy change (ΔG) for the reaction.""",
    )
    enthalpy_change: Optional[str] = Field(
        default=None,
        description="""Enthalpy change (ΔH) for the reaction.""",
    )
    entropy_change: Optional[str] = Field(
        default=None,
        description="""Entropy change (ΔS) for the reaction.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about thermodynamic measurements.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:ThermodynamicResults/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ThermodynamicResults",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "gibbs_free_energy_change": "stbc:ThermodynamicResults/gibbs_free_energy_change",
            "enthalpy_change": "stbc:ThermodynamicResults/enthalpy_change",
            "entropy_change": "stbc:ThermodynamicResults/entropy_change",
            "notes": "stbc:ThermodynamicResults/notes",
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


class InhibitionType(Enum):
    COMPETITIVE = "competitive"
    IRREVERSIBLE = "irreversible"
    MIXED = "mixed"
    NONCOMPETITIVE = "non_competitive"
    OTHER = "other"
    UNCOMPETITIVE = "uncompetitive"


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
