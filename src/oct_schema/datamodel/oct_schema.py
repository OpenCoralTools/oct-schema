# Auto generated from oct_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-06T15:25:21
# Schema: oct-schema
#
# id: https://w3id.org/OpenCoralTools/oct-schema
# description: Data standards for coral research and conservation
# license: MIT

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
OCT_SCHEMA = CurieNamespace("oct_schema", "https://w3id.org/OpenCoralTools/oct-schema/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
DEFAULT_ = OCT_SCHEMA


# Types


# Class references
class RecordId(URIorCURIE):
    pass


class InventoryRecordId(RecordId):
    pass


class OrganizationId(InventoryRecordId):
    pass


class SiteId(InventoryRecordId):
    pass


class LocationId(InventoryRecordId):
    pass


class GenetId(InventoryRecordId):
    pass


class CoralId(InventoryRecordId):
    pass


class SpeciesId(URIorCURIE):
    pass


class PersonId(RecordId):
    pass


class EventId(InventoryRecordId):
    pass


class SpeciesRegisterEntryCode(extended_str):
    pass


class OrganizationRegisterEntryOrgId(extended_str):
    pass


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    Base class for all records
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Record"]
    class_class_curie: ClassVar[str] = "oct_schema:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Record

    id: Union[str, RecordId] = None
    createdAt: Optional[Union[str, XSDDateTime]] = None
    createdById: Optional[str] = None
    updatedAt: Optional[Union[str, XSDDateTime]] = None
    updatedById: Optional[str] = None
    organizationId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordId):
            self.id = RecordId(self.id)

        if self.createdAt is not None and not isinstance(self.createdAt, XSDDateTime):
            self.createdAt = XSDDateTime(self.createdAt)

        if self.createdById is not None and not isinstance(self.createdById, str):
            self.createdById = str(self.createdById)

        if self.updatedAt is not None and not isinstance(self.updatedAt, XSDDateTime):
            self.updatedAt = XSDDateTime(self.updatedAt)

        if self.updatedById is not None and not isinstance(self.updatedById, str):
            self.updatedById = str(self.updatedById)

        if self.organizationId is not None and not isinstance(self.organizationId, str):
            self.organizationId = str(self.organizationId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InventoryRecord(Record):
    """
    Base class for inventory items that have URL paths
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["InventoryRecord"]
    class_class_curie: ClassVar[str] = "oct_schema:InventoryRecord"
    class_name: ClassVar[str] = "InventoryRecord"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.InventoryRecord

    id: Union[str, InventoryRecordId] = None
    urlPath: Optional[str] = None
    internalPath: Optional[str] = None
    slug: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.urlPath is not None and not isinstance(self.urlPath, str):
            self.urlPath = str(self.urlPath)

        if self.internalPath is not None and not isinstance(self.internalPath, str):
            self.internalPath = str(self.internalPath)

        if self.slug is not None and not isinstance(self.slug, str):
            self.slug = str(self.slug)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(InventoryRecord):
    """
    Represents an organization
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "oct_schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Organization

    id: Union[str, OrganizationId] = None
    name: str = None
    domain: str = None
    siteTypeIds: Optional[Union[str, list[str]]] = empty_list()
    speciesIds: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if not isinstance(self.siteTypeIds, list):
            self.siteTypeIds = (
                [self.siteTypeIds] if self.siteTypeIds is not None else []
            )
        self.siteTypeIds = [
            v if isinstance(v, str) else str(v) for v in self.siteTypeIds
        ]

        if not isinstance(self.speciesIds, list):
            self.speciesIds = [self.speciesIds] if self.speciesIds is not None else []
        self.speciesIds = [v if isinstance(v, str) else str(v) for v in self.speciesIds]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Site(InventoryRecord):
    """
    Represents a physical site
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Site"]
    class_class_curie: ClassVar[str] = "oct_schema:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Site

    id: Union[str, SiteId] = None
    siteTypeId: str = None
    name: str = None
    groupIdHierarchy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiteId):
            self.id = SiteId(self.id)

        if self._is_empty(self.siteTypeId):
            self.MissingRequiredField("siteTypeId")
        if not isinstance(self.siteTypeId, str):
            self.siteTypeId = str(self.siteTypeId)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.groupIdHierarchy, list):
            self.groupIdHierarchy = (
                [self.groupIdHierarchy] if self.groupIdHierarchy is not None else []
            )
        self.groupIdHierarchy = [
            v if isinstance(v, str) else str(v) for v in self.groupIdHierarchy
        ]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(InventoryRecord):
    """
    Represents a group of items or a container within a site
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Location"]
    class_class_curie: ClassVar[str] = "oct_schema:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Location

    id: Union[str, LocationId] = None
    groupTypeId: str = None
    name: str = None
    siteId: str = None
    parentId: str = None
    description: Optional[str] = None
    capacity: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationId):
            self.id = LocationId(self.id)

        if self._is_empty(self.groupTypeId):
            self.MissingRequiredField("groupTypeId")
        if not isinstance(self.groupTypeId, str):
            self.groupTypeId = str(self.groupTypeId)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.siteId):
            self.MissingRequiredField("siteId")
        if not isinstance(self.siteId, str):
            self.siteId = str(self.siteId)

        if self._is_empty(self.parentId):
            self.MissingRequiredField("parentId")
        if not isinstance(self.parentId, str):
            self.parentId = str(self.parentId)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.capacity is not None and not isinstance(self.capacity, int):
            self.capacity = int(self.capacity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Genet(InventoryRecord):
    """
    Represents a genetic individual
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Genet"]
    class_class_curie: ClassVar[str] = "oct_schema:Genet"
    class_name: ClassVar[str] = "Genet"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Genet

    id: Union[str, GenetId] = None
    name: str = None
    speciesId: str = None
    genetTypeId: str = None
    sfId: str = None
    clonalId: Optional[str] = None
    accessionNumber: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenetId):
            self.id = GenetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.speciesId):
            self.MissingRequiredField("speciesId")
        if not isinstance(self.speciesId, str):
            self.speciesId = str(self.speciesId)

        if self._is_empty(self.genetTypeId):
            self.MissingRequiredField("genetTypeId")
        if not isinstance(self.genetTypeId, str):
            self.genetTypeId = str(self.genetTypeId)

        if self._is_empty(self.sfId):
            self.MissingRequiredField("sfId")
        if not isinstance(self.sfId, str):
            self.sfId = str(self.sfId)

        if self.clonalId is not None and not isinstance(self.clonalId, str):
            self.clonalId = str(self.clonalId)

        if self.accessionNumber is not None and not isinstance(
            self.accessionNumber, str
        ):
            self.accessionNumber = str(self.accessionNumber)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coral(InventoryRecord):
    """
    Represents a specific coral instance
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Coral"]
    class_class_curie: ClassVar[str] = "oct_schema:Coral"
    class_name: ClassVar[str] = "Coral"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Coral

    id: Union[str, CoralId] = None
    name: str = None
    genetId: str = None
    speciesId: str = None
    siteId: str = None
    groupId: str = None
    coralTypeId: str = None
    quantity: int = None
    coral_size: Optional[Union[str, "CoralSize"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CoralId):
            self.id = CoralId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.genetId):
            self.MissingRequiredField("genetId")
        if not isinstance(self.genetId, str):
            self.genetId = str(self.genetId)

        if self._is_empty(self.speciesId):
            self.MissingRequiredField("speciesId")
        if not isinstance(self.speciesId, str):
            self.speciesId = str(self.speciesId)

        if self._is_empty(self.siteId):
            self.MissingRequiredField("siteId")
        if not isinstance(self.siteId, str):
            self.siteId = str(self.siteId)

        if self._is_empty(self.groupId):
            self.MissingRequiredField("groupId")
        if not isinstance(self.groupId, str):
            self.groupId = str(self.groupId)

        if self._is_empty(self.coralTypeId):
            self.MissingRequiredField("coralTypeId")
        if not isinstance(self.coralTypeId, str):
            self.coralTypeId = str(self.coralTypeId)

        if self._is_empty(self.quantity):
            self.MissingRequiredField("quantity")
        if not isinstance(self.quantity, int):
            self.quantity = int(self.quantity)

        if self.coral_size is not None and not isinstance(self.coral_size, CoralSize):
            self.coral_size = CoralSize(self.coral_size)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Species(YAMLRoot):
    """
    Represents a species
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Species"]
    class_class_curie: ClassVar[str] = "oct_schema:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Species

    id: Union[str, SpeciesId] = None
    genus: str = None
    specific_epithet: str = None
    common_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesId):
            self.id = SpeciesId(self.id)

        if self._is_empty(self.genus):
            self.MissingRequiredField("genus")
        if not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self._is_empty(self.specific_epithet):
            self.MissingRequiredField("specific_epithet")
        if not isinstance(self.specific_epithet, str):
            self.specific_epithet = str(self.specific_epithet)

        if self.common_name is not None and not isinstance(self.common_name, str):
            self.common_name = str(self.common_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(Record):
    """
    Represents a person (user)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "oct_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Person

    id: Union[str, PersonId] = None
    name: str = None
    email: str = None
    imageUrl: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self.imageUrl is not None and not isinstance(self.imageUrl, str):
            self.imageUrl = str(self.imageUrl)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(InventoryRecord):
    """
    Represents an event in the system history
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["Event"]
    class_class_curie: ClassVar[str] = "oct_schema:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.Event

    id: Union[str, EventId] = None
    eventTypeId: str = None
    recordId: str = None
    recordModelType: Union[str, "ModelType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self._is_empty(self.eventTypeId):
            self.MissingRequiredField("eventTypeId")
        if not isinstance(self.eventTypeId, str):
            self.eventTypeId = str(self.eventTypeId)

        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, str):
            self.recordId = str(self.recordId)

        if self._is_empty(self.recordModelType):
            self.MissingRequiredField("recordModelType")
        if not isinstance(self.recordModelType, ModelType):
            self.recordModelType = ModelType(self.recordModelType)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpeciesRegisterEntry(YAMLRoot):
    """
    A canonical species record in the registry
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["SpeciesRegisterEntry"]
    class_class_curie: ClassVar[str] = "oct_schema:SpeciesRegisterEntry"
    class_name: ClassVar[str] = "SpeciesRegisterEntry"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.SpeciesRegisterEntry

    code: Union[str, SpeciesRegisterEntryCode] = None
    genus: str = None
    specific_epithet: str = None
    scientific_name: Optional[str] = None
    scientific_name_authorship: Optional[str] = None
    external_references: Optional[Union[str, list[str]]] = empty_list()
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    deprecated_codes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, SpeciesRegisterEntryCode):
            self.code = SpeciesRegisterEntryCode(self.code)

        if self._is_empty(self.genus):
            self.MissingRequiredField("genus")
        if not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self._is_empty(self.specific_epithet):
            self.MissingRequiredField("specific_epithet")
        if not isinstance(self.specific_epithet, str):
            self.specific_epithet = str(self.specific_epithet)

        if self.scientific_name is not None and not isinstance(
            self.scientific_name, str
        ):
            self.scientific_name = str(self.scientific_name)

        if self.scientific_name_authorship is not None and not isinstance(
            self.scientific_name_authorship, str
        ):
            self.scientific_name_authorship = str(self.scientific_name_authorship)

        if not isinstance(self.external_references, list):
            self.external_references = (
                [self.external_references]
                if self.external_references is not None
                else []
            )
        self.external_references = [
            v if isinstance(v, str) else str(v) for v in self.external_references
        ]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.deprecated_codes, list):
            self.deprecated_codes = (
                [self.deprecated_codes] if self.deprecated_codes is not None else []
            )
        self.deprecated_codes = [
            v if isinstance(v, str) else str(v) for v in self.deprecated_codes
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganizationRegisterEntry(YAMLRoot):
    """
    A canonical organization record in the registry
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["OrganizationRegisterEntry"]
    class_class_curie: ClassVar[str] = "oct_schema:OrganizationRegisterEntry"
    class_name: ClassVar[str] = "OrganizationRegisterEntry"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.OrganizationRegisterEntry

    org_id: Union[str, OrganizationRegisterEntryOrgId] = None
    name: str = None
    url: Optional[str] = None
    country: Optional[str] = None
    metadata: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.org_id):
            self.MissingRequiredField("org_id")
        if not isinstance(self.org_id, OrganizationRegisterEntryOrgId):
            self.org_id = OrganizationRegisterEntryOrgId(self.org_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        super().__post_init__(**kwargs)


# Enumerations
class CoralSize(EnumDefinitionImpl):
    xs = PermissibleValue(text="xs")
    s = PermissibleValue(text="s")
    m = PermissibleValue(text="m")
    l = PermissibleValue(text="l")
    xl = PermissibleValue(text="xl")

    _defn = EnumDefinition(
        name="CoralSize",
    )


class ModelType(EnumDefinitionImpl):
    user = PermissibleValue(text="user")
    organization = PermissibleValue(text="organization")
    site = PermissibleValue(text="site")
    group = PermissibleValue(text="group")
    coral = PermissibleValue(text="coral")
    genet = PermissibleValue(text="genet")
    recordType = PermissibleValue(text="recordType")
    event = PermissibleValue(text="event")
    invitation = PermissibleValue(text="invitation")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="ModelType",
    )


class SiteType(EnumDefinitionImpl):
    site_type_nursery_ex_situ = PermissibleValue(
        text="site_type_nursery_ex_situ", description="Ex-Situ Nursery"
    )
    site_type_nursery_in_situ = PermissibleValue(
        text="site_type_nursery_in_situ", description="In-Situ Nursery"
    )
    site_type_outplanting = PermissibleValue(
        text="site_type_outplanting", description="Outplanting Site"
    )
    site_type_gene_bank = PermissibleValue(
        text="site_type_gene_bank", description="Gene Bank"
    )

    _defn = EnumDefinition(
        name="SiteType",
    )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=OCT_SCHEMA.id,
    name="id",
    curie=OCT_SCHEMA.curie("id"),
    model_uri=OCT_SCHEMA.id,
    domain=None,
    range=URIRef,
)

slots.createdAt = Slot(
    uri=OCT_SCHEMA.createdAt,
    name="createdAt",
    curie=OCT_SCHEMA.curie("createdAt"),
    model_uri=OCT_SCHEMA.createdAt,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.createdById = Slot(
    uri=OCT_SCHEMA.createdById,
    name="createdById",
    curie=OCT_SCHEMA.curie("createdById"),
    model_uri=OCT_SCHEMA.createdById,
    domain=None,
    range=Optional[str],
)

slots.updatedAt = Slot(
    uri=OCT_SCHEMA.updatedAt,
    name="updatedAt",
    curie=OCT_SCHEMA.curie("updatedAt"),
    model_uri=OCT_SCHEMA.updatedAt,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.updatedById = Slot(
    uri=OCT_SCHEMA.updatedById,
    name="updatedById",
    curie=OCT_SCHEMA.curie("updatedById"),
    model_uri=OCT_SCHEMA.updatedById,
    domain=None,
    range=Optional[str],
)

slots.organizationId = Slot(
    uri=OCT_SCHEMA.organizationId,
    name="organizationId",
    curie=OCT_SCHEMA.curie("organizationId"),
    model_uri=OCT_SCHEMA.organizationId,
    domain=None,
    range=Optional[str],
)

slots.urlPath = Slot(
    uri=OCT_SCHEMA.urlPath,
    name="urlPath",
    curie=OCT_SCHEMA.curie("urlPath"),
    model_uri=OCT_SCHEMA.urlPath,
    domain=None,
    range=Optional[str],
)

slots.internalPath = Slot(
    uri=OCT_SCHEMA.internalPath,
    name="internalPath",
    curie=OCT_SCHEMA.curie("internalPath"),
    model_uri=OCT_SCHEMA.internalPath,
    domain=None,
    range=Optional[str],
)

slots.slug = Slot(
    uri=OCT_SCHEMA.slug,
    name="slug",
    curie=OCT_SCHEMA.curie("slug"),
    model_uri=OCT_SCHEMA.slug,
    domain=None,
    range=Optional[str],
)

slots.name = Slot(
    uri=OCT_SCHEMA.name,
    name="name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.name,
    domain=None,
    range=Optional[str],
)

slots.description = Slot(
    uri=OCT_SCHEMA.description,
    name="description",
    curie=OCT_SCHEMA.curie("description"),
    model_uri=OCT_SCHEMA.description,
    domain=None,
    range=Optional[str],
)

slots.genus = Slot(
    uri=OCT_SCHEMA.genus,
    name="genus",
    curie=OCT_SCHEMA.curie("genus"),
    model_uri=OCT_SCHEMA.genus,
    domain=None,
    range=Optional[str],
)

slots.specific_epithet = Slot(
    uri=OCT_SCHEMA.specific_epithet,
    name="specific_epithet",
    curie=OCT_SCHEMA.curie("specific_epithet"),
    model_uri=OCT_SCHEMA.specific_epithet,
    domain=None,
    range=Optional[str],
)

slots.common_name = Slot(
    uri=OCT_SCHEMA.common_name,
    name="common_name",
    curie=OCT_SCHEMA.curie("common_name"),
    model_uri=OCT_SCHEMA.common_name,
    domain=None,
    range=Optional[str],
)

slots.domain = Slot(
    uri=OCT_SCHEMA.domain,
    name="domain",
    curie=OCT_SCHEMA.curie("domain"),
    model_uri=OCT_SCHEMA.domain,
    domain=None,
    range=Optional[str],
)

slots.siteTypeIds = Slot(
    uri=OCT_SCHEMA.siteTypeIds,
    name="siteTypeIds",
    curie=OCT_SCHEMA.curie("siteTypeIds"),
    model_uri=OCT_SCHEMA.siteTypeIds,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.speciesIds = Slot(
    uri=OCT_SCHEMA.speciesIds,
    name="speciesIds",
    curie=OCT_SCHEMA.curie("speciesIds"),
    model_uri=OCT_SCHEMA.speciesIds,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.siteTypeId = Slot(
    uri=OCT_SCHEMA.siteTypeId,
    name="siteTypeId",
    curie=OCT_SCHEMA.curie("siteTypeId"),
    model_uri=OCT_SCHEMA.siteTypeId,
    domain=None,
    range=Optional[str],
)

slots.groupIdHierarchy = Slot(
    uri=OCT_SCHEMA.groupIdHierarchy,
    name="groupIdHierarchy",
    curie=OCT_SCHEMA.curie("groupIdHierarchy"),
    model_uri=OCT_SCHEMA.groupIdHierarchy,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.groupTypeId = Slot(
    uri=OCT_SCHEMA.groupTypeId,
    name="groupTypeId",
    curie=OCT_SCHEMA.curie("groupTypeId"),
    model_uri=OCT_SCHEMA.groupTypeId,
    domain=None,
    range=Optional[str],
)

slots.siteId = Slot(
    uri=OCT_SCHEMA.siteId,
    name="siteId",
    curie=OCT_SCHEMA.curie("siteId"),
    model_uri=OCT_SCHEMA.siteId,
    domain=None,
    range=Optional[str],
)

slots.parentId = Slot(
    uri=OCT_SCHEMA.parentId,
    name="parentId",
    curie=OCT_SCHEMA.curie("parentId"),
    model_uri=OCT_SCHEMA.parentId,
    domain=None,
    range=Optional[str],
)

slots.capacity = Slot(
    uri=OCT_SCHEMA.capacity,
    name="capacity",
    curie=OCT_SCHEMA.curie("capacity"),
    model_uri=OCT_SCHEMA.capacity,
    domain=None,
    range=Optional[int],
)

slots.genetTypeId = Slot(
    uri=OCT_SCHEMA.genetTypeId,
    name="genetTypeId",
    curie=OCT_SCHEMA.curie("genetTypeId"),
    model_uri=OCT_SCHEMA.genetTypeId,
    domain=None,
    range=Optional[str],
)

slots.sfId = Slot(
    uri=OCT_SCHEMA.sfId,
    name="sfId",
    curie=OCT_SCHEMA.curie("sfId"),
    model_uri=OCT_SCHEMA.sfId,
    domain=None,
    range=Optional[str],
)

slots.clonalId = Slot(
    uri=OCT_SCHEMA.clonalId,
    name="clonalId",
    curie=OCT_SCHEMA.curie("clonalId"),
    model_uri=OCT_SCHEMA.clonalId,
    domain=None,
    range=Optional[str],
)

slots.accessionNumber = Slot(
    uri=OCT_SCHEMA.accessionNumber,
    name="accessionNumber",
    curie=OCT_SCHEMA.curie("accessionNumber"),
    model_uri=OCT_SCHEMA.accessionNumber,
    domain=None,
    range=Optional[str],
)

slots.genetId = Slot(
    uri=OCT_SCHEMA.genetId,
    name="genetId",
    curie=OCT_SCHEMA.curie("genetId"),
    model_uri=OCT_SCHEMA.genetId,
    domain=None,
    range=Optional[str],
)

slots.speciesId = Slot(
    uri=OCT_SCHEMA.speciesId,
    name="speciesId",
    curie=OCT_SCHEMA.curie("speciesId"),
    model_uri=OCT_SCHEMA.speciesId,
    domain=None,
    range=Optional[str],
)

slots.groupId = Slot(
    uri=OCT_SCHEMA.groupId,
    name="groupId",
    curie=OCT_SCHEMA.curie("groupId"),
    model_uri=OCT_SCHEMA.groupId,
    domain=None,
    range=Optional[str],
)

slots.coralTypeId = Slot(
    uri=OCT_SCHEMA.coralTypeId,
    name="coralTypeId",
    curie=OCT_SCHEMA.curie("coralTypeId"),
    model_uri=OCT_SCHEMA.coralTypeId,
    domain=None,
    range=Optional[str],
)

slots.quantity = Slot(
    uri=OCT_SCHEMA.quantity,
    name="quantity",
    curie=OCT_SCHEMA.curie("quantity"),
    model_uri=OCT_SCHEMA.quantity,
    domain=None,
    range=Optional[int],
)

slots.coral_size = Slot(
    uri=OCT_SCHEMA.coral_size,
    name="coral_size",
    curie=OCT_SCHEMA.curie("coral_size"),
    model_uri=OCT_SCHEMA.coral_size,
    domain=None,
    range=Optional[Union[str, "CoralSize"]],
)

slots.email = Slot(
    uri=OCT_SCHEMA.email,
    name="email",
    curie=OCT_SCHEMA.curie("email"),
    model_uri=OCT_SCHEMA.email,
    domain=None,
    range=Optional[str],
)

slots.imageUrl = Slot(
    uri=OCT_SCHEMA.imageUrl,
    name="imageUrl",
    curie=OCT_SCHEMA.curie("imageUrl"),
    model_uri=OCT_SCHEMA.imageUrl,
    domain=None,
    range=Optional[str],
)

slots.eventTypeId = Slot(
    uri=OCT_SCHEMA.eventTypeId,
    name="eventTypeId",
    curie=OCT_SCHEMA.curie("eventTypeId"),
    model_uri=OCT_SCHEMA.eventTypeId,
    domain=None,
    range=Optional[str],
)

slots.recordId = Slot(
    uri=OCT_SCHEMA.recordId,
    name="recordId",
    curie=OCT_SCHEMA.curie("recordId"),
    model_uri=OCT_SCHEMA.recordId,
    domain=None,
    range=Optional[str],
)

slots.recordModelType = Slot(
    uri=OCT_SCHEMA.recordModelType,
    name="recordModelType",
    curie=OCT_SCHEMA.curie("recordModelType"),
    model_uri=OCT_SCHEMA.recordModelType,
    domain=None,
    range=Optional[Union[str, "ModelType"]],
)

slots.code = Slot(
    uri=OCT_SCHEMA.code,
    name="code",
    curie=OCT_SCHEMA.curie("code"),
    model_uri=OCT_SCHEMA.code,
    domain=None,
    range=Optional[str],
)

slots.scientific_name = Slot(
    uri=OCT_SCHEMA.scientific_name,
    name="scientific_name",
    curie=OCT_SCHEMA.curie("scientific_name"),
    model_uri=OCT_SCHEMA.scientific_name,
    domain=None,
    range=Optional[str],
)

slots.scientific_name_authorship = Slot(
    uri=OCT_SCHEMA.scientific_name_authorship,
    name="scientific_name_authorship",
    curie=OCT_SCHEMA.curie("scientific_name_authorship"),
    model_uri=OCT_SCHEMA.scientific_name_authorship,
    domain=None,
    range=Optional[str],
)

slots.external_references = Slot(
    uri=OCT_SCHEMA.external_references,
    name="external_references",
    curie=OCT_SCHEMA.curie("external_references"),
    model_uri=OCT_SCHEMA.external_references,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.synonyms = Slot(
    uri=OCT_SCHEMA.synonyms,
    name="synonyms",
    curie=OCT_SCHEMA.curie("synonyms"),
    model_uri=OCT_SCHEMA.synonyms,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.deprecated_codes = Slot(
    uri=OCT_SCHEMA.deprecated_codes,
    name="deprecated_codes",
    curie=OCT_SCHEMA.curie("deprecated_codes"),
    model_uri=OCT_SCHEMA.deprecated_codes,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.org_id = Slot(
    uri=OCT_SCHEMA.org_id,
    name="org_id",
    curie=OCT_SCHEMA.curie("org_id"),
    model_uri=OCT_SCHEMA.org_id,
    domain=None,
    range=Optional[str],
)

slots.url = Slot(
    uri=OCT_SCHEMA.url,
    name="url",
    curie=OCT_SCHEMA.curie("url"),
    model_uri=OCT_SCHEMA.url,
    domain=None,
    range=Optional[str],
)

slots.country = Slot(
    uri=OCT_SCHEMA.country,
    name="country",
    curie=OCT_SCHEMA.curie("country"),
    model_uri=OCT_SCHEMA.country,
    domain=None,
    range=Optional[str],
)

slots.metadata = Slot(
    uri=OCT_SCHEMA.metadata,
    name="metadata",
    curie=OCT_SCHEMA.curie("metadata"),
    model_uri=OCT_SCHEMA.metadata,
    domain=None,
    range=Optional[str],
)

slots.Organization_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Organization_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Organization_name,
    domain=Organization,
    range=str,
)

slots.Organization_domain = Slot(
    uri=OCT_SCHEMA.domain,
    name="Organization_domain",
    curie=OCT_SCHEMA.curie("domain"),
    model_uri=OCT_SCHEMA.Organization_domain,
    domain=Organization,
    range=str,
)

slots.Site_siteTypeId = Slot(
    uri=OCT_SCHEMA.siteTypeId,
    name="Site_siteTypeId",
    curie=OCT_SCHEMA.curie("siteTypeId"),
    model_uri=OCT_SCHEMA.Site_siteTypeId,
    domain=Site,
    range=str,
)

slots.Site_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Site_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Site_name,
    domain=Site,
    range=str,
)

slots.Location_groupTypeId = Slot(
    uri=OCT_SCHEMA.groupTypeId,
    name="Location_groupTypeId",
    curie=OCT_SCHEMA.curie("groupTypeId"),
    model_uri=OCT_SCHEMA.Location_groupTypeId,
    domain=Location,
    range=str,
)

slots.Location_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Location_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Location_name,
    domain=Location,
    range=str,
)

slots.Location_siteId = Slot(
    uri=OCT_SCHEMA.siteId,
    name="Location_siteId",
    curie=OCT_SCHEMA.curie("siteId"),
    model_uri=OCT_SCHEMA.Location_siteId,
    domain=Location,
    range=str,
)

slots.Location_parentId = Slot(
    uri=OCT_SCHEMA.parentId,
    name="Location_parentId",
    curie=OCT_SCHEMA.curie("parentId"),
    model_uri=OCT_SCHEMA.Location_parentId,
    domain=Location,
    range=str,
)

slots.Genet_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Genet_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Genet_name,
    domain=Genet,
    range=str,
)

slots.Genet_speciesId = Slot(
    uri=OCT_SCHEMA.speciesId,
    name="Genet_speciesId",
    curie=OCT_SCHEMA.curie("speciesId"),
    model_uri=OCT_SCHEMA.Genet_speciesId,
    domain=Genet,
    range=str,
)

slots.Genet_genetTypeId = Slot(
    uri=OCT_SCHEMA.genetTypeId,
    name="Genet_genetTypeId",
    curie=OCT_SCHEMA.curie("genetTypeId"),
    model_uri=OCT_SCHEMA.Genet_genetTypeId,
    domain=Genet,
    range=str,
)

slots.Genet_sfId = Slot(
    uri=OCT_SCHEMA.sfId,
    name="Genet_sfId",
    curie=OCT_SCHEMA.curie("sfId"),
    model_uri=OCT_SCHEMA.Genet_sfId,
    domain=Genet,
    range=str,
)

slots.Coral_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Coral_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Coral_name,
    domain=Coral,
    range=str,
)

slots.Coral_genetId = Slot(
    uri=OCT_SCHEMA.genetId,
    name="Coral_genetId",
    curie=OCT_SCHEMA.curie("genetId"),
    model_uri=OCT_SCHEMA.Coral_genetId,
    domain=Coral,
    range=str,
)

slots.Coral_speciesId = Slot(
    uri=OCT_SCHEMA.speciesId,
    name="Coral_speciesId",
    curie=OCT_SCHEMA.curie("speciesId"),
    model_uri=OCT_SCHEMA.Coral_speciesId,
    domain=Coral,
    range=str,
)

slots.Coral_siteId = Slot(
    uri=OCT_SCHEMA.siteId,
    name="Coral_siteId",
    curie=OCT_SCHEMA.curie("siteId"),
    model_uri=OCT_SCHEMA.Coral_siteId,
    domain=Coral,
    range=str,
)

slots.Coral_groupId = Slot(
    uri=OCT_SCHEMA.groupId,
    name="Coral_groupId",
    curie=OCT_SCHEMA.curie("groupId"),
    model_uri=OCT_SCHEMA.Coral_groupId,
    domain=Coral,
    range=str,
)

slots.Coral_coralTypeId = Slot(
    uri=OCT_SCHEMA.coralTypeId,
    name="Coral_coralTypeId",
    curie=OCT_SCHEMA.curie("coralTypeId"),
    model_uri=OCT_SCHEMA.Coral_coralTypeId,
    domain=Coral,
    range=str,
)

slots.Coral_quantity = Slot(
    uri=OCT_SCHEMA.quantity,
    name="Coral_quantity",
    curie=OCT_SCHEMA.curie("quantity"),
    model_uri=OCT_SCHEMA.Coral_quantity,
    domain=Coral,
    range=int,
)

slots.Species_id = Slot(
    uri=OCT_SCHEMA.id,
    name="Species_id",
    curie=OCT_SCHEMA.curie("id"),
    model_uri=OCT_SCHEMA.Species_id,
    domain=Species,
    range=Union[str, SpeciesId],
)

slots.Species_common_name = Slot(
    uri=OCT_SCHEMA.common_name,
    name="Species_common_name",
    curie=OCT_SCHEMA.curie("common_name"),
    model_uri=OCT_SCHEMA.Species_common_name,
    domain=Species,
    range=Optional[str],
)

slots.Species_genus = Slot(
    uri=OCT_SCHEMA.genus,
    name="Species_genus",
    curie=OCT_SCHEMA.curie("genus"),
    model_uri=OCT_SCHEMA.Species_genus,
    domain=Species,
    range=str,
)

slots.Species_specific_epithet = Slot(
    uri=OCT_SCHEMA.specific_epithet,
    name="Species_specific_epithet",
    curie=OCT_SCHEMA.curie("specific_epithet"),
    model_uri=OCT_SCHEMA.Species_specific_epithet,
    domain=Species,
    range=str,
)

slots.Person_name = Slot(
    uri=OCT_SCHEMA.name,
    name="Person_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.Person_name,
    domain=Person,
    range=str,
)

slots.Person_email = Slot(
    uri=OCT_SCHEMA.email,
    name="Person_email",
    curie=OCT_SCHEMA.curie("email"),
    model_uri=OCT_SCHEMA.Person_email,
    domain=Person,
    range=str,
)

slots.Event_eventTypeId = Slot(
    uri=OCT_SCHEMA.eventTypeId,
    name="Event_eventTypeId",
    curie=OCT_SCHEMA.curie("eventTypeId"),
    model_uri=OCT_SCHEMA.Event_eventTypeId,
    domain=Event,
    range=str,
)

slots.Event_recordId = Slot(
    uri=OCT_SCHEMA.recordId,
    name="Event_recordId",
    curie=OCT_SCHEMA.curie("recordId"),
    model_uri=OCT_SCHEMA.Event_recordId,
    domain=Event,
    range=str,
)

slots.Event_recordModelType = Slot(
    uri=OCT_SCHEMA.recordModelType,
    name="Event_recordModelType",
    curie=OCT_SCHEMA.curie("recordModelType"),
    model_uri=OCT_SCHEMA.Event_recordModelType,
    domain=Event,
    range=Union[str, "ModelType"],
)

slots.SpeciesRegisterEntry_code = Slot(
    uri=OCT_SCHEMA.code,
    name="SpeciesRegisterEntry_code",
    curie=OCT_SCHEMA.curie("code"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_code,
    domain=SpeciesRegisterEntry,
    range=Union[str, SpeciesRegisterEntryCode],
)

slots.SpeciesRegisterEntry_genus = Slot(
    uri=OCT_SCHEMA.genus,
    name="SpeciesRegisterEntry_genus",
    curie=OCT_SCHEMA.curie("genus"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_genus,
    domain=SpeciesRegisterEntry,
    range=str,
)

slots.SpeciesRegisterEntry_specific_epithet = Slot(
    uri=OCT_SCHEMA.specific_epithet,
    name="SpeciesRegisterEntry_specific_epithet",
    curie=OCT_SCHEMA.curie("specific_epithet"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_specific_epithet,
    domain=SpeciesRegisterEntry,
    range=str,
)

slots.OrganizationRegisterEntry_org_id = Slot(
    uri=OCT_SCHEMA.org_id,
    name="OrganizationRegisterEntry_org_id",
    curie=OCT_SCHEMA.curie("org_id"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_org_id,
    domain=OrganizationRegisterEntry,
    range=Union[str, OrganizationRegisterEntryOrgId],
)

slots.OrganizationRegisterEntry_name = Slot(
    uri=OCT_SCHEMA.name,
    name="OrganizationRegisterEntry_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_name,
    domain=OrganizationRegisterEntry,
    range=str,
)
