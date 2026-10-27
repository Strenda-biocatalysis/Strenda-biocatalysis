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


class Biocatalyst(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    identity: BiocatalystIdentity = Field(
        default=...,
        description="""Essential identifying information about the
        biocatalyst including name, EC number,
        molecular properties, and sequence data.""",
    )
    source_type: Optional[BiocatalystSourceType] = Field(
        default=None,
        description="""""",
    )
    source: Optional[BiocatalystSource] = Field(
        default=None,
        description="""Information about how the biocatalyst was
        obtained, whether purchased commercially
        or produced in-house.""",
    )
    application: Optional[BiocatalystApplication] = Field(
        default=None,
        description="""Details about how the biocatalyst is applied in
        the reaction, including concentration,
        activity, and workflow specifics.""",
    )
    immobilization: Optional[Immobilization] = Field(
        default=None,
        description="""Information about whether and how the biocatalyst
        is immobilized on a support material.""",
    )
    storage: Optional[StorageConditions] = Field(
        default=None,
        description="""Conditions under which the biocatalyst is stored
        to maintain its activity and stability.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes or comments about the biocatalyst
        that don't fit in other categories.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Biocatalyst/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Biocatalyst",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "BiocatalystIdentity": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystIdentity/",
            "BiocatalystSourceType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystSourceType/",
            "BiocatalystSource": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystSource/",
            "BiocatalystApplication": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystApplication/",
            "Immobilization": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Immobilization/",
            "StorageConditions": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#StorageConditions/",
            "identity": "stbc:Biocatalyst/identity",
            "source_type": "stbc:Biocatalyst/source_type",
            "source": "stbc:Biocatalyst/source",
            "application": "stbc:Biocatalyst/application",
            "immobilization": "stbc:Biocatalyst/immobilization",
            "storage": "stbc:Biocatalyst/storage",
            "notes": "stbc:Biocatalyst/notes",
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


class BiocatalystIdentity(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    name: str = Field(
        default=...,
        description="""The name of the biocatalyst, which can be the
        trivial name, systematic name, or trade
        name.""",
    )
    ec_number: list[str] = Field(
        default_factory=list,
        description="""The Enzyme Commission (EC) number that classifies
        the enzyme according to the reaction it
        catalyzes.""",
    )
    molecular_weight: Optional[float] = Field(
        default=None,
        description="""The molecular weight of the enzyme in the
        specified units.""",
    )
    molecular_weight_unit: Optional[MolecularWeightUnit] = Field(
        default=None,
        description="""The unit of measurement for the molecular weight
        (e.g., kDa, Da).""",
    )
    catalyzed_reaction: list[str] = Field(
        default_factory=list,
        description="""Description of the specific reaction or type of
        reaction catalyzed by this enzyme.""",
    )
    sequences: Optional[SequenceInfo] = Field(
        default=None,
        description="""Amino acid and/or DNA sequence information for
        the enzyme.""",
    )
    origin_organism: Optional[str] = Field(
        default=None,
        description="""The organism from which the enzyme was originally
        derived or isolated.""",
    )
    production_organism: Optional[str] = Field(
        default=None,
        description="""The organism used to produce the enzyme
        (may differ from origin organism for
        recombinant enzymes).""",
    )
    posttranslational_modification: list[str] = Field(
        default_factory=list,
        description="""Any post-translational modifications present on
        the enzyme that may affect its activity or
        properties.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:BiocatalystIdentity/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:BiocatalystIdentity",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "MolecularWeightUnit": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#MolecularWeightUnit/",
            "SequenceInfo": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SequenceInfo/",
            "name": "stbc:BiocatalystIdentity/name",
            "ec_number": {
                "@id": "stbc:BiocatalystIdentity/ec_number",
                "@container": "@list",
            },
            "molecular_weight": "stbc:BiocatalystIdentity/molecular_weight",
            "molecular_weight_unit": "stbc:BiocatalystIdentity/molecular_weight_unit",
            "catalyzed_reaction": {
                "@id": "stbc:BiocatalystIdentity/catalyzed_reaction",
                "@container": "@list",
            },
            "sequences": "stbc:BiocatalystIdentity/sequences",
            "origin_organism": "stbc:BiocatalystIdentity/origin_organism",
            "production_organism": "stbc:BiocatalystIdentity/production_organism",
            "posttranslational_modification": {
                "@id": "stbc:BiocatalystIdentity/posttranslational_modification",
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


class SequenceInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    sequence_amino_acid: list[str] = Field(
        default_factory=list,
        description="""The amino acid sequence of the enzyme in single-
        letter code format.""",
    )
    sequence_dna: list[str] = Field(
        default_factory=list,
        description="""The DNA sequence encoding the enzyme.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:SequenceInfo/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:SequenceInfo",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "sequence_amino_acid": {
                "@id": "stbc:SequenceInfo/sequence_amino_acid",
                "@container": "@list",
            },
            "sequence_dna": {
                "@id": "stbc:SequenceInfo/sequence_dna",
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


class BiocatalystSource(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    source_type: BiocatalystSourceType = Field(
        default=...,
        description="""Whether the biocatalyst was purchased from a
        supplier or produced in-house.""",
    )
    supplier: Optional[str] = Field(
        default=None,
        description="""Name of the commercial supplier or source of the
        biocatalyst.""",
    )
    purchased_details: Optional[PurchasedDetails] = Field(
        default=None,
        description="""Specific details relevant to commercially
        purchased biocatalysts.""",
    )
    self_produced_details: Optional[SelfProducedDetails] = Field(
        default=None,
        description="""Specific details relevant to biocatalysts produced
        in-house.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:BiocatalystSource/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:BiocatalystSource",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "BiocatalystSourceType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystSourceType/",
            "PurchasedDetails": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#PurchasedDetails/",
            "SelfProducedDetails": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#SelfProducedDetails/",
            "source_type": "stbc:BiocatalystSource/source_type",
            "supplier": "stbc:BiocatalystSource/supplier",
            "purchased_details": "stbc:BiocatalystSource/purchased_details",
            "self_produced_details": "stbc:BiocatalystSource/self_produced_details",
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


class PurchasedDetails(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    reference: Optional[str] = Field(
        default=None,
        description="""Product code, catalog number, or other reference
        identifier from the supplier.""",
    )
    purity: Optional[float] = Field(
        default=None,
        description="""Purity of the purchased biocatalyst as specified
        by the supplier, typically as a
        percentage.""",
    )
    purity_specification: Optional[str] = Field(
        default=None,
        description="""Method or specification used to determine the
        purity (e.g., SDS-PAGE, activity assay).""",
    )
    formulation: Optional[FormulationType] = Field(
        default=None,
        description="""Physical form of the purchased biocatalyst
        (dissolved, powder, etc.).""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:PurchasedDetails/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:PurchasedDetails",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "FormulationType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#FormulationType/",
            "reference": "stbc:PurchasedDetails/reference",
            "purity": "stbc:PurchasedDetails/purity",
            "purity_specification": "stbc:PurchasedDetails/purity_specification",
            "formulation": "stbc:PurchasedDetails/formulation",
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


class SelfProducedDetails(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    sequence_plasmid: list[str] = Field(
        default_factory=list,
        description="""Sequence of the plasmid used for enzyme
        expression.""",
    )
    plasmid_specifications: list[str] = Field(
        default_factory=list,
        description="""Details about the plasmid construction, including
        vector backbone, promoter, and other
        relevant features.""",
    )
    purification_method: list[str] = Field(
        default_factory=list,
        description="""Method(s) used to purify the enzyme after
        expression.""",
    )
    purity: Optional[float] = Field(
        default=None,
        description="""Achieved purity of the self-produced biocatalyst,
        typically as a percentage.""",
    )
    purity_specification: Optional[str] = Field(
        default=None,
        description="""Method used to determine the purity of the self-
        produced enzyme.""",
    )
    formulation: Optional[FormulationType] = Field(
        default=None,
        description="""Physical form of the self-produced biocatalyst
        after purification and processing.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:SelfProducedDetails/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:SelfProducedDetails",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "FormulationType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#FormulationType/",
            "sequence_plasmid": {
                "@id": "stbc:SelfProducedDetails/sequence_plasmid",
                "@container": "@list",
            },
            "plasmid_specifications": {
                "@id": "stbc:SelfProducedDetails/plasmid_specifications",
                "@container": "@list",
            },
            "purification_method": {
                "@id": "stbc:SelfProducedDetails/purification_method",
                "@container": "@list",
            },
            "purity": "stbc:SelfProducedDetails/purity",
            "purity_specification": "stbc:SelfProducedDetails/purity_specification",
            "formulation": "stbc:SelfProducedDetails/formulation",
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


class BiocatalystApplication(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    application_type: BiocatalystApplicationType = Field(
        default=...,
        description="""The form in which the biocatalyst is applied
        (purified enzyme, crude extract, whole
        cells, etc.).""",
    )
    concentration: list[Concentration] = Field(
        default_factory=list,
        description="""Concentration of the biocatalyst in the reaction
        mixture.""",
    )
    activity: list[Activity] = Field(
        default_factory=list,
        description="""Measured enzymatic activity of the biocatalyst
        under the reaction conditions.""",
    )
    workflow_details: Optional[ApplicationWorkflowDetails] = Field(
        default=None,
        description="""Specific workflow steps and methods used in
        applying the biocatalyst.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id",
        default_factory=lambda: "stbc:BiocatalystApplication/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:BiocatalystApplication",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "BiocatalystApplicationType": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#BiocatalystApplicationType/",
            "Concentration": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Concentration/",
            "Activity": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Activity/",
            "ApplicationWorkflowDetails": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#ApplicationWorkflowDetails/",
            "application_type": "stbc:BiocatalystApplication/application_type",
            "concentration": {
                "@id": "stbc:BiocatalystApplication/concentration",
                "@container": "@list",
            },
            "activity": {
                "@id": "stbc:BiocatalystApplication/activity",
                "@container": "@list",
            },
            "workflow_details": "stbc:BiocatalystApplication/workflow_details",
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

    def filter_concentration(self, **kwargs) -> list[Concentration]:
        """Filters the concentration attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Concentration]: The filtered list of Concentration objects
        """

        return FilterWrapper[Concentration](self.concentration, **kwargs).filter()

    def filter_activity(self, **kwargs) -> list[Activity]:
        """Filters the activity attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Activity]: The filtered list of Activity objects
        """

        return FilterWrapper[Activity](self.activity, **kwargs).filter()

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

    def add_to_concentration(
        self,
        value: Optional[float] = None,
        unit: Optional[str] = None,
        determination_method: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "value": value,
            "unit": unit,
            "determination_method": determination_method,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.concentration.append(Concentration(**params))

        return self.concentration[-1]

    def add_to_activity(
        self,
        value: Optional[float] = None,
        unit: Optional[str] = None,
        determination_method: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "value": value,
            "unit": unit,
            "determination_method": determination_method,
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.activity.append(Activity(**params))

        return self.activity[-1]


class Concentration(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    value: Optional[float] = Field(
        default=None,
        description="""Numerical value of the concentration.""",
    )
    unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the concentration (e.g.,
        mg/mL, µM, U/mL).""",
    )
    determination_method: Optional[str] = Field(
        default=None,
        description="""Method used to determine or calculate the
        concentration.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Concentration/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Concentration",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "value": "stbc:Concentration/value",
            "unit": "stbc:Concentration/unit",
            "determination_method": "stbc:Concentration/determination_method",
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


class Activity(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    value: Optional[float] = Field(
        default=None,
        description="""Numerical value of the measured activity.""",
    )
    unit: Optional[str] = Field(
        default=None,
        description="""Unit of measurement for the activity (e.g., U/mg,
        µmol/min/mg).""",
    )
    determination_method: Optional[str] = Field(
        default=None,
        description="""Assay method used to measure the enzymatic
        activity.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Activity/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Activity",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "value": "stbc:Activity/value",
            "unit": "stbc:Activity/unit",
            "determination_method": "stbc:Activity/determination_method",
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


class ApplicationWorkflowDetails(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    cell_disruption_process: Optional[str] = Field(
        default=None,
        description="""Method used to disrupt cells if working with whole
        cell preparations.""",
    )
    harvesting_method: Optional[str] = Field(
        default=None,
        description="""Method used to harvest cells or enzyme from the
        production system.""",
    )
    separation_method: Optional[str] = Field(
        default=None,
        description="""Method used to separate the biocatalyst from other
        components.""",
    )
    source_of_cellfree_extract: Optional[str] = Field(
        default=None,
        description="""Details about the source and preparation of cell-
        free extracts if applicable.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id",
        default_factory=lambda: "stbc:ApplicationWorkflowDetails/" + str(uuid4()),
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:ApplicationWorkflowDetails",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "cell_disruption_process": "stbc:ApplicationWorkflowDetails/cell_disruption_process",
            "harvesting_method": "stbc:ApplicationWorkflowDetails/harvesting_method",
            "separation_method": "stbc:ApplicationWorkflowDetails/separation_method",
            "source_of_cellfree_extract": "stbc:ApplicationWorkflowDetails/source_of_cellfree_extract",
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


class Immobilization(BaseModel):
    model_config: ConfigDict = ConfigDict(  # type: ignore
        validate_assignment=True,
        populate_by_name=True,
    )  # type: ignore

    immobilized: bool = Field(
        default=...,
        description="""Whether the biocatalyst is immobilized (true) or
        used in free form (false).""",
    )
    biocatalyst_state: Optional[str] = Field(
        default=None,
        description="""Physical state of the biocatalyst during
        immobilization (e.g., purified enzyme,
        crude extract).""",
    )
    immobilisation_chemistry: list[str] = Field(
        default_factory=list,
        description="""Chemical method or mechanism used for
        immobilization (e.g., covalent binding,
        adsorption, entrapment).""",
    )
    carrier_material: list[str] = Field(
        default_factory=list,
        description="""Material used as the solid support for
        immobilization.""",
    )
    linkers: list[str] = Field(
        default_factory=list,
        description="""Chemical linkers or spacers used between the
        enzyme and carrier material.""",
    )
    immobilisation_method: list[str] = Field(
        default_factory=list,
        description="""Detailed procedure used for the immobilization
        process.""",
    )
    purification_method: list[str] = Field(
        default_factory=list,
        description="""Method used to purify or wash the immobilized
        biocatalyst.""",
    )
    loading: Optional[Concentration] = Field(
        default=None,
        description="""Amount of enzyme loaded onto the carrier material.""",
    )
    notes: Optional[str] = Field(
        default=None,
        description="""Additional notes about the immobilization process
        or properties.""",
    )

    # JSON-LD fields
    ld_id: str = Field(
        alias="@id", default_factory=lambda: "stbc:Immobilization/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        alias="@type",
        default_factory=lambda: [
            "stbc:Immobilization",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        alias="@context",
        default_factory=lambda: {
            "@vocab": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "stbc": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#",
            "Concentration": "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis#Concentration/",
            "immobilized": "stbc:Immobilization/immobilized",
            "biocatalyst_state": "stbc:Immobilization/biocatalyst_state",
            "immobilisation_chemistry": {
                "@id": "stbc:Immobilization/immobilisation_chemistry",
                "@container": "@list",
            },
            "carrier_material": {
                "@id": "stbc:Immobilization/carrier_material",
                "@container": "@list",
            },
            "linkers": {
                "@id": "stbc:Immobilization/linkers",
                "@container": "@list",
            },
            "immobilisation_method": {
                "@id": "stbc:Immobilization/immobilisation_method",
                "@container": "@list",
            },
            "purification_method": {
                "@id": "stbc:Immobilization/purification_method",
                "@container": "@list",
            },
            "loading": "stbc:Immobilization/loading",
            "notes": "stbc:Immobilization/notes",
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


class BiocatalystSourceType(Enum):
    PURCHASED = "purchased"
    SELF_PRODUCED = "self_produced"


class BiocatalystApplicationType(Enum):
    CELL_FREE = "cell_free"
    CRUDE_CELL_EXTRACT = "crude_cell_extract"
    PURIFIED = "purified"
    SECRETED = "secreted"
    WHOLE_CELL = "whole_cell"


class MolecularWeightUnit(Enum):
    DA = "Da"
    KDA = "kDa"
    OTHER = "other"


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
