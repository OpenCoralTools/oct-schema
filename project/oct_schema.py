# Auto generated from oct_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-07T18:57:50
# Schema: oct-schema
#
# id: https://opencoral.tools/oct-schema
# description: Top-level schema combining Core and Coral modules.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import re
from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
OCT = CurieNamespace("oct", "https://opencoral.tools/oct-schema/")
RDF = CurieNamespace("rdf", "http://example.org/UNKNOWN/rdf/")
XSD = CurieNamespace("xsd", "http://www.w3.org/2001/XMLSchema#")
DEFAULT_ = OCT


# Types
class DateTime(str):
    """A timestamp in ISO 8601 format (e.g. 2023-01-01T12:00:00Z)"""

    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DateTime"
    type_model_uri = OCT.DateTime


class Identifier(str):
    """A unique identifier for a record (URI, UUID, or CURIE)"""

    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Identifier"
    type_model_uri = OCT.Identifier


# Class references
class RecordRecordId(extended_str):
    pass


class GenetRecordRecordId(RecordRecordId):
    pass


class PersonRecordId(RecordRecordId):
    pass


class OrganizationRecordId(RecordRecordId):
    pass


class LocationRecordRecordId(RecordRecordId):
    pass


class CoralLocationRecordRecordId(LocationRecordRecordId):
    pass


class SpecimenRecordRecordId(RecordRecordId):
    pass


class CoralSpecimenRecordRecordId(SpecimenRecordRecordId):
    pass


class EventRecordId(RecordRecordId):
    pass


class CoralEventRecordId(EventRecordId):
    pass


@dataclass(repr=False)
class CoralTaxonRef(YAMLRoot):
    """
    Coral-specific taxon reference with species code
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/CoralTaxonRef"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/CoralTaxonRef"
    class_name: ClassVar[str] = "CoralTaxonRef"
    class_model_uri: ClassVar[URIRef] = OCT.CoralTaxonRef

    speciesCode: str = None
    scientificName: Optional[str] = None
    taxonId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.speciesCode):
            self.MissingRequiredField("speciesCode")
        if not isinstance(self.speciesCode, str):
            self.speciesCode = str(self.speciesCode)

        if self.scientificName is not None and not isinstance(self.scientificName, str):
            self.scientificName = str(self.scientificName)

        if self.taxonId is not None and not isinstance(self.taxonId, str):
            self.taxonId = str(self.taxonId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenetOrigin(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/GenetOrigin"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/GenetOrigin"
    class_name: ClassVar[str] = "GenetOrigin"
    class_model_uri: ClassVar[URIRef] = OCT.GenetOrigin

    originType: Optional[Union[str, "GenetOriginType"]] = None
    collectedAt: Optional[str] = None
    collectionLocationRef: Optional[Union[dict, "LocationRef"]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.originType is not None and not isinstance(
            self.originType, GenetOriginType
        ):
            self.originType = GenetOriginType(self.originType)

        if self.collectedAt is not None and not isinstance(self.collectedAt, str):
            self.collectedAt = str(self.collectedAt)

        if self.collectionLocationRef is not None and not isinstance(
            self.collectionLocationRef, LocationRef
        ):
            self.collectionLocationRef = LocationRef(
                **as_dict(self.collectionLocationRef)
            )

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenotypingMetadata(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/GenotypingMetadata"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/GenotypingMetadata"
    class_name: ClassVar[str] = "GenotypingMetadata"
    class_model_uri: ClassVar[URIRef] = OCT.GenotypingMetadata

    method: Optional[str] = None
    lab: Optional[str] = None
    assayDate: Optional[str] = None
    associatedSequences: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        if self.lab is not None and not isinstance(self.lab, str):
            self.lab = str(self.lab)

        if self.assayDate is not None and not isinstance(self.assayDate, str):
            self.assayDate = str(self.assayDate)

        if not isinstance(self.associatedSequences, list):
            self.associatedSequences = (
                [self.associatedSequences]
                if self.associatedSequences is not None
                else []
            )
        self.associatedSequences = [
            v if isinstance(v, str) else str(v) for v in self.associatedSequences
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenetPedigree(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/GenetPedigree"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/GenetPedigree"
    class_name: ClassVar[str] = "GenetPedigree"
    class_model_uri: ClassVar[URIRef] = OCT.GenetPedigree

    damGenetId: Optional[str] = None
    sireGenetId: Optional[str] = None
    cohortId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.damGenetId is not None and not isinstance(self.damGenetId, str):
            self.damGenetId = str(self.damGenetId)

        if self.sireGenetId is not None and not isinstance(self.sireGenetId, str):
            self.sireGenetId = str(self.sireGenetId)

        if self.cohortId is not None and not isinstance(self.cohortId, str):
            self.cohortId = str(self.cohortId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GenetRecordSource(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/GenetRecordSource"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/GenetRecordSource"
    class_name: ClassVar[str] = "GenetRecordSource"
    class_model_uri: ClassVar[URIRef] = OCT.GenetRecordSource

    datasetId: Optional[str] = None
    externalRecordId: Optional[str] = None
    ingestedAt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.datasetId is not None and not isinstance(self.datasetId, str):
            self.datasetId = str(self.datasetId)

        if self.externalRecordId is not None and not isinstance(
            self.externalRecordId, str
        ):
            self.externalRecordId = str(self.externalRecordId)

        if self.ingestedAt is not None and not isinstance(self.ingestedAt, str):
            self.ingestedAt = str(self.ingestedAt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoPoint(YAMLRoot):
    """
    A geographic coordinate
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/types/GeoPoint"]
    class_class_curie: ClassVar[str] = "oct:core/types/GeoPoint"
    class_name: ClassVar[str] = "GeoPoint"
    class_model_uri: ClassVar[URIRef] = OCT.GeoPoint

    decimalLatitude: float = None
    decimalLongitude: float = None
    geodeticDatum: Optional[str] = "WGS84"
    coordinateUncertaintyMeters: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.decimalLatitude):
            self.MissingRequiredField("decimalLatitude")
        if not isinstance(self.decimalLatitude, float):
            self.decimalLatitude = float(self.decimalLatitude)

        if self._is_empty(self.decimalLongitude):
            self.MissingRequiredField("decimalLongitude")
        if not isinstance(self.decimalLongitude, float):
            self.decimalLongitude = float(self.decimalLongitude)

        if self.geodeticDatum is not None and not isinstance(self.geodeticDatum, str):
            self.geodeticDatum = str(self.geodeticDatum)

        if self.coordinateUncertaintyMeters is not None and not isinstance(
            self.coordinateUncertaintyMeters, float
        ):
            self.coordinateUncertaintyMeters = float(self.coordinateUncertaintyMeters)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasureValue(YAMLRoot):
    """
    A measured value with a unit
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/types/MeasureValue"]
    class_class_curie: ClassVar[str] = "oct:core/types/MeasureValue"
    class_name: ClassVar[str] = "MeasureValue"
    class_model_uri: ClassVar[URIRef] = OCT.MeasureValue

    value: float = None
    unit: str = None
    method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.method is not None and not isinstance(self.method, str):
            self.method = str(self.method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityRef(YAMLRoot):
    """
    A generic reference to another entity
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/types/EntityRef"]
    class_class_curie: ClassVar[str] = "oct:core/types/EntityRef"
    class_name: ClassVar[str] = "EntityRef"
    class_model_uri: ClassVar[URIRef] = OCT.EntityRef

    id: str = None
    type: Optional[str] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonRef(YAMLRoot):
    """
    A reference to a taxonomic entity
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/types/TaxonRef"]
    class_class_curie: ClassVar[str] = "oct:core/types/TaxonRef"
    class_name: ClassVar[str] = "TaxonRef"
    class_model_uri: ClassVar[URIRef] = OCT.TaxonRef

    name: str = None
    taxonId: Optional[str] = None
    rank: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.taxonId is not None and not isinstance(self.taxonId, str):
            self.taxonId = str(self.taxonId)

        if self.rank is not None and not isinstance(self.rank, str):
            self.rank = str(self.rank)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    Base class for all authoritative records
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/record/Record"]
    class_class_curie: ClassVar[str] = "oct:core/record/Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = OCT.Record

    recordId: Union[str, RecordRecordId] = None
    recordType: str = None
    orgId: str = None
    createdAt: Optional[str] = None
    createdBy: Optional[str] = None
    updatedAt: Optional[str] = None
    updatedBy: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, RecordRecordId):
            self.recordId = RecordRecordId(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        self.recordType = str(self.class_name)

        if self._is_empty(self.orgId):
            self.MissingRequiredField("orgId")
        if not isinstance(self.orgId, str):
            self.orgId = str(self.orgId)

        if self.createdAt is not None and not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if self.updatedAt is not None and not isinstance(self.updatedAt, str):
            self.updatedAt = str(self.updatedAt)

        if self.updatedBy is not None and not isinstance(self.updatedBy, str):
            self.updatedBy = str(self.updatedBy)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "recordType"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class GenetRecord(Record):
    """
    Coral-specific genet record (clonal lineage)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/genet/GenetRecord"]
    class_class_curie: ClassVar[str] = "oct:coral/genet/GenetRecord"
    class_name: ClassVar[str] = "GenetRecord"
    class_model_uri: ClassVar[URIRef] = OCT.GenetRecord

    recordId: Union[str, GenetRecordRecordId] = None
    orgId: str = None
    recordType: str = None
    createdAt: str = None
    taxon: Union[dict, CoralTaxonRef] = None
    genetCode: str = None
    updatedAt: Optional[str] = None
    origin: Optional[Union[dict, GenetOrigin]] = None
    genotyping: Optional[Union[dict, GenotypingMetadata]] = None
    pedigree: Optional[Union[dict, GenetPedigree]] = None
    notes: Optional[str] = None
    source: Optional[Union[dict, GenetRecordSource]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, GenetRecordRecordId):
            self.recordId = GenetRecordRecordId(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        self.recordType = str(self.class_name)

        if self._is_empty(self.createdAt):
            self.MissingRequiredField("createdAt")
        if not isinstance(self.createdAt, str):
            self.createdAt = str(self.createdAt)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, CoralTaxonRef):
            self.taxon = CoralTaxonRef(**as_dict(self.taxon))

        if self._is_empty(self.genetCode):
            self.MissingRequiredField("genetCode")
        if not isinstance(self.genetCode, str):
            self.genetCode = str(self.genetCode)

        if self.updatedAt is not None and not isinstance(self.updatedAt, str):
            self.updatedAt = str(self.updatedAt)

        if self.origin is not None and not isinstance(self.origin, GenetOrigin):
            self.origin = GenetOrigin(**as_dict(self.origin))

        if self.genotyping is not None and not isinstance(
            self.genotyping, GenotypingMetadata
        ):
            self.genotyping = GenotypingMetadata(**as_dict(self.genotyping))

        if self.pedigree is not None and not isinstance(self.pedigree, GenetPedigree):
            self.pedigree = GenetPedigree(**as_dict(self.pedigree))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.source is not None and not isinstance(self.source, GenetRecordSource):
            self.source = GenetRecordSource(**as_dict(self.source))

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)


