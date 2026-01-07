# Auto generated from oct_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-06T17:57:47
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
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

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


class SpeciesRegisterEntryId(URIorCURIE):
    pass


class OrganizationRegisterEntryId(URIorCURIE):
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
    created_at: Optional[Union[str, XSDDateTime]] = None
    created_by_id: Optional[str] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    updated_by_id: Optional[str] = None
    organization_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordId):
            self.id = RecordId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.created_by_id is not None and not isinstance(self.created_by_id, str):
            self.created_by_id = str(self.created_by_id)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.updated_by_id is not None and not isinstance(self.updated_by_id, str):
            self.updated_by_id = str(self.updated_by_id)

        if self.organization_id is not None and not isinstance(
            self.organization_id, str
        ):
            self.organization_id = str(self.organization_id)

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
    url_path: Optional[str] = None
    internal_path: Optional[str] = None
    slug: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.url_path is not None and not isinstance(self.url_path, str):
            self.url_path = str(self.url_path)

        if self.internal_path is not None and not isinstance(self.internal_path, str):
            self.internal_path = str(self.internal_path)

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
    site_type_ids: Optional[Union[str, list[str]]] = empty_list()
    species_ids: Optional[Union[str, list[str]]] = empty_list()

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

        if not isinstance(self.site_type_ids, list):
            self.site_type_ids = (
                [self.site_type_ids] if self.site_type_ids is not None else []
            )
        self.site_type_ids = [
            v if isinstance(v, str) else str(v) for v in self.site_type_ids
        ]

        if not isinstance(self.species_ids, list):
            self.species_ids = (
                [self.species_ids] if self.species_ids is not None else []
            )
        self.species_ids = [
            v if isinstance(v, str) else str(v) for v in self.species_ids
        ]

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
    site_type_id: str = None
    name: str = None
    group_id_hierarchy: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SiteId):
            self.id = SiteId(self.id)

        if self._is_empty(self.site_type_id):
            self.MissingRequiredField("site_type_id")
        if not isinstance(self.site_type_id, str):
            self.site_type_id = str(self.site_type_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.group_id_hierarchy, list):
            self.group_id_hierarchy = (
                [self.group_id_hierarchy] if self.group_id_hierarchy is not None else []
            )
        self.group_id_hierarchy = [
            v if isinstance(v, str) else str(v) for v in self.group_id_hierarchy
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
    group_type_id: str = None
    name: str = None
    site_id: str = None
    parent_id: str = None
    description: Optional[str] = None
    capacity: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationId):
            self.id = LocationId(self.id)

        if self._is_empty(self.group_type_id):
            self.MissingRequiredField("group_type_id")
        if not isinstance(self.group_type_id, str):
            self.group_type_id = str(self.group_type_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.site_id):
            self.MissingRequiredField("site_id")
        if not isinstance(self.site_id, str):
            self.site_id = str(self.site_id)

        if self._is_empty(self.parent_id):
            self.MissingRequiredField("parent_id")
        if not isinstance(self.parent_id, str):
            self.parent_id = str(self.parent_id)

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
    species_id: str = None
    genet_type_id: str = None
    sf_id: str = None
    clonal_id: Optional[str] = None
    accession_number: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenetId):
            self.id = GenetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.species_id):
            self.MissingRequiredField("species_id")
        if not isinstance(self.species_id, str):
            self.species_id = str(self.species_id)

        if self._is_empty(self.genet_type_id):
            self.MissingRequiredField("genet_type_id")
        if not isinstance(self.genet_type_id, str):
            self.genet_type_id = str(self.genet_type_id)

        if self._is_empty(self.sf_id):
            self.MissingRequiredField("sf_id")
        if not isinstance(self.sf_id, str):
            self.sf_id = str(self.sf_id)

        if self.clonal_id is not None and not isinstance(self.clonal_id, str):
            self.clonal_id = str(self.clonal_id)

        if self.accession_number is not None and not isinstance(
            self.accession_number, str
        ):
            self.accession_number = str(self.accession_number)

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
    genet_id: str = None
    species_id: str = None
    site_id: str = None
    group_id: str = None
    coral_type_id: str = None
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

        if self._is_empty(self.genet_id):
            self.MissingRequiredField("genet_id")
        if not isinstance(self.genet_id, str):
            self.genet_id = str(self.genet_id)

        if self._is_empty(self.species_id):
            self.MissingRequiredField("species_id")
        if not isinstance(self.species_id, str):
            self.species_id = str(self.species_id)

        if self._is_empty(self.site_id):
            self.MissingRequiredField("site_id")
        if not isinstance(self.site_id, str):
            self.site_id = str(self.site_id)

        if self._is_empty(self.group_id):
            self.MissingRequiredField("group_id")
        if not isinstance(self.group_id, str):
            self.group_id = str(self.group_id)

        if self._is_empty(self.coral_type_id):
            self.MissingRequiredField("coral_type_id")
        if not isinstance(self.coral_type_id, str):
            self.coral_type_id = str(self.coral_type_id)

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
    image_url: Optional[str] = None

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

        if self.image_url is not None and not isinstance(self.image_url, str):
            self.image_url = str(self.image_url)

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
    event_type_id: str = None
    record_id: str = None
    record_model_type: Union[str, "ModelType"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self._is_empty(self.event_type_id):
            self.MissingRequiredField("event_type_id")
        if not isinstance(self.event_type_id, str):
            self.event_type_id = str(self.event_type_id)

        if self._is_empty(self.record_id):
            self.MissingRequiredField("record_id")
        if not isinstance(self.record_id, str):
            self.record_id = str(self.record_id)

        if self._is_empty(self.record_model_type):
            self.MissingRequiredField("record_model_type")
        if not isinstance(self.record_model_type, ModelType):
            self.record_model_type = ModelType(self.record_model_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpeciesRegisterEntry(YAMLRoot):
    """
    Represents an entry in the species registry
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["SpeciesRegisterEntry"]
    class_class_curie: ClassVar[str] = "oct_schema:SpeciesRegisterEntry"
    class_name: ClassVar[str] = "SpeciesRegisterEntry"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.SpeciesRegisterEntry

    id: Union[str, SpeciesRegisterEntryId] = None
    created_at: Union[str, XSDDateTime] = None
    updated_at: Union[str, XSDDateTime] = None
    genus: str = None
    specific_epithet: str = None
    common_name: Optional[str] = None
    scientific_name: Optional[str] = None
    photo_url: Optional[str] = None
    tags: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesRegisterEntryId):
            self.id = SpeciesRegisterEntryId(self.id)

        if self._is_empty(self.created_at):
            self.MissingRequiredField("created_at")
        if not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self._is_empty(self.updated_at):
            self.MissingRequiredField("updated_at")
        if not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

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

        if self.scientific_name is not None and not isinstance(
            self.scientific_name, str
        ):
            self.scientific_name = str(self.scientific_name)

        if self.photo_url is not None and not isinstance(self.photo_url, str):
            self.photo_url = str(self.photo_url)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganizationRegisterEntry(YAMLRoot):
    """
    Represents an entry in the organization registry
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT_SCHEMA["OrganizationRegisterEntry"]
    class_class_curie: ClassVar[str] = "oct_schema:OrganizationRegisterEntry"
    class_name: ClassVar[str] = "OrganizationRegisterEntry"
    class_model_uri: ClassVar[URIRef] = OCT_SCHEMA.OrganizationRegisterEntry

    id: Union[str, OrganizationRegisterEntryId] = None
    created_at: Union[str, XSDDateTime] = None
    updated_at: Union[str, XSDDateTime] = None
    name: str = None
    region: str = None
    description: Optional[str] = None
    website_url: Optional[str] = None
    contact_email: Optional[str] = None
    logo_url: Optional[str] = None
    is_active: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationRegisterEntryId):
            self.id = OrganizationRegisterEntryId(self.id)

        if self._is_empty(self.created_at):
            self.MissingRequiredField("created_at")
        if not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self._is_empty(self.updated_at):
            self.MissingRequiredField("updated_at")
        if not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.region):
            self.MissingRequiredField("region")
        if not isinstance(self.region, str):
            self.region = str(self.region)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.website_url is not None and not isinstance(self.website_url, str):
            self.website_url = str(self.website_url)

        if self.contact_email is not None and not isinstance(self.contact_email, str):
            self.contact_email = str(self.contact_email)

        if self.logo_url is not None and not isinstance(self.logo_url, str):
            self.logo_url = str(self.logo_url)

        if self.is_active is not None and not isinstance(self.is_active, Bool):
            self.is_active = Bool(self.is_active)

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

