from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, ClassVar, Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    model_serializer,
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias=True,
        validate_by_name=True,
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )

    @model_serializer(mode="wrap", when_used="unless-none")
    def treat_empty_lists_as_none(
        self, handler: SerializerFunctionWrapHandler, info: SerializationInfo
    ) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not (field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)


class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key: str):
        return getattr(self.root, key)

    def __getitem__(self, key: str):
        return self.root[key]

    def __setitem__(self, key: str, value):
        self.root[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta(
    {
        "default_prefix": "oct_schema",
        "default_range": "string",
        "description": "Data standards for coral research and conservation",
        "id": "https://w3id.org/OpenCoralTools/oct-schema",
        "imports": [
            "linkml:types",
            "common",
            "Record",
            "InventoryRecord",
            "Organization",
            "Site",
            "Location",
            "Genet",
            "Coral",
            "Species",
            "Person",
            "Event",
            "registry/SpeciesRegisterEntry",
            "registry/OrganizationRegisterEntry",
        ],
        "license": "MIT",
        "name": "oct-schema",
        "prefixes": {
            "linkml": {
                "prefix_prefix": "linkml",
                "prefix_reference": "https://w3id.org/linkml/",
            },
            "oct_schema": {
                "prefix_prefix": "oct_schema",
                "prefix_reference": "https://w3id.org/OpenCoralTools/oct-schema/",
            },
            "schema": {
                "prefix_prefix": "schema",
                "prefix_reference": "http://schema.org/",
            },
        },
        "see_also": ["https://OpenCoralTools.github.io/oct-schema"],
        "source_file": "src/oct_schema/schema/oct_schema.yaml",
        "title": "oct-schema",
    }
)


class CoralSize(str, Enum):
    xs = "xs"
    s = "s"
    m = "m"
    l = "l"
    xl = "xl"


class ModelType(str, Enum):
    user = "user"
    organization = "organization"
    site = "site"
    group = "group"
    coral = "coral"
    genet = "genet"
    recordType = "recordType"
    event = "event"
    invitation = "invitation"
    unknown = "unknown"


class SiteType(str, Enum):
    site_type_nursery_ex_situ = "site_type_nursery_ex_situ"
    """
    Ex-Situ Nursery
    """
    site_type_nursery_in_situ = "site_type_nursery_in_situ"
    """
    In-Situ Nursery
    """
    site_type_outplanting = "site_type_outplanting"
    """
    Outplanting Site
    """
    site_type_gene_bank = "site_type_gene_bank"
    """
    Gene Bank
    """


class Record(ConfiguredBaseModel):
    """
    Base class for all records
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Record",
        }
    )

    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class InventoryRecord(Record):
    """
    Base class for inventory items that have URL paths
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "abstract": True,
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/InventoryRecord",
        }
    )

    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Organization(InventoryRecord):
    """
    Represents an organization
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Organization",
            "slot_usage": {
                "domain": {"name": "domain", "required": True},
                "name": {"name": "name", "required": True},
            },
        }
    )

    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    domain: str = Field(
        default=...,
        description="""Domain name associated with the organization""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Organization"]}},
    )
    siteTypeIds: Optional[list[str]] = Field(
        default=[],
        description="""List of site type IDs supported by the organization""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Organization"]}},
    )
    speciesIds: Optional[list[str]] = Field(
        default=[],
        description="""List of species IDs supported by the organization""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Organization"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Site(InventoryRecord):
    """
    Represents a physical site
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Site",
            "slot_usage": {
                "name": {"name": "name", "required": True},
                "siteTypeId": {"name": "siteTypeId", "required": True},
            },
        }
    )

    siteTypeId: str = Field(
        default=...,
        description="""ID of the site type""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site"]}},
    )
    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    groupIdHierarchy: Optional[list[str]] = Field(
        default=[],
        description="""Hierarchy of group IDs""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""Description of the entity""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site", "Location"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Location(InventoryRecord):
    """
    Represents a group of items or a container within a site
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Location",
            "slot_usage": {
                "groupTypeId": {"name": "groupTypeId", "required": True},
                "name": {"name": "name", "required": True},
                "parentId": {"name": "parentId", "required": True},
                "siteId": {"name": "siteId", "required": True},
            },
        }
    )

    groupTypeId: str = Field(
        default=...,
        description="""ID of the group type""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Location"]}},
    )
    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    siteId: str = Field(
        default=...,
        description="""ID of the site this entity belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Location", "Coral"]}},
    )
    parentId: str = Field(
        default=...,
        description="""ID of the parent entity""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Location"]}},
    )
    description: Optional[str] = Field(
        default=None,
        description="""Description of the entity""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Site", "Location"]}},
    )
    capacity: Optional[int] = Field(
        default=None,
        description="""Capacity of the group""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Location"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Genet(InventoryRecord):
    """
    Represents a genetic individual
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Genet",
            "slot_usage": {
                "genetTypeId": {"name": "genetTypeId", "required": True},
                "name": {"name": "name", "required": True},
                "sfId": {"name": "sfId", "required": True},
                "speciesId": {"name": "speciesId", "required": True},
            },
        }
    )

    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    speciesId: str = Field(
        default=...,
        description="""ID of the species""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet", "Coral"]}},
    )
    genetTypeId: str = Field(
        default=...,
        description="""ID of the genet type""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet"]}},
    )
    sfId: str = Field(
        default=...,
        description="""SeaFoundry ID""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet"]}},
    )
    clonalId: Optional[str] = Field(
        default=None,
        description="""Clonal ID if applicable""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet"]}},
    )
    accessionNumber: Optional[str] = Field(
        default=None,
        description="""Accession number if applicable""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Coral(InventoryRecord):
    """
    Represents a specific coral instance
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Coral",
            "slot_usage": {
                "coralTypeId": {"name": "coralTypeId", "required": True},
                "genetId": {"name": "genetId", "required": True},
                "groupId": {"name": "groupId", "required": True},
                "name": {"name": "name", "required": True},
                "quantity": {"name": "quantity", "required": True},
                "siteId": {"name": "siteId", "required": True},
                "speciesId": {"name": "speciesId", "required": True},
            },
        }
    )

    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    genetId: str = Field(
        default=...,
        description="""ID of the genet""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Coral"]}},
    )
    speciesId: str = Field(
        default=...,
        description="""ID of the species""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Genet", "Coral"]}},
    )
    siteId: str = Field(
        default=...,
        description="""ID of the site this entity belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Location", "Coral"]}},
    )
    groupId: str = Field(
        default=...,
        description="""ID of the group/location""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Coral"]}},
    )
    coralTypeId: str = Field(
        default=...,
        description="""ID of the coral type""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Coral"]}},
    )
    quantity: int = Field(
        default=...,
        description="""Quantity of items""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Coral"]}},
    )
    coral_size: Optional[CoralSize] = Field(
        default=None,
        description="""Size of the coral""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Coral"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Species(ConfiguredBaseModel):
    """
    Represents a species
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Species",
            "slot_usage": {
                "common_name": {"name": "common_name", "required": False},
                "genus": {"name": "genus", "required": True},
                "id": {"identifier": True, "name": "id"},
                "specific_epithet": {"name": "specific_epithet", "required": True},
            },
        }
    )

    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    common_name: Optional[str] = Field(
        default=None,
        description="""Common name of the species""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Species"]}},
    )
    genus: str = Field(
        default=...,
        description="""The genus name""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Species", "SpeciesRegisterEntry"]}
        },
    )
    specific_epithet: str = Field(
        default=...,
        description="""The specific name (second part of the binomial name)""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Species", "SpeciesRegisterEntry"]}
        },
    )


class Person(Record):
    """
    Represents a person (user)
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Person",
            "slot_usage": {
                "email": {"name": "email", "required": True},
                "name": {"name": "name", "required": True},
            },
        }
    )

    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    email: str = Field(
        default=...,
        description="""Email address of the user""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Person"]}},
    )
    imageUrl: Optional[str] = Field(
        default=None,
        description="""URL to the user's image""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Person"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class Event(InventoryRecord):
    """
    Represents an event in the system history
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/Event",
            "slot_usage": {
                "eventTypeId": {"name": "eventTypeId", "required": True},
                "recordId": {"name": "recordId", "required": True},
                "recordModelType": {"name": "recordModelType", "required": True},
            },
        }
    )

    eventTypeId: str = Field(
        default=...,
        description="""ID of the event type""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    recordId: str = Field(
        default=...,
        description="""ID of the record associated with the event""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    recordModelType: ModelType = Field(
        default=...,
        description="""Type of the record model""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Event"]}},
    )
    urlPath: Optional[str] = Field(
        default=None,
        description="""URL friendly path to this resource""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    internalPath: Optional[str] = Field(
        default=None,
        description="""Internal path structure""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    slug: Optional[str] = Field(
        default=None,
        description="""URL friendly identifier part""",
        json_schema_extra={"linkml_meta": {"domain_of": ["InventoryRecord"]}},
    )
    id: str = Field(
        default=...,
        description="""Unique identifier for the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record", "Species"]}},
    )
    createdAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was created""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    createdById: Optional[str] = Field(
        default=None,
        description="""ID of the user who created the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedAt: Optional[datetime] = Field(
        default=None,
        description="""Timestamp when the record was last updated""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    updatedById: Optional[str] = Field(
        default=None,
        description="""ID of the user who last updated the record""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )
    organizationId: Optional[str] = Field(
        default=None,
        description="""ID of the organization this record belongs to""",
        json_schema_extra={"linkml_meta": {"domain_of": ["Record"]}},
    )


class SpeciesRegisterEntry(ConfiguredBaseModel):
    """
    A canonical species record in the registry
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/registry/SpeciesRegisterEntry",
            "slot_usage": {
                "code": {"identifier": True, "name": "code", "required": True},
                "genus": {"name": "genus", "required": True},
                "specific_epithet": {"name": "specific_epithet", "required": True},
            },
        }
    )

    code: str = Field(
        default=...,
        description="""Unique 4-character species code (e.g. apal)""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )
    genus: str = Field(
        default=...,
        description="""The genus name""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Species", "SpeciesRegisterEntry"]}
        },
    )
    specific_epithet: str = Field(
        default=...,
        description="""The specific name (second part of the binomial name)""",
        json_schema_extra={
            "linkml_meta": {"domain_of": ["Species", "SpeciesRegisterEntry"]}
        },
    )
    scientific_name: Optional[str] = Field(
        default=None,
        description="""Full scientific name (genus + specific_epithet)""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )
    scientific_name_authorship: Optional[str] = Field(
        default=None,
        description="""Author and year of the species description""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )
    external_references: Optional[list[str]] = Field(
        default=[],
        description="""External identifiers (e.g. worms:12345)""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )
    synonyms: Optional[list[str]] = Field(
        default=[],
        description="""List of synonymous scientific names""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )
    deprecated_codes: Optional[list[str]] = Field(
        default=[],
        description="""Previous or deprecated codes for this species""",
        json_schema_extra={"linkml_meta": {"domain_of": ["SpeciesRegisterEntry"]}},
    )


class OrganizationRegisterEntry(ConfiguredBaseModel):
    """
    A canonical organization record in the registry
    """

    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta(
        {
            "from_schema": "https://w3id.org/OpenCoralTools/oct-schema/classes/registry/OrganizationRegisterEntry",
            "slot_usage": {
                "name": {"name": "name", "required": True},
                "org_id": {"identifier": True, "name": "org_id", "required": True},
            },
        }
    )

    org_id: str = Field(
        default=...,
        description="""Unique identifier for the organization""",
        json_schema_extra={"linkml_meta": {"domain_of": ["OrganizationRegisterEntry"]}},
    )
    name: str = Field(
        default=...,
        description="""Name of the entity""",
        json_schema_extra={
            "linkml_meta": {
                "domain_of": [
                    "Organization",
                    "Site",
                    "Location",
                    "Genet",
                    "Coral",
                    "Person",
                    "OrganizationRegisterEntry",
                ]
            }
        },
    )
    url: Optional[str] = Field(
        default=None,
        description="""Website URL of the organization""",
        json_schema_extra={"linkml_meta": {"domain_of": ["OrganizationRegisterEntry"]}},
    )
    country: Optional[str] = Field(
        default=None,
        description="""Country where the organization is based""",
        json_schema_extra={"linkml_meta": {"domain_of": ["OrganizationRegisterEntry"]}},
    )
    metadata: Optional[str] = Field(
        default=None,
        description="""Additional metadata as a JSON string or key-value pair""",
        json_schema_extra={"linkml_meta": {"domain_of": ["OrganizationRegisterEntry"]}},
    )


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Record.model_rebuild()
InventoryRecord.model_rebuild()
Organization.model_rebuild()
Site.model_rebuild()
Location.model_rebuild()
Genet.model_rebuild()
Coral.model_rebuild()
Species.model_rebuild()
Person.model_rebuild()
Event.model_rebuild()
SpeciesRegisterEntry.model_rebuild()
OrganizationRegisterEntry.model_rebuild()