@dataclass(repr=False)
class Person(Record):
    """
    Represents a human user or agent
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/person/Person"]
    class_class_curie: ClassVar[str] = "oct:core/person/Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OCT.Person

    recordId: Union[str, PersonRecordId] = None
    orgId: str = None
    name: str = None
    email: str = None
    recordType: Optional[str] = None
    imageUrl: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, PersonRecordId):
            self.recordId = PersonRecordId(self.recordId)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        self.recordType = str(self.class_name)

        if self.imageUrl is not None and not isinstance(self.imageUrl, str):
            self.imageUrl = str(self.imageUrl)

        super().__post_init__(**kwargs)
        self.unknown_recordType = str(self.class_name)


@dataclass(repr=False)
class Organization(Record):
    """
    Represents an organization
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/organization/Organization"]
    class_class_curie: ClassVar[str] = "oct:core/organization/Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = OCT.Organization

    recordId: Union[str, OrganizationRecordId] = None
    orgId: str = None
    name: str = None
    recordType: Optional[str] = None
    domain: Optional[str] = None
    supportedSiteTypes: Optional[
        Union[Union[str, "SiteType"], list[Union[str, "SiteType"]]]
    ] = empty_list()
    supportedSpecies: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, OrganizationRecordId):
            self.recordId = OrganizationRecordId(self.recordId)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self.recordType = str(self.class_name)

        if self.domain is not None and not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if not isinstance(self.supportedSiteTypes, list):
            self.supportedSiteTypes = (
                [self.supportedSiteTypes] if self.supportedSiteTypes is not None else []
            )
        self.supportedSiteTypes = [
            v if isinstance(v, SiteType) else SiteType(v)
            for v in self.supportedSiteTypes
        ]

        if not isinstance(self.supportedSpecies, list):
            self.supportedSpecies = (
                [self.supportedSpecies] if self.supportedSpecies is not None else []
            )
        self.supportedSpecies = [
            v if isinstance(v, str) else str(v) for v in self.supportedSpecies
        ]

        super().__post_init__(**kwargs)
        self.unknown_recordType = str(self.class_name)


@dataclass(repr=False)
class LocationRef(YAMLRoot):
    """
    A lightweight reference to a location
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/location/LocationRef"]
    class_class_curie: ClassVar[str] = "oct:core/location/LocationRef"
    class_name: ClassVar[str] = "LocationRef"
    class_model_uri: ClassVar[URIRef] = OCT.LocationRef

    locationId: str = None
    locationType: Optional[Union[str, "LocationType"]] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.locationId):
            self.MissingRequiredField("locationId")
        if not isinstance(self.locationId, str):
            self.locationId = str(self.locationId)

        if self.locationType is not None and not isinstance(
            self.locationType, LocationType
        ):
            self.locationType = LocationType(self.locationType)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParentLocationRef(LocationRef):
    """
    Reference to a parent location with structural type information
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/location/ParentLocationRef"]
    class_class_curie: ClassVar[str] = "oct:core/location/ParentLocationRef"
    class_name: ClassVar[str] = "ParentLocationRef"
    class_model_uri: ClassVar[URIRef] = OCT.ParentLocationRef

    locationId: str = None
    siteType: Optional[Union[str, "SiteType"]] = None
    containerType: Optional[Union[str, "ContainerType"]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.siteType is not None and not isinstance(self.siteType, SiteType):
            self.siteType = SiteType(self.siteType)

        if self.containerType is not None and not isinstance(
            self.containerType, ContainerType
        ):
            self.containerType = ContainerType(self.containerType)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocationRecord(Record):
    """
    A record representing a physical or logical location
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/location/LocationRecord"]
    class_class_curie: ClassVar[str] = "oct:core/location/LocationRecord"
    class_name: ClassVar[str] = "LocationRecord"
    class_model_uri: ClassVar[URIRef] = OCT.LocationRecord

    recordId: Union[str, LocationRecordRecordId] = None
    orgId: str = None
    recordType: str = None
    locationType: Union[str, "LocationType"] = None
    name: str = None
    parentLocationRef: Optional[Union[dict, ParentLocationRef]] = None
    siteType: Optional[Union[str, "SiteType"]] = None
    containerType: Optional[Union[str, "ContainerType"]] = None
    positionType: Optional[Union[str, "PositionType"]] = None
    geo: Optional[Union[dict, GeoPoint]] = None
    depth: Optional[Union[dict, MeasureValue]] = None
    notes: Optional[str] = None
    codes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, LocationRecordRecordId):
            self.recordId = LocationRecordRecordId(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        self.recordType = str(self.class_name)

        if self._is_empty(self.locationType):
            self.MissingRequiredField("locationType")
        if not isinstance(self.locationType, LocationType):
            self.locationType = LocationType(self.locationType)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.parentLocationRef is not None and not isinstance(
            self.parentLocationRef, ParentLocationRef
        ):
            self.parentLocationRef = ParentLocationRef(
                **as_dict(self.parentLocationRef)
            )

        if self.siteType is not None and not isinstance(self.siteType, SiteType):
            self.siteType = SiteType(self.siteType)

        if self.containerType is not None and not isinstance(
            self.containerType, ContainerType
        ):
            self.containerType = ContainerType(self.containerType)

        if self.positionType is not None and not isinstance(
            self.positionType, PositionType
        ):
            self.positionType = PositionType(self.positionType)

        if self.geo is not None and not isinstance(self.geo, GeoPoint):
            self.geo = GeoPoint(**as_dict(self.geo))

        if self.depth is not None and not isinstance(self.depth, MeasureValue):
            self.depth = MeasureValue(**as_dict(self.depth))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.codes, list):
            self.codes = [self.codes] if self.codes is not None else []
        self.codes = [v if isinstance(v, str) else str(v) for v in self.codes]

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "recordType"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class CoralLocationRecord(LocationRecord):
    """
    A location record used in coral restoration (extensible placeholder)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/location/CoralLocationRecord"]
    class_class_curie: ClassVar[str] = "oct:coral/location/CoralLocationRecord"
    class_name: ClassVar[str] = "CoralLocationRecord"
    class_model_uri: ClassVar[URIRef] = OCT.CoralLocationRecord

    recordId: Union[str, CoralLocationRecordRecordId] = None
    orgId: str = None
    recordType: str = None
    locationType: Union[str, "LocationType"] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, CoralLocationRecordRecordId):
            self.recordId = CoralLocationRecordRecordId(self.recordId)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)