slots.created_at = Slot(
    uri=OCT_SCHEMA.created_at,
    name="created_at",
    curie=OCT_SCHEMA.curie("created_at"),
    model_uri=OCT_SCHEMA.created_at,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.created_by_id = Slot(
    uri=OCT_SCHEMA.created_by_id,
    name="created_by_id",
    curie=OCT_SCHEMA.curie("created_by_id"),
    model_uri=OCT_SCHEMA.created_by_id,
    domain=None,
    range=Optional[str],
)

slots.updated_at = Slot(
    uri=OCT_SCHEMA.updated_at,
    name="updated_at",
    curie=OCT_SCHEMA.curie("updated_at"),
    model_uri=OCT_SCHEMA.updated_at,
    domain=None,
    range=Optional[Union[str, XSDDateTime]],
)

slots.updated_by_id = Slot(
    uri=OCT_SCHEMA.updated_by_id,
    name="updated_by_id",
    curie=OCT_SCHEMA.curie("updated_by_id"),
    model_uri=OCT_SCHEMA.updated_by_id,
    domain=None,
    range=Optional[str],
)

slots.organization_id = Slot(
    uri=OCT_SCHEMA.organization_id,
    name="organization_id",
    curie=OCT_SCHEMA.curie("organization_id"),
    model_uri=OCT_SCHEMA.organization_id,
    domain=None,
    range=Optional[str],
)

slots.url_path = Slot(
    uri=OCT_SCHEMA.url_path,
    name="url_path",
    curie=OCT_SCHEMA.curie("url_path"),
    model_uri=OCT_SCHEMA.url_path,
    domain=None,
    range=Optional[str],
)

slots.internal_path = Slot(
    uri=OCT_SCHEMA.internal_path,
    name="internal_path",
    curie=OCT_SCHEMA.curie("internal_path"),
    model_uri=OCT_SCHEMA.internal_path,
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

slots.site_type_ids = Slot(
    uri=OCT_SCHEMA.site_type_ids,
    name="site_type_ids",
    curie=OCT_SCHEMA.curie("site_type_ids"),
    model_uri=OCT_SCHEMA.site_type_ids,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.species_ids = Slot(
    uri=OCT_SCHEMA.species_ids,
    name="species_ids",
    curie=OCT_SCHEMA.curie("species_ids"),
    model_uri=OCT_SCHEMA.species_ids,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.site_type_id = Slot(
    uri=OCT_SCHEMA.site_type_id,
    name="site_type_id",
    curie=OCT_SCHEMA.curie("site_type_id"),
    model_uri=OCT_SCHEMA.site_type_id,
    domain=None,
    range=Optional[str],
)

slots.group_id_hierarchy = Slot(
    uri=OCT_SCHEMA.group_id_hierarchy,
    name="group_id_hierarchy",
    curie=OCT_SCHEMA.curie("group_id_hierarchy"),
    model_uri=OCT_SCHEMA.group_id_hierarchy,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.group_type_id = Slot(
    uri=OCT_SCHEMA.group_type_id,
    name="group_type_id",
    curie=OCT_SCHEMA.curie("group_type_id"),
    model_uri=OCT_SCHEMA.group_type_id,
    domain=None,
    range=Optional[str],
)

slots.site_id = Slot(
    uri=OCT_SCHEMA.site_id,
    name="site_id",
    curie=OCT_SCHEMA.curie("site_id"),
    model_uri=OCT_SCHEMA.site_id,
    domain=None,
    range=Optional[str],
)

slots.parent_id = Slot(
    uri=OCT_SCHEMA.parent_id,
    name="parent_id",
    curie=OCT_SCHEMA.curie("parent_id"),
    model_uri=OCT_SCHEMA.parent_id,
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

slots.genet_type_id = Slot(
    uri=OCT_SCHEMA.genet_type_id,
    name="genet_type_id",
    curie=OCT_SCHEMA.curie("genet_type_id"),
    model_uri=OCT_SCHEMA.genet_type_id,
    domain=None,
    range=Optional[str],
)

slots.sf_id = Slot(
    uri=OCT_SCHEMA.sf_id,
    name="sf_id",
    curie=OCT_SCHEMA.curie("sf_id"),
    model_uri=OCT_SCHEMA.sf_id,
    domain=None,
    range=Optional[str],
)

slots.clonal_id = Slot(
    uri=OCT_SCHEMA.clonal_id,
    name="clonal_id",
    curie=OCT_SCHEMA.curie("clonal_id"),
    model_uri=OCT_SCHEMA.clonal_id,
    domain=None,
    range=Optional[str],
)

slots.accession_number = Slot(
    uri=OCT_SCHEMA.accession_number,
    name="accession_number",
    curie=OCT_SCHEMA.curie("accession_number"),
    model_uri=OCT_SCHEMA.accession_number,
    domain=None,
    range=Optional[str],
)

slots.genet_id = Slot(
    uri=OCT_SCHEMA.genet_id,
    name="genet_id",
    curie=OCT_SCHEMA.curie("genet_id"),
    model_uri=OCT_SCHEMA.genet_id,
    domain=None,
    range=Optional[str],
)

slots.species_id = Slot(
    uri=OCT_SCHEMA.species_id,
    name="species_id",
    curie=OCT_SCHEMA.curie("species_id"),
    model_uri=OCT_SCHEMA.species_id,
    domain=None,
    range=Optional[str],
)

slots.group_id = Slot(
    uri=OCT_SCHEMA.group_id,
    name="group_id",
    curie=OCT_SCHEMA.curie("group_id"),
    model_uri=OCT_SCHEMA.group_id,
    domain=None,
    range=Optional[str],
)

slots.coral_type_id = Slot(
    uri=OCT_SCHEMA.coral_type_id,
    name="coral_type_id",
    curie=OCT_SCHEMA.curie("coral_type_id"),
    model_uri=OCT_SCHEMA.coral_type_id,
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

slots.image_url = Slot(
    uri=OCT_SCHEMA.image_url,
    name="image_url",
    curie=OCT_SCHEMA.curie("image_url"),
    model_uri=OCT_SCHEMA.image_url,
    domain=None,
    range=Optional[str],
)

slots.event_type_id = Slot(
    uri=OCT_SCHEMA.event_type_id,
    name="event_type_id",
    curie=OCT_SCHEMA.curie("event_type_id"),
    model_uri=OCT_SCHEMA.event_type_id,
    domain=None,
    range=Optional[str],
)

slots.record_id = Slot(
    uri=OCT_SCHEMA.record_id,
    name="record_id",
    curie=OCT_SCHEMA.curie("record_id"),
    model_uri=OCT_SCHEMA.record_id,
    domain=None,
    range=Optional[str],
)

slots.record_model_type = Slot(
    uri=OCT_SCHEMA.record_model_type,
    name="record_model_type",
    curie=OCT_SCHEMA.curie("record_model_type"),
    model_uri=OCT_SCHEMA.record_model_type,
    domain=None,
    range=Optional[Union[str, "ModelType"]],
)

slots.scientific_name = Slot(
    uri=OCT_SCHEMA.scientific_name,
    name="scientific_name",
    curie=OCT_SCHEMA.curie("scientific_name"),
    model_uri=OCT_SCHEMA.scientific_name,
    domain=None,
    range=Optional[str],
)

slots.photo_url = Slot(
    uri=OCT_SCHEMA.photo_url,
    name="photo_url",
    curie=OCT_SCHEMA.curie("photo_url"),
    model_uri=OCT_SCHEMA.photo_url,
    domain=None,
    range=Optional[str],
)

slots.tags = Slot(
    uri=OCT_SCHEMA.tags,
    name="tags",
    curie=OCT_SCHEMA.curie("tags"),
    model_uri=OCT_SCHEMA.tags,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.region = Slot(
    uri=OCT_SCHEMA.region,
    name="region",
    curie=OCT_SCHEMA.curie("region"),
    model_uri=OCT_SCHEMA.region,
    domain=None,
    range=Optional[str],
)

slots.website_url = Slot(
    uri=OCT_SCHEMA.website_url,
    name="website_url",
    curie=OCT_SCHEMA.curie("website_url"),
    model_uri=OCT_SCHEMA.website_url,
    domain=None,
    range=Optional[str],
)

slots.contact_email = Slot(
    uri=OCT_SCHEMA.contact_email,
    name="contact_email",
    curie=OCT_SCHEMA.curie("contact_email"),
    model_uri=OCT_SCHEMA.contact_email,
    domain=None,
    range=Optional[str],
)

slots.logo_url = Slot(
    uri=OCT_SCHEMA.logo_url,
    name="logo_url",
    curie=OCT_SCHEMA.curie("logo_url"),
    model_uri=OCT_SCHEMA.logo_url,
    domain=None,
    range=Optional[str],
)

slots.is_active = Slot(
    uri=OCT_SCHEMA.is_active,
    name="is_active",
    curie=OCT_SCHEMA.curie("is_active"),
    model_uri=OCT_SCHEMA.is_active,
    domain=None,
    range=Optional[Union[bool, Bool]],
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

slots.Site_site_type_id = Slot(
    uri=OCT_SCHEMA.site_type_id,
    name="Site_site_type_id",
    curie=OCT_SCHEMA.curie("site_type_id"),
    model_uri=OCT_SCHEMA.Site_site_type_id,
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

slots.Location_group_type_id = Slot(
    uri=OCT_SCHEMA.group_type_id,
    name="Location_group_type_id",
    curie=OCT_SCHEMA.curie("group_type_id"),
    model_uri=OCT_SCHEMA.Location_group_type_id,
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

slots.Location_site_id = Slot(
    uri=OCT_SCHEMA.site_id,
    name="Location_site_id",
    curie=OCT_SCHEMA.curie("site_id"),
    model_uri=OCT_SCHEMA.Location_site_id,
    domain=Location,
    range=str,
)

slots.Location_parent_id = Slot(
    uri=OCT_SCHEMA.parent_id,
    name="Location_parent_id",
    curie=OCT_SCHEMA.curie("parent_id"),
    model_uri=OCT_SCHEMA.Location_parent_id,
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

slots.Genet_species_id = Slot(
    uri=OCT_SCHEMA.species_id,
    name="Genet_species_id",
    curie=OCT_SCHEMA.curie("species_id"),
    model_uri=OCT_SCHEMA.Genet_species_id,
    domain=Genet,
    range=str,
)

slots.Genet_genet_type_id = Slot(
    uri=OCT_SCHEMA.genet_type_id,
    name="Genet_genet_type_id",
    curie=OCT_SCHEMA.curie("genet_type_id"),
    model_uri=OCT_SCHEMA.Genet_genet_type_id,
    domain=Genet,
    range=str,
)

slots.Genet_sf_id = Slot(
    uri=OCT_SCHEMA.sf_id,
    name="Genet_sf_id",
    curie=OCT_SCHEMA.curie("sf_id"),
    model_uri=OCT_SCHEMA.Genet_sf_id,
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

slots.Coral_genet_id = Slot(
    uri=OCT_SCHEMA.genet_id,
    name="Coral_genet_id",
    curie=OCT_SCHEMA.curie("genet_id"),
    model_uri=OCT_SCHEMA.Coral_genet_id,
    domain=Coral,
    range=str,
)

slots.Coral_species_id = Slot(
    uri=OCT_SCHEMA.species_id,
    name="Coral_species_id",
    curie=OCT_SCHEMA.curie("species_id"),
    model_uri=OCT_SCHEMA.Coral_species_id,
    domain=Coral,
    range=str,
)

slots.Coral_site_id = Slot(
    uri=OCT_SCHEMA.site_id,
    name="Coral_site_id",
    curie=OCT_SCHEMA.curie("site_id"),
    model_uri=OCT_SCHEMA.Coral_site_id,
    domain=Coral,
    range=str,
)

slots.Coral_group_id = Slot(
    uri=OCT_SCHEMA.group_id,
    name="Coral_group_id",
    curie=OCT_SCHEMA.curie("group_id"),
    model_uri=OCT_SCHEMA.Coral_group_id,
    domain=Coral,
    range=str,
)

slots.Coral_coral_type_id = Slot(
    uri=OCT_SCHEMA.coral_type_id,
    name="Coral_coral_type_id",
    curie=OCT_SCHEMA.curie("coral_type_id"),
    model_uri=OCT_SCHEMA.Coral_coral_type_id,
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

slots.Event_event_type_id = Slot(
    uri=OCT_SCHEMA.event_type_id,
    name="Event_event_type_id",
    curie=OCT_SCHEMA.curie("event_type_id"),
    model_uri=OCT_SCHEMA.Event_event_type_id,
    domain=Event,
    range=str,
)

slots.Event_record_id = Slot(
    uri=OCT_SCHEMA.record_id,
    name="Event_record_id",
    curie=OCT_SCHEMA.curie("record_id"),
    model_uri=OCT_SCHEMA.Event_record_id,
    domain=Event,
    range=str,
)

slots.Event_record_model_type = Slot(
    uri=OCT_SCHEMA.record_model_type,
    name="Event_record_model_type",
    curie=OCT_SCHEMA.curie("record_model_type"),
    model_uri=OCT_SCHEMA.Event_record_model_type,
    domain=Event,
    range=Union[str, "ModelType"],
)

slots.SpeciesRegisterEntry_id = Slot(
    uri=OCT_SCHEMA.id,
    name="SpeciesRegisterEntry_id",
    curie=OCT_SCHEMA.curie("id"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_id,
    domain=SpeciesRegisterEntry,
    range=Union[str, SpeciesRegisterEntryId],
)

slots.SpeciesRegisterEntry_created_at = Slot(
    uri=OCT_SCHEMA.created_at,
    name="SpeciesRegisterEntry_created_at",
    curie=OCT_SCHEMA.curie("created_at"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_created_at,
    domain=SpeciesRegisterEntry,
    range=Union[str, XSDDateTime],
)

slots.SpeciesRegisterEntry_updated_at = Slot(
    uri=OCT_SCHEMA.updated_at,
    name="SpeciesRegisterEntry_updated_at",
    curie=OCT_SCHEMA.curie("updated_at"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_updated_at,
    domain=SpeciesRegisterEntry,
    range=Union[str, XSDDateTime],
)

slots.SpeciesRegisterEntry_common_name = Slot(
    uri=OCT_SCHEMA.common_name,
    name="SpeciesRegisterEntry_common_name",
    curie=OCT_SCHEMA.curie("common_name"),
    model_uri=OCT_SCHEMA.SpeciesRegisterEntry_common_name,
    domain=SpeciesRegisterEntry,
    range=Optional[str],
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

slots.OrganizationRegisterEntry_id = Slot(
    uri=OCT_SCHEMA.id,
    name="OrganizationRegisterEntry_id",
    curie=OCT_SCHEMA.curie("id"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_id,
    domain=OrganizationRegisterEntry,
    range=Union[str, OrganizationRegisterEntryId],
)

slots.OrganizationRegisterEntry_created_at = Slot(
    uri=OCT_SCHEMA.created_at,
    name="OrganizationRegisterEntry_created_at",
    curie=OCT_SCHEMA.curie("created_at"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_created_at,
    domain=OrganizationRegisterEntry,
    range=Union[str, XSDDateTime],
)

slots.OrganizationRegisterEntry_updated_at = Slot(
    uri=OCT_SCHEMA.updated_at,
    name="OrganizationRegisterEntry_updated_at",
    curie=OCT_SCHEMA.curie("updated_at"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_updated_at,
    domain=OrganizationRegisterEntry,
    range=Union[str, XSDDateTime],
)

slots.OrganizationRegisterEntry_name = Slot(
    uri=OCT_SCHEMA.name,
    name="OrganizationRegisterEntry_name",
    curie=OCT_SCHEMA.curie("name"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_name,
    domain=OrganizationRegisterEntry,
    range=str,
)

slots.OrganizationRegisterEntry_region = Slot(
    uri=OCT_SCHEMA.region,
    name="OrganizationRegisterEntry_region",
    curie=OCT_SCHEMA.curie("region"),
    model_uri=OCT_SCHEMA.OrganizationRegisterEntry_region,
    domain=OrganizationRegisterEntry,
    range=str,
)