@dataclass(repr=False)
class Quantity(YAMLRoot):
    """
    Quantification of the specimen (count, size, etc.)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/specimen/Quantity"]
    class_class_curie: ClassVar[str] = "oct:core/specimen/Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = OCT.Quantity

    count: float = None
    countUncertainty: Optional[float] = None
    surfaceArea: Optional[Union[dict, MeasureValue]] = None
    volume: Optional[Union[dict, MeasureValue]] = None
    biomass: Optional[Union[dict, MeasureValue]] = None
    linearSize: Optional[Union[dict, MeasureValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.count):
            self.MissingRequiredField("count")
        if not isinstance(self.count, float):
            self.count = float(self.count)

        if self.countUncertainty is not None and not isinstance(
            self.countUncertainty, float
        ):
            self.countUncertainty = float(self.countUncertainty)

        if self.surfaceArea is not None and not isinstance(
            self.surfaceArea, MeasureValue
        ):
            self.surfaceArea = MeasureValue(**as_dict(self.surfaceArea))

        if self.volume is not None and not isinstance(self.volume, MeasureValue):
            self.volume = MeasureValue(**as_dict(self.volume))

        if self.biomass is not None and not isinstance(self.biomass, MeasureValue):
            self.biomass = MeasureValue(**as_dict(self.biomass))

        if self.linearSize is not None and not isinstance(
            self.linearSize, MeasureValue
        ):
            self.linearSize = MeasureValue(**as_dict(self.linearSize))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenState(YAMLRoot):
    """
    Derived state of the specimen
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/specimen/SpecimenState"]
    class_class_curie: ClassVar[str] = "oct:core/specimen/SpecimenState"
    class_name: ClassVar[str] = "SpecimenState"
    class_model_uri: ClassVar[URIRef] = OCT.SpecimenState

    disposition: Optional[Union[str, "DispositionStatus"]] = None
    health: Optional[Union[str, "HealthStatus"]] = None
    readyForPropagation: Optional[Union[bool, Bool]] = None
    readyForOutplant: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.disposition is not None and not isinstance(
            self.disposition, DispositionStatus
        ):
            self.disposition = DispositionStatus(self.disposition)

        if self.health is not None and not isinstance(self.health, HealthStatus):
            self.health = HealthStatus(self.health)

        if self.readyForPropagation is not None and not isinstance(
            self.readyForPropagation, Bool
        ):
            self.readyForPropagation = Bool(self.readyForPropagation)

        if self.readyForOutplant is not None and not isinstance(
            self.readyForOutplant, Bool
        ):
            self.readyForOutplant = Bool(self.readyForOutplant)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenRecordSource(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/specimen/SpecimenRecordSource"]
    class_class_curie: ClassVar[str] = "oct:core/specimen/SpecimenRecordSource"
    class_name: ClassVar[str] = "SpecimenRecordSource"
    class_model_uri: ClassVar[URIRef] = OCT.SpecimenRecordSource

    datasetId: Optional[str] = None
    externalRecordId: Optional[str] = None
    ingestedAt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.datasetId is not None and not isinstance(self.datasetId, str):
            self.datasetId = str(self.datasetId)

        if self.externalRecordId is not None and not isinstance(
            self.externalRecordId, str
        ):
            self.externalRecordId = str(self.externalRecordId)

        if self.ingestedAt is not None and not isinstance(self.ingestedAt, str):
            self.ingestedAt = str(self.ingestedAt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecimenRecord(Record):
    """
    A record representing a biological specimen or group
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/specimen/SpecimenRecord"]
    class_class_curie: ClassVar[str] = "oct:core/specimen/SpecimenRecord"
    class_name: ClassVar[str] = "SpecimenRecord"
    class_model_uri: ClassVar[URIRef] = OCT.SpecimenRecord

    recordId: Union[str, SpecimenRecordRecordId] = None
    orgId: str = None
    recordType: str = None
    asOf: str = None
    taxon: Union[dict, TaxonRef] = None
    inventoryUnitType: Union[str, "InventoryUnitType"] = None
    quantity: Union[dict, Quantity] = None
    locationRef: Union[dict, LocationRef] = None
    geneticGroupRef: Optional[Union[dict, EntityRef]] = None
    developmentalStage: Optional[Union[str, "DevelopmentalStage"]] = None
    state: Optional[Union[dict, SpecimenState]] = None
    tags: Optional[Union[str, list[str]]] = empty_list()
    notes: Optional[str] = None
    source: Optional[Union[dict, SpecimenRecordSource]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, SpecimenRecordRecordId):
            self.recordId = SpecimenRecordRecordId(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        self.recordType = str(self.class_name)

        if self._is_empty(self.asOf):
            self.MissingRequiredField("asOf")
        if not isinstance(self.asOf, str):
            self.asOf = str(self.asOf)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, TaxonRef):
            self.taxon = TaxonRef(**as_dict(self.taxon))

        if self._is_empty(self.inventoryUnitType):
            self.MissingRequiredField("inventoryUnitType")
        if not isinstance(self.inventoryUnitType, InventoryUnitType):
            self.inventoryUnitType = InventoryUnitType(self.inventoryUnitType)

        if self._is_empty(self.quantity):
            self.MissingRequiredField("quantity")
        if not isinstance(self.quantity, Quantity):
            self.quantity = Quantity(**as_dict(self.quantity))

        if self._is_empty(self.locationRef):
            self.MissingRequiredField("locationRef")
        if not isinstance(self.locationRef, LocationRef):
            self.locationRef = LocationRef(**as_dict(self.locationRef))

        if self.geneticGroupRef is not None and not isinstance(
            self.geneticGroupRef, EntityRef
        ):
            self.geneticGroupRef = EntityRef(**as_dict(self.geneticGroupRef))

        if self.developmentalStage is not None and not isinstance(
            self.developmentalStage, DevelopmentalStage
        ):
            self.developmentalStage = DevelopmentalStage(self.developmentalStage)

        if self.state is not None and not isinstance(self.state, SpecimenState):
            self.state = SpecimenState(**as_dict(self.state))

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.source is not None and not isinstance(
            self.source, SpecimenRecordSource
        ):
            self.source = SpecimenRecordSource(**as_dict(self.source))

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "recordType"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class CoralSpecimenRecord(SpecimenRecord):
    """
    A specimen record representing a coral
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/specimen/CoralSpecimenRecord"]
    class_class_curie: ClassVar[str] = "oct:coral/specimen/CoralSpecimenRecord"
    class_name: ClassVar[str] = "CoralSpecimenRecord"
    class_model_uri: ClassVar[URIRef] = OCT.CoralSpecimenRecord

    recordId: Union[str, CoralSpecimenRecordRecordId] = None
    orgId: str = None
    recordType: str = None
    asOf: str = None
    quantity: Union[dict, Quantity] = None
    locationRef: Union[dict, LocationRef] = None
    taxon: Union[dict, CoralTaxonRef] = None
    inventoryUnitType: Union[str, "InventoryUnitType"] = None
    geneticGroupRef: Optional[Union[str, GenetRecordRecordId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, CoralSpecimenRecordRecordId):
            self.recordId = CoralSpecimenRecordRecordId(self.recordId)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, CoralTaxonRef):
            self.taxon = CoralTaxonRef(**as_dict(self.taxon))

        if self._is_empty(self.inventoryUnitType):
            self.MissingRequiredField("inventoryUnitType")
        if not isinstance(self.inventoryUnitType, InventoryUnitType):
            self.inventoryUnitType = InventoryUnitType(self.inventoryUnitType)

        if self.geneticGroupRef is not None and not isinstance(
            self.geneticGroupRef, GenetRecordRecordId
        ):
            self.geneticGroupRef = GenetRecordRecordId(self.geneticGroupRef)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)


@dataclass(repr=False)
class EffectiveTime(YAMLRoot):
    """
    Time of the event (moment or interval)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/EffectiveTime"]
    class_class_curie: ClassVar[str] = "oct:core/event/EffectiveTime"
    class_name: ClassVar[str] = "EffectiveTime"
    class_model_uri: ClassVar[URIRef] = OCT.EffectiveTime

    occurredAt: Optional[str] = None
    startAt: Optional[str] = None
    endAt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.occurredAt is not None and not isinstance(self.occurredAt, str):
            self.occurredAt = str(self.occurredAt)

        if self.startAt is not None and not isinstance(self.startAt, str):
            self.startAt = str(self.startAt)

        if self.endAt is not None and not isinstance(self.endAt, str):
            self.endAt = str(self.endAt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectRef(YAMLRoot):
    """
    Reference to a record affected by the event
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/SubjectRef"]
    class_class_curie: ClassVar[str] = "oct:core/event/SubjectRef"
    class_name: ClassVar[str] = "SubjectRef"
    class_model_uri: ClassVar[URIRef] = OCT.SubjectRef

    recordId: str = None
    recordType: Union[str, "RecordTypeEnum"] = None
    role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, str):
            self.recordId = str(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        if not isinstance(self.recordType, RecordTypeEnum):
            self.recordType = RecordTypeEnum(self.recordType)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


class EventPayload(YAMLRoot):
    """
    Abstract base for event-specific payloads
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/EventPayload"]
    class_class_curie: ClassVar[str] = "oct:core/event/EventPayload"
    class_name: ClassVar[str] = "EventPayload"
    class_model_uri: ClassVar[URIRef] = OCT.EventPayload


@dataclass(repr=False)
class StateEventPayload(EventPayload):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/StateEventPayload"]
    class_class_curie: ClassVar[str] = "oct:core/event/StateEventPayload"
    class_name: ClassVar[str] = "StateEventPayload"
    class_model_uri: ClassVar[URIRef] = OCT.StateEventPayload

    stateType: str = None
    stateValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.stateType):
            self.MissingRequiredField("stateType")
        if not isinstance(self.stateType, str):
            self.stateType = str(self.stateType)

        if self._is_empty(self.stateValue):
            self.MissingRequiredField("stateValue")
        if not isinstance(self.stateValue, str):
            self.stateValue = str(self.stateValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventSource(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/EventSource"]
    class_class_curie: ClassVar[str] = "oct:core/event/EventSource"
    class_name: ClassVar[str] = "EventSource"
    class_model_uri: ClassVar[URIRef] = OCT.EventSource

    datasetId: Optional[str] = None
    externalEventId: Optional[str] = None
    ingestedAt: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.datasetId is not None and not isinstance(self.datasetId, str):
            self.datasetId = str(self.datasetId)

        if self.externalEventId is not None and not isinstance(
            self.externalEventId, str
        ):
            self.externalEventId = str(self.externalEventId)

        if self.ingestedAt is not None and not isinstance(self.ingestedAt, str):
            self.ingestedAt = str(self.ingestedAt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(Record):
    """
    An event modifying one or more records
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["core/event/Event"]
    class_class_curie: ClassVar[str] = "oct:core/event/Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = OCT.Event

    recordId: Union[str, EventRecordId] = None
    orgId: str = None
    recordType: str = None
    eventType: Union[str, "EventType"] = None
    effectiveTime: Union[dict, EffectiveTime] = None
    subjects: Union[Union[dict, SubjectRef], list[Union[dict, SubjectRef]]] = None
    location: Optional[Union[dict, LocationRef]] = None
    payload: Optional[Union[dict, EventPayload]] = None
    notes: Optional[str] = None
    source: Optional[Union[dict, EventSource]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, EventRecordId):
            self.recordId = EventRecordId(self.recordId)

        if self._is_empty(self.recordType):
            self.MissingRequiredField("recordType")
        self.recordType = str(self.class_name)

        if self._is_empty(self.eventType):
            self.MissingRequiredField("eventType")
        if not isinstance(self.eventType, EventType):
            self.eventType = EventType(self.eventType)

        if self._is_empty(self.effectiveTime):
            self.MissingRequiredField("effectiveTime")
        if not isinstance(self.effectiveTime, EffectiveTime):
            self.effectiveTime = EffectiveTime(**as_dict(self.effectiveTime))

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        if not isinstance(self.subjects, list):
            self.subjects = [self.subjects] if self.subjects is not None else []
        self.subjects = [
            v if isinstance(v, SubjectRef) else SubjectRef(**as_dict(v))
            for v in self.subjects
        ]

        if self.location is not None and not isinstance(self.location, LocationRef):
            self.location = LocationRef(**as_dict(self.location))

        if self.payload is not None and not isinstance(self.payload, EventPayload):
            self.payload = EventPayload()

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.source is not None and not isinstance(self.source, EventSource):
            self.source = EventSource(**as_dict(self.source))

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)

    def __new__(cls, *args, **kwargs):
        type_designator = "recordType"
        if type_designator not in kwargs:
            return super().__new__(cls, *args, **kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)

            if target_cls is None:
                raise ValueError(
                    f"Wrong type designator value: class {cls.__name__} "
                    f"has no subclass with ['class_name']='{kwargs[type_designator]}'"
                )
            return super().__new__(target_cls, *args, **kwargs)


@dataclass(repr=False)
class CoralEvent(Event):
    """
    An event in the coral domain
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OCT["coral/event/CoralEvent"]
    class_class_curie: ClassVar[str] = "oct:coral/event/CoralEvent"
    class_name: ClassVar[str] = "CoralEvent"
    class_model_uri: ClassVar[URIRef] = OCT.CoralEvent

    recordId: Union[str, CoralEventRecordId] = None
    orgId: str = None
    recordType: str = None
    eventType: Union[str, "EventType"] = None
    effectiveTime: Union[dict, EffectiveTime] = None
    subjects: Union[Union[dict, SubjectRef], list[Union[dict, SubjectRef]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.recordId):
            self.MissingRequiredField("recordId")
        if not isinstance(self.recordId, CoralEventRecordId):
            self.recordId = CoralEventRecordId(self.recordId)

        super().__post_init__(**kwargs)
        if self._is_empty(self.unknown_recordType):
            self.MissingRequiredField("unknown_recordType")
        self.unknown_recordType = str(self.class_name)


# Enumerations
class GenetOriginType(EnumDefinitionImpl):
    wild_collection = PermissibleValue(text="wild_collection")
    sexual_cohort_root = PermissibleValue(text="sexual_cohort_root")
    unknown = PermissibleValue(text="unknown")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="GenetOriginType",
    )


class LocationType(EnumDefinitionImpl):
    organization = PermissibleValue(text="organization")
    site = PermissibleValue(text="site")
    container = PermissibleValue(text="container")
    position = PermissibleValue(text="position")

    _defn = EnumDefinition(
        name="LocationType",
    )


class SiteType(EnumDefinitionImpl):
    in_situ_nursery = PermissibleValue(text="in_situ_nursery")
    ex_situ_nursery = PermissibleValue(text="ex_situ_nursery")
    gene_bank = PermissibleValue(text="gene_bank")
    outplant_site = PermissibleValue(text="outplant_site")
    lab = PermissibleValue(text="lab")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="SiteType",
    )


class ContainerType(EnumDefinitionImpl):
    system = PermissibleValue(text="system")
    tank = PermissibleValue(text="tank")
    tray = PermissibleValue(text="tray")
    rack = PermissibleValue(text="rack")
    table = PermissibleValue(text="table")
    tree = PermissibleValue(text="tree")
    tree_branch = PermissibleValue(text="tree_branch")
    rebar_table = PermissibleValue(text="rebar_table")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ContainerType",
    )


class PositionType(EnumDefinitionImpl):
    slot = PermissibleValue(text="slot")
    cell = PermissibleValue(text="cell")
    quadrant = PermissibleValue(text="quadrant")
    row = PermissibleValue(text="row")
    column = PermissibleValue(text="column")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="PositionType",
    )


class InventoryUnitType(EnumDefinitionImpl):
    individual = PermissibleValue(text="individual")
    colony = PermissibleValue(text="colony")
    fragment = PermissibleValue(text="fragment")
    substrate_unit = PermissibleValue(text="substrate_unit")
    propagule_batch = PermissibleValue(text="propagule_batch")
    sample = PermissibleValue(text="sample")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="InventoryUnitType",
    )


class DevelopmentalStage(EnumDefinitionImpl):
    gamete = PermissibleValue(text="gamete")
    embryo = PermissibleValue(text="embryo")
    larva = PermissibleValue(text="larva")
    recruit = PermissibleValue(text="recruit")
    juvenile = PermissibleValue(text="juvenile")
    adult = PermissibleValue(text="adult")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DevelopmentalStage",
    )


class HealthStatus(EnumDefinitionImpl):
    healthy = PermissibleValue(text="healthy")
    stressed = PermissibleValue(text="stressed")
    bleached = PermissibleValue(text="bleached")
    diseased = PermissibleValue(text="diseased")
    dead = PermissibleValue(text="dead")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="HealthStatus",
    )


class DispositionStatus(EnumDefinitionImpl):
    available = PermissibleValue(text="available")
    reserved = PermissibleValue(text="reserved")
    quarantine = PermissibleValue(text="quarantine")
    grow_out = PermissibleValue(text="grow_out")
    broodstock = PermissibleValue(text="broodstock")
    research_only = PermissibleValue(text="research_only")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="DispositionStatus",
    )


class EventType(EnumDefinitionImpl):
    create = PermissibleValue(text="create")
    transfer = PermissibleValue(text="transfer")
    split = PermissibleValue(text="split")
    merge = PermissibleValue(text="merge")
    measurement = PermissibleValue(text="measurement")
    state = PermissibleValue(text="state")

    _defn = EnumDefinition(
        name="EventType",
    )


class RecordTypeEnum(EnumDefinitionImpl):
    Specimen = PermissibleValue(text="Specimen")
    Location = PermissibleValue(text="Location")
    Genet = PermissibleValue(text="Genet")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="RecordTypeEnum",
    )


# Slots
class slots:
    pass


slots.coralTaxonRef__speciesCode = Slot(
    uri=OCT["coral/genet/speciesCode"],
    name="coralTaxonRef__speciesCode",
    curie=OCT.curie("coral/genet/speciesCode"),
    model_uri=OCT.coralTaxonRef__speciesCode,
    domain=None,
    range=str,
    pattern=re.compile(r"^[a-z0-9]{4}$"),
)

slots.coralTaxonRef__scientificName = Slot(
    uri=OCT["coral/genet/scientificName"],
    name="coralTaxonRef__scientificName",
    curie=OCT.curie("coral/genet/scientificName"),
    model_uri=OCT.coralTaxonRef__scientificName,
    domain=None,
    range=Optional[str],
)

slots.coralTaxonRef__taxonId = Slot(
    uri=OCT["coral/genet/taxonId"],
    name="coralTaxonRef__taxonId",
    curie=OCT.curie("coral/genet/taxonId"),
    model_uri=OCT.coralTaxonRef__taxonId,
    domain=None,
    range=Optional[str],
)

slots.genetOrigin__originType = Slot(
    uri=OCT["coral/genet/originType"],
    name="genetOrigin__originType",
    curie=OCT.curie("coral/genet/originType"),
    model_uri=OCT.genetOrigin__originType,
    domain=None,
    range=Optional[Union[str, "GenetOriginType"]],
)

slots.genetOrigin__collectedAt = Slot(
    uri=OCT["coral/genet/collectedAt"],
    name="genetOrigin__collectedAt",
    curie=OCT.curie("coral/genet/collectedAt"),
    model_uri=OCT.genetOrigin__collectedAt,
    domain=None,
    range=Optional[str],
)

slots.genetOrigin__collectionLocationRef = Slot(
    uri=OCT["coral/genet/collectionLocationRef"],
    name="genetOrigin__collectionLocationRef",
    curie=OCT.curie("coral/genet/collectionLocationRef"),
    model_uri=OCT.genetOrigin__collectionLocationRef,
    domain=None,
    range=Optional[Union[dict, LocationRef]],
)

slots.genetOrigin__notes = Slot(
    uri=OCT["coral/genet/notes"],
    name="genetOrigin__notes",
    curie=OCT.curie("coral/genet/notes"),
    model_uri=OCT.genetOrigin__notes,
    domain=None,
    range=Optional[str],
)

slots.genotypingMetadata__method = Slot(
    uri=OCT["coral/genet/method"],
    name="genotypingMetadata__method",
    curie=OCT.curie("coral/genet/method"),
    model_uri=OCT.genotypingMetadata__method,
    domain=None,
    range=Optional[str],
)

slots.genotypingMetadata__lab = Slot(
    uri=OCT["coral/genet/lab"],
    name="genotypingMetadata__lab",
    curie=OCT.curie("coral/genet/lab"),
    model_uri=OCT.genotypingMetadata__lab,
    domain=None,
    range=Optional[str],
)

slots.genotypingMetadata__assayDate = Slot(
    uri=OCT["coral/genet/assayDate"],
    name="genotypingMetadata__assayDate",
    curie=OCT.curie("coral/genet/assayDate"),
    model_uri=OCT.genotypingMetadata__assayDate,
    domain=None,
    range=Optional[str],
)

slots.genotypingMetadata__associatedSequences = Slot(
    uri=OCT["coral/genet/associatedSequences"],
    name="genotypingMetadata__associatedSequences",
    curie=OCT.curie("coral/genet/associatedSequences"),
    model_uri=OCT.genotypingMetadata__associatedSequences,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.genetPedigree__damGenetId = Slot(
    uri=OCT["coral/genet/damGenetId"],
    name="genetPedigree__damGenetId",
    curie=OCT.curie("coral/genet/damGenetId"),
    model_uri=OCT.genetPedigree__damGenetId,
    domain=None,
    range=Optional[str],
)

slots.genetPedigree__sireGenetId = Slot(
    uri=OCT["coral/genet/sireGenetId"],
    name="genetPedigree__sireGenetId",
    curie=OCT.curie("coral/genet/sireGenetId"),
    model_uri=OCT.genetPedigree__sireGenetId,
    domain=None,
    range=Optional[str],
)

slots.genetPedigree__cohortId = Slot(
    uri=OCT["coral/genet/cohortId"],
    name="genetPedigree__cohortId",
    curie=OCT.curie("coral/genet/cohortId"),
    model_uri=OCT.genetPedigree__cohortId,
    domain=None,
    range=Optional[str],
)

slots.genetRecordSource__datasetId = Slot(
    uri=OCT["coral/genet/datasetId"],
    name="genetRecordSource__datasetId",
    curie=OCT.curie("coral/genet/datasetId"),
    model_uri=OCT.genetRecordSource__datasetId,
    domain=None,
    range=Optional[str],
)

slots.genetRecordSource__externalRecordId = Slot(
    uri=OCT["coral/genet/externalRecordId"],
    name="genetRecordSource__externalRecordId",
    curie=OCT.curie("coral/genet/externalRecordId"),
    model_uri=OCT.genetRecordSource__externalRecordId,
    domain=None,
    range=Optional[str],
)

slots.genetRecordSource__ingestedAt = Slot(
    uri=OCT["coral/genet/ingestedAt"],
    name="genetRecordSource__ingestedAt",
    curie=OCT.curie("coral/genet/ingestedAt"),
    model_uri=OCT.genetRecordSource__ingestedAt,
    domain=None,
    range=Optional[str],
)

slots.genetRecord__recordType = Slot(
    uri=RDF.type,
    name="genetRecord__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.genetRecord__recordType,
    domain=None,
    range=str,
    pattern=re.compile(r"^Genet$"),
)

slots.genetRecord__createdAt = Slot(
    uri=OCT["coral/genet/createdAt"],
    name="genetRecord__createdAt",
    curie=OCT.curie("coral/genet/createdAt"),
    model_uri=OCT.genetRecord__createdAt,
    domain=None,
    range=str,
)

slots.genetRecord__updatedAt = Slot(
    uri=OCT["coral/genet/updatedAt"],
    name="genetRecord__updatedAt",
    curie=OCT.curie("coral/genet/updatedAt"),
    model_uri=OCT.genetRecord__updatedAt,
    domain=None,
    range=Optional[str],
)

slots.genetRecord__taxon = Slot(
    uri=OCT["coral/genet/taxon"],
    name="genetRecord__taxon",
    curie=OCT.curie("coral/genet/taxon"),
    model_uri=OCT.genetRecord__taxon,
    domain=None,
    range=Union[dict, CoralTaxonRef],
)

slots.genetRecord__genetCode = Slot(
    uri=OCT["coral/genet/genetCode"],
    name="genetRecord__genetCode",
    curie=OCT.curie("coral/genet/genetCode"),
    model_uri=OCT.genetRecord__genetCode,
    domain=None,
    range=str,
)

slots.genetRecord__origin = Slot(
    uri=OCT["coral/genet/origin"],
    name="genetRecord__origin",
    curie=OCT.curie("coral/genet/origin"),
    model_uri=OCT.genetRecord__origin,
    domain=None,
    range=Optional[Union[dict, GenetOrigin]],
)

slots.genetRecord__genotyping = Slot(
    uri=OCT["coral/genet/genotyping"],
    name="genetRecord__genotyping",
    curie=OCT.curie("coral/genet/genotyping"),
    model_uri=OCT.genetRecord__genotyping,
    domain=None,
    range=Optional[Union[dict, GenotypingMetadata]],
)

slots.genetRecord__pedigree = Slot(
    uri=OCT["coral/genet/pedigree"],
    name="genetRecord__pedigree",
    curie=OCT.curie("coral/genet/pedigree"),
    model_uri=OCT.genetRecord__pedigree,
    domain=None,
    range=Optional[Union[dict, GenetPedigree]],
)

slots.genetRecord__notes = Slot(
    uri=OCT["coral/genet/notes"],
    name="genetRecord__notes",
    curie=OCT.curie("coral/genet/notes"),
    model_uri=OCT.genetRecord__notes,
    domain=None,
    range=Optional[str],
)

slots.genetRecord__source = Slot(
    uri=OCT["coral/genet/source"],
    name="genetRecord__source",
    curie=OCT.curie("coral/genet/source"),
    model_uri=OCT.genetRecord__source,
    domain=None,
    range=Optional[Union[dict, GenetRecordSource]],
)

slots.geoPoint__decimalLatitude = Slot(
    uri=OCT["core/types/decimalLatitude"],
    name="geoPoint__decimalLatitude",
    curie=OCT.curie("core/types/decimalLatitude"),
    model_uri=OCT.geoPoint__decimalLatitude,
    domain=None,
    range=float,
)

slots.geoPoint__decimalLongitude = Slot(
    uri=OCT["core/types/decimalLongitude"],
    name="geoPoint__decimalLongitude",
    curie=OCT.curie("core/types/decimalLongitude"),
    model_uri=OCT.geoPoint__decimalLongitude,
    domain=None,
    range=float,
)

slots.geoPoint__geodeticDatum = Slot(
    uri=OCT["core/types/geodeticDatum"],
    name="geoPoint__geodeticDatum",
    curie=OCT.curie("core/types/geodeticDatum"),
    model_uri=OCT.geoPoint__geodeticDatum,
    domain=None,
    range=Optional[str],
)

slots.geoPoint__coordinateUncertaintyMeters = Slot(
    uri=OCT["core/types/coordinateUncertaintyMeters"],
    name="geoPoint__coordinateUncertaintyMeters",
    curie=OCT.curie("core/types/coordinateUncertaintyMeters"),
    model_uri=OCT.geoPoint__coordinateUncertaintyMeters,
    domain=None,
    range=Optional[float],
)

slots.measureValue__value = Slot(
    uri=OCT["core/types/value"],
    name="measureValue__value",
    curie=OCT.curie("core/types/value"),
    model_uri=OCT.measureValue__value,
    domain=None,
    range=float,
)

slots.measureValue__unit = Slot(
    uri=OCT["core/types/unit"],
    name="measureValue__unit",
    curie=OCT.curie("core/types/unit"),
    model_uri=OCT.measureValue__unit,
    domain=None,
    range=str,
)

slots.measureValue__method = Slot(
    uri=OCT["core/types/method"],
    name="measureValue__method",
    curie=OCT.curie("core/types/method"),
    model_uri=OCT.measureValue__method,
    domain=None,
    range=Optional[str],
)

slots.entityRef__id = Slot(
    uri=OCT["core/types/id"],
    name="entityRef__id",
    curie=OCT.curie("core/types/id"),
    model_uri=OCT.entityRef__id,
    domain=None,
    range=str,
)

slots.entityRef__type = Slot(
    uri=OCT["core/types/type"],
    name="entityRef__type",
    curie=OCT.curie("core/types/type"),
    model_uri=OCT.entityRef__type,
    domain=None,
    range=Optional[str],
)

slots.entityRef__label = Slot(
    uri=OCT["core/types/label"],
    name="entityRef__label",
    curie=OCT.curie("core/types/label"),
    model_uri=OCT.entityRef__label,
    domain=None,
    range=Optional[str],
)

slots.taxonRef__name = Slot(
    uri=OCT["core/types/name"],
    name="taxonRef__name",
    curie=OCT.curie("core/types/name"),
    model_uri=OCT.taxonRef__name,
    domain=None,
    range=str,
)

slots.taxonRef__taxonId = Slot(
    uri=OCT["core/types/taxonId"],
    name="taxonRef__taxonId",
    curie=OCT.curie("core/types/taxonId"),
    model_uri=OCT.taxonRef__taxonId,
    domain=None,
    range=Optional[str],
)

slots.taxonRef__rank = Slot(
    uri=OCT["core/types/rank"],
    name="taxonRef__rank",
    curie=OCT.curie("core/types/rank"),
    model_uri=OCT.taxonRef__rank,
    domain=None,
    range=Optional[str],
)

slots.record__recordId = Slot(
    uri=OCT["core/record/recordId"],
    name="record__recordId",
    curie=OCT.curie("core/record/recordId"),
    model_uri=OCT.record__recordId,
    domain=None,
    range=URIRef,
)

slots.record__recordType = Slot(
    uri=OCT["core/record/recordType"],
    name="record__recordType",
    curie=OCT.curie("core/record/recordType"),
    model_uri=OCT.record__recordType,
    domain=None,
    range=str,
)

slots.record__orgId = Slot(
    uri=OCT["core/record/orgId"],
    name="record__orgId",
    curie=OCT.curie("core/record/orgId"),
    model_uri=OCT.record__orgId,
    domain=None,
    range=str,
)

slots.record__createdAt = Slot(
    uri=OCT["core/record/createdAt"],
    name="record__createdAt",
    curie=OCT.curie("core/record/createdAt"),
    model_uri=OCT.record__createdAt,
    domain=None,
    range=Optional[str],
)

slots.record__createdBy = Slot(
    uri=OCT["core/record/createdBy"],
    name="record__createdBy",
    curie=OCT.curie("core/record/createdBy"),
    model_uri=OCT.record__createdBy,
    domain=None,
    range=Optional[str],
)

slots.record__updatedAt = Slot(
    uri=OCT["core/record/updatedAt"],
    name="record__updatedAt",
    curie=OCT.curie("core/record/updatedAt"),
    model_uri=OCT.record__updatedAt,
    domain=None,
    range=Optional[str],
)

slots.record__updatedBy = Slot(
    uri=OCT["core/record/updatedBy"],
    name="record__updatedBy",
    curie=OCT.curie("core/record/updatedBy"),
    model_uri=OCT.record__updatedBy,
    domain=None,
    range=Optional[str],
)

slots.person__recordType = Slot(
    uri=RDF.type,
    name="person__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.person__recordType,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^Person$"),
)

slots.person__name = Slot(
    uri=OCT["core/person/name"],
    name="person__name",
    curie=OCT.curie("core/person/name"),
    model_uri=OCT.person__name,
    domain=None,
    range=str,
)

slots.person__email = Slot(
    uri=OCT["core/person/email"],
    name="person__email",
    curie=OCT.curie("core/person/email"),
    model_uri=OCT.person__email,
    domain=None,
    range=str,
)

slots.person__imageUrl = Slot(
    uri=OCT["core/person/imageUrl"],
    name="person__imageUrl",
    curie=OCT.curie("core/person/imageUrl"),
    model_uri=OCT.person__imageUrl,
    domain=None,
    range=Optional[str],
)

slots.organization__recordType = Slot(
    uri=RDF.type,
    name="organization__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.organization__recordType,
    domain=None,
    range=Optional[str],
    pattern=re.compile(r"^Organization$"),
)

slots.organization__name = Slot(
    uri=OCT["core/organization/name"],
    name="organization__name",
    curie=OCT.curie("core/organization/name"),
    model_uri=OCT.organization__name,
    domain=None,
    range=str,
)

slots.organization__domain = Slot(
    uri=OCT["core/organization/domain"],
    name="organization__domain",
    curie=OCT.curie("core/organization/domain"),
    model_uri=OCT.organization__domain,
    domain=None,
    range=Optional[str],
)

slots.organization__supportedSiteTypes = Slot(
    uri=OCT["core/organization/supportedSiteTypes"],
    name="organization__supportedSiteTypes",
    curie=OCT.curie("core/organization/supportedSiteTypes"),
    model_uri=OCT.organization__supportedSiteTypes,
    domain=None,
    range=Optional[Union[Union[str, "SiteType"], list[Union[str, "SiteType"]]]],
)

slots.organization__supportedSpecies = Slot(
    uri=OCT["core/organization/supportedSpecies"],
    name="organization__supportedSpecies",
    curie=OCT.curie("core/organization/supportedSpecies"),
    model_uri=OCT.organization__supportedSpecies,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.locationRef__locationId = Slot(
    uri=OCT["core/location/locationId"],
    name="locationRef__locationId",
    curie=OCT.curie("core/location/locationId"),
    model_uri=OCT.locationRef__locationId,
    domain=None,
    range=str,
)

slots.locationRef__locationType = Slot(
    uri=OCT["core/location/locationType"],
    name="locationRef__locationType",
    curie=OCT.curie("core/location/locationType"),
    model_uri=OCT.locationRef__locationType,
    domain=None,
    range=Optional[Union[str, "LocationType"]],
)

slots.locationRef__label = Slot(
    uri=OCT["core/location/label"],
    name="locationRef__label",
    curie=OCT.curie("core/location/label"),
    model_uri=OCT.locationRef__label,
    domain=None,
    range=Optional[str],
)

slots.parentLocationRef__siteType = Slot(
    uri=OCT["core/location/siteType"],
    name="parentLocationRef__siteType",
    curie=OCT.curie("core/location/siteType"),
    model_uri=OCT.parentLocationRef__siteType,
    domain=None,
    range=Optional[Union[str, "SiteType"]],
)

slots.parentLocationRef__containerType = Slot(
    uri=OCT["core/location/containerType"],
    name="parentLocationRef__containerType",
    curie=OCT.curie("core/location/containerType"),
    model_uri=OCT.parentLocationRef__containerType,
    domain=None,
    range=Optional[Union[str, "ContainerType"]],
)

slots.parentLocationRef__name = Slot(
    uri=OCT["core/location/name"],
    name="parentLocationRef__name",
    curie=OCT.curie("core/location/name"),
    model_uri=OCT.parentLocationRef__name,
    domain=None,
    range=Optional[str],
)

slots.locationRecord__recordType = Slot(
    uri=RDF.type,
    name="locationRecord__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.locationRecord__recordType,
    domain=None,
    range=str,
    pattern=re.compile(r"^Location$"),
)

slots.locationRecord__locationType = Slot(
    uri=OCT["core/location/locationType"],
    name="locationRecord__locationType",
    curie=OCT.curie("core/location/locationType"),
    model_uri=OCT.locationRecord__locationType,
    domain=None,
    range=Union[str, "LocationType"],
)

slots.locationRecord__name = Slot(
    uri=OCT["core/location/name"],
    name="locationRecord__name",
    curie=OCT.curie("core/location/name"),
    model_uri=OCT.locationRecord__name,
    domain=None,
    range=str,
)

slots.locationRecord__parentLocationRef = Slot(
    uri=OCT["core/location/parentLocationRef"],
    name="locationRecord__parentLocationRef",
    curie=OCT.curie("core/location/parentLocationRef"),
    model_uri=OCT.locationRecord__parentLocationRef,
    domain=None,
    range=Optional[Union[dict, ParentLocationRef]],
)

slots.locationRecord__siteType = Slot(
    uri=OCT["core/location/siteType"],
    name="locationRecord__siteType",
    curie=OCT.curie("core/location/siteType"),
    model_uri=OCT.locationRecord__siteType,
    domain=None,
    range=Optional[Union[str, "SiteType"]],
)

slots.locationRecord__containerType = Slot(
    uri=OCT["core/location/containerType"],
    name="locationRecord__containerType",
    curie=OCT.curie("core/location/containerType"),
    model_uri=OCT.locationRecord__containerType,
    domain=None,
    range=Optional[Union[str, "ContainerType"]],
)

slots.locationRecord__positionType = Slot(
    uri=OCT["core/location/positionType"],
    name="locationRecord__positionType",
    curie=OCT.curie("core/location/positionType"),
    model_uri=OCT.locationRecord__positionType,
    domain=None,
    range=Optional[Union[str, "PositionType"]],
)

slots.locationRecord__geo = Slot(
    uri=OCT["core/location/geo"],
    name="locationRecord__geo",
    curie=OCT.curie("core/location/geo"),
    model_uri=OCT.locationRecord__geo,
    domain=None,
    range=Optional[Union[dict, GeoPoint]],
)

slots.locationRecord__depth = Slot(
    uri=OCT["core/location/depth"],
    name="locationRecord__depth",
    curie=OCT.curie("core/location/depth"),
    model_uri=OCT.locationRecord__depth,
    domain=None,
    range=Optional[Union[dict, MeasureValue]],
)

slots.locationRecord__notes = Slot(
    uri=OCT["core/location/notes"],
    name="locationRecord__notes",
    curie=OCT.curie("core/location/notes"),
    model_uri=OCT.locationRecord__notes,
    domain=None,
    range=Optional[str],
)

slots.locationRecord__codes = Slot(
    uri=OCT["core/location/codes"],
    name="locationRecord__codes",
    curie=OCT.curie("core/location/codes"),
    model_uri=OCT.locationRecord__codes,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.quantity__count = Slot(
    uri=OCT["core/specimen/count"],
    name="quantity__count",
    curie=OCT.curie("core/specimen/count"),
    model_uri=OCT.quantity__count,
    domain=None,
    range=float,
)

slots.quantity__countUncertainty = Slot(
    uri=OCT["core/specimen/countUncertainty"],
    name="quantity__countUncertainty",
    curie=OCT.curie("core/specimen/countUncertainty"),
    model_uri=OCT.quantity__countUncertainty,
    domain=None,
    range=Optional[float],
)

slots.quantity__surfaceArea = Slot(
    uri=OCT["core/specimen/surfaceArea"],
    name="quantity__surfaceArea",
    curie=OCT.curie("core/specimen/surfaceArea"),
    model_uri=OCT.quantity__surfaceArea,
    domain=None,
    range=Optional[Union[dict, MeasureValue]],
)

slots.quantity__volume = Slot(
    uri=OCT["core/specimen/volume"],
    name="quantity__volume",
    curie=OCT.curie("core/specimen/volume"),
    model_uri=OCT.quantity__volume,
    domain=None,
    range=Optional[Union[dict, MeasureValue]],
)

slots.quantity__biomass = Slot(
    uri=OCT["core/specimen/biomass"],
    name="quantity__biomass",
    curie=OCT.curie("core/specimen/biomass"),
    model_uri=OCT.quantity__biomass,
    domain=None,
    range=Optional[Union[dict, MeasureValue]],
)

slots.quantity__linearSize = Slot(
    uri=OCT["core/specimen/linearSize"],
    name="quantity__linearSize",
    curie=OCT.curie("core/specimen/linearSize"),
    model_uri=OCT.quantity__linearSize,
    domain=None,
    range=Optional[Union[dict, MeasureValue]],
)

slots.specimenState__disposition = Slot(
    uri=OCT["core/specimen/disposition"],
    name="specimenState__disposition",
    curie=OCT.curie("core/specimen/disposition"),
    model_uri=OCT.specimenState__disposition,
    domain=None,
    range=Optional[Union[str, "DispositionStatus"]],
)

slots.specimenState__health = Slot(
    uri=OCT["core/specimen/health"],
    name="specimenState__health",
    curie=OCT.curie("core/specimen/health"),
    model_uri=OCT.specimenState__health,
    domain=None,
    range=Optional[Union[str, "HealthStatus"]],
)

slots.specimenState__readyForPropagation = Slot(
    uri=OCT["core/specimen/readyForPropagation"],
    name="specimenState__readyForPropagation",
    curie=OCT.curie("core/specimen/readyForPropagation"),
    model_uri=OCT.specimenState__readyForPropagation,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.specimenState__readyForOutplant = Slot(
    uri=OCT["core/specimen/readyForOutplant"],
    name="specimenState__readyForOutplant",
    curie=OCT.curie("core/specimen/readyForOutplant"),
    model_uri=OCT.specimenState__readyForOutplant,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.specimenRecordSource__datasetId = Slot(
    uri=OCT["core/specimen/datasetId"],
    name="specimenRecordSource__datasetId",
    curie=OCT.curie("core/specimen/datasetId"),
    model_uri=OCT.specimenRecordSource__datasetId,
    domain=None,
    range=Optional[str],
)

slots.specimenRecordSource__externalRecordId = Slot(
    uri=OCT["core/specimen/externalRecordId"],
    name="specimenRecordSource__externalRecordId",
    curie=OCT.curie("core/specimen/externalRecordId"),
    model_uri=OCT.specimenRecordSource__externalRecordId,
    domain=None,
    range=Optional[str],
)

slots.specimenRecordSource__ingestedAt = Slot(
    uri=OCT["core/specimen/ingestedAt"],
    name="specimenRecordSource__ingestedAt",
    curie=OCT.curie("core/specimen/ingestedAt"),
    model_uri=OCT.specimenRecordSource__ingestedAt,
    domain=None,
    range=Optional[str],
)

slots.specimenRecord__recordType = Slot(
    uri=RDF.type,
    name="specimenRecord__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.specimenRecord__recordType,
    domain=None,
    range=str,
    pattern=re.compile(r"^Specimen$"),
)

slots.specimenRecord__asOf = Slot(
    uri=OCT["core/specimen/asOf"],
    name="specimenRecord__asOf",
    curie=OCT.curie("core/specimen/asOf"),
    model_uri=OCT.specimenRecord__asOf,
    domain=None,
    range=str,
)

slots.specimenRecord__taxon = Slot(
    uri=OCT["core/specimen/taxon"],
    name="specimenRecord__taxon",
    curie=OCT.curie("core/specimen/taxon"),
    model_uri=OCT.specimenRecord__taxon,
    domain=None,
    range=Union[dict, TaxonRef],
)

slots.specimenRecord__geneticGroupRef = Slot(
    uri=OCT["core/specimen/geneticGroupRef"],
    name="specimenRecord__geneticGroupRef",
    curie=OCT.curie("core/specimen/geneticGroupRef"),
    model_uri=OCT.specimenRecord__geneticGroupRef,
    domain=None,
    range=Optional[Union[dict, EntityRef]],
)

slots.specimenRecord__inventoryUnitType = Slot(
    uri=OCT["core/specimen/inventoryUnitType"],
    name="specimenRecord__inventoryUnitType",
    curie=OCT.curie("core/specimen/inventoryUnitType"),
    model_uri=OCT.specimenRecord__inventoryUnitType,
    domain=None,
    range=Union[str, "InventoryUnitType"],
)

slots.specimenRecord__developmentalStage = Slot(
    uri=OCT["core/specimen/developmentalStage"],
    name="specimenRecord__developmentalStage",
    curie=OCT.curie("core/specimen/developmentalStage"),
    model_uri=OCT.specimenRecord__developmentalStage,
    domain=None,
    range=Optional[Union[str, "DevelopmentalStage"]],
)

slots.specimenRecord__quantity = Slot(
    uri=OCT["core/specimen/quantity"],
    name="specimenRecord__quantity",
    curie=OCT.curie("core/specimen/quantity"),
    model_uri=OCT.specimenRecord__quantity,
    domain=None,
    range=Union[dict, Quantity],
)

slots.specimenRecord__locationRef = Slot(
    uri=OCT["core/specimen/locationRef"],
    name="specimenRecord__locationRef",
    curie=OCT.curie("core/specimen/locationRef"),
    model_uri=OCT.specimenRecord__locationRef,
    domain=None,
    range=Union[dict, LocationRef],
)

slots.specimenRecord__state = Slot(
    uri=OCT["core/specimen/state"],
    name="specimenRecord__state",
    curie=OCT.curie("core/specimen/state"),
    model_uri=OCT.specimenRecord__state,
    domain=None,
    range=Optional[Union[dict, SpecimenState]],
)

slots.specimenRecord__tags = Slot(
    uri=OCT["core/specimen/tags"],
    name="specimenRecord__tags",
    curie=OCT.curie("core/specimen/tags"),
    model_uri=OCT.specimenRecord__tags,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.specimenRecord__notes = Slot(
    uri=OCT["core/specimen/notes"],
    name="specimenRecord__notes",
    curie=OCT.curie("core/specimen/notes"),
    model_uri=OCT.specimenRecord__notes,
    domain=None,
    range=Optional[str],
)

slots.specimenRecord__source = Slot(
    uri=OCT["core/specimen/source"],
    name="specimenRecord__source",
    curie=OCT.curie("core/specimen/source"),
    model_uri=OCT.specimenRecord__source,
    domain=None,
    range=Optional[Union[dict, SpecimenRecordSource]],
)

slots.effectiveTime__occurredAt = Slot(
    uri=OCT["core/event/occurredAt"],
    name="effectiveTime__occurredAt",
    curie=OCT.curie("core/event/occurredAt"),
    model_uri=OCT.effectiveTime__occurredAt,
    domain=None,
    range=Optional[str],
)

slots.effectiveTime__startAt = Slot(
    uri=OCT["core/event/startAt"],
    name="effectiveTime__startAt",
    curie=OCT.curie("core/event/startAt"),
    model_uri=OCT.effectiveTime__startAt,
    domain=None,
    range=Optional[str],
)

slots.effectiveTime__endAt = Slot(
    uri=OCT["core/event/endAt"],
    name="effectiveTime__endAt",
    curie=OCT.curie("core/event/endAt"),
    model_uri=OCT.effectiveTime__endAt,
    domain=None,
    range=Optional[str],
)

slots.subjectRef__recordId = Slot(
    uri=OCT["core/event/recordId"],
    name="subjectRef__recordId",
    curie=OCT.curie("core/event/recordId"),
    model_uri=OCT.subjectRef__recordId,
    domain=None,
    range=str,
)

slots.subjectRef__recordType = Slot(
    uri=OCT["core/event/recordType"],
    name="subjectRef__recordType",
    curie=OCT.curie("core/event/recordType"),
    model_uri=OCT.subjectRef__recordType,
    domain=None,
    range=Union[str, "RecordTypeEnum"],
)

slots.subjectRef__role = Slot(
    uri=OCT["core/event/role"],
    name="subjectRef__role",
    curie=OCT.curie("core/event/role"),
    model_uri=OCT.subjectRef__role,
    domain=None,
    range=Optional[str],
)

slots.stateEventPayload__stateType = Slot(
    uri=OCT["core/event/stateType"],
    name="stateEventPayload__stateType",
    curie=OCT.curie("core/event/stateType"),
    model_uri=OCT.stateEventPayload__stateType,
    domain=None,
    range=str,
)

slots.stateEventPayload__stateValue = Slot(
    uri=OCT["core/event/stateValue"],
    name="stateEventPayload__stateValue",
    curie=OCT.curie("core/event/stateValue"),
    model_uri=OCT.stateEventPayload__stateValue,
    domain=None,
    range=str,
)

slots.eventSource__datasetId = Slot(
    uri=OCT["core/event/datasetId"],
    name="eventSource__datasetId",
    curie=OCT.curie("core/event/datasetId"),
    model_uri=OCT.eventSource__datasetId,
    domain=None,
    range=Optional[str],
)

slots.eventSource__externalEventId = Slot(
    uri=OCT["core/event/externalEventId"],
    name="eventSource__externalEventId",
    curie=OCT.curie("core/event/externalEventId"),
    model_uri=OCT.eventSource__externalEventId,
    domain=None,
    range=Optional[str],
)

slots.eventSource__ingestedAt = Slot(
    uri=OCT["core/event/ingestedAt"],
    name="eventSource__ingestedAt",
    curie=OCT.curie("core/event/ingestedAt"),
    model_uri=OCT.eventSource__ingestedAt,
    domain=None,
    range=Optional[str],
)

slots.event__recordType = Slot(
    uri=RDF.type,
    name="event__recordType",
    curie=RDF.curie("type"),
    model_uri=OCT.event__recordType,
    domain=None,
    range=str,
    pattern=re.compile(r"^Event$"),
)

slots.event__eventType = Slot(
    uri=OCT["core/event/eventType"],
    name="event__eventType",
    curie=OCT.curie("core/event/eventType"),
    model_uri=OCT.event__eventType,
    domain=None,
    range=Union[str, "EventType"],
)

slots.event__effectiveTime = Slot(
    uri=OCT["core/event/effectiveTime"],
    name="event__effectiveTime",
    curie=OCT.curie("core/event/effectiveTime"),
    model_uri=OCT.event__effectiveTime,
    domain=None,
    range=Union[dict, EffectiveTime],
)

slots.event__subjects = Slot(
    uri=OCT["core/event/subjects"],
    name="event__subjects",
    curie=OCT.curie("core/event/subjects"),
    model_uri=OCT.event__subjects,
    domain=None,
    range=Union[Union[dict, SubjectRef], list[Union[dict, SubjectRef]]],
)

slots.event__location = Slot(
    uri=OCT["core/event/location"],
    name="event__location",
    curie=OCT.curie("core/event/location"),
    model_uri=OCT.event__location,
    domain=None,
    range=Optional[Union[dict, LocationRef]],
)

slots.event__payload = Slot(
    uri=OCT["core/event/payload"],
    name="event__payload",
    curie=OCT.curie("core/event/payload"),
    model_uri=OCT.event__payload,
    domain=None,
    range=Optional[Union[dict, EventPayload]],
)

slots.event__notes = Slot(
    uri=OCT["core/event/notes"],
    name="event__notes",
    curie=OCT.curie("core/event/notes"),
    model_uri=OCT.event__notes,
    domain=None,
    range=Optional[str],
)

slots.event__source = Slot(
    uri=OCT["core/event/source"],
    name="event__source",
    curie=OCT.curie("core/event/source"),
    model_uri=OCT.event__source,
    domain=None,
    range=Optional[Union[dict, EventSource]],
)

slots.CoralSpecimenRecord_taxon = Slot(
    uri=OCT.taxon,
    name="CoralSpecimenRecord_taxon",
    curie=OCT.curie("taxon"),
    model_uri=OCT.CoralSpecimenRecord_taxon,
    domain=CoralSpecimenRecord,
    range=Union[dict, CoralTaxonRef],
)

slots.CoralSpecimenRecord_geneticGroupRef = Slot(
    uri=OCT.geneticGroupRef,
    name="CoralSpecimenRecord_geneticGroupRef",
    curie=OCT.curie("geneticGroupRef"),
    model_uri=OCT.CoralSpecimenRecord_geneticGroupRef,
    domain=CoralSpecimenRecord,
    range=Optional[Union[str, GenetRecordRecordId]],
)

slots.CoralSpecimenRecord_inventoryUnitType = Slot(
    uri=OCT.inventoryUnitType,
    name="CoralSpecimenRecord_inventoryUnitType",
    curie=OCT.curie("inventoryUnitType"),
    model_uri=OCT.CoralSpecimenRecord_inventoryUnitType,
    domain=CoralSpecimenRecord,
    range=Union[str, "InventoryUnitType"],
)
