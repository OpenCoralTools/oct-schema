export type RecordRecordId = string;
export type PersonRecordId = string;
export type LocationRecordRecordId = string;
export type OrganizationRecordId = string;
export type SpecimenRecordRecordId = string;
export type EventRecordId = string;
export type GenetRecordRecordId = string;
export type CoralLocationRecordRecordId = string;
export type CoralSpecimenRecordRecordId = string;
export type CoralEventRecordId = string;

export enum LocationType {

    organization = "organization",
    site = "site",
    container = "container",
    position = "position",
};

export enum SiteType {

    in_situ_nursery = "in_situ_nursery",
    ex_situ_nursery = "ex_situ_nursery",
    gene_bank = "gene_bank",
    outplant_site = "outplant_site",
    lab = "lab",
    other = "other",
};

export enum ContainerType {

    system = "system",
    tank = "tank",
    tray = "tray",
    rack = "rack",
    table = "table",
    tree = "tree",
    tree_branch = "tree_branch",
    rebar_table = "rebar_table",
    other = "other",
};

export enum PositionType {

    slot = "slot",
    cell = "cell",
    quadrant = "quadrant",
    row = "row",
    column = "column",
    other = "other",
};

export enum InventoryUnitType {

    individual = "individual",
    colony = "colony",
    fragment = "fragment",
    substrate_unit = "substrate_unit",
    propagule_batch = "propagule_batch",
    sample = "sample",
    unknown = "unknown",
};

export enum DevelopmentalStage {

    gamete = "gamete",
    embryo = "embryo",
    larva = "larva",
    recruit = "recruit",
    juvenile = "juvenile",
    adult = "adult",
    unknown = "unknown",
};

export enum HealthStatus {

    healthy = "healthy",
    stressed = "stressed",
    bleached = "bleached",
    diseased = "diseased",
    dead = "dead",
    unknown = "unknown",
};

export enum DispositionStatus {

    available = "available",
    reserved = "reserved",
    quarantine = "quarantine",
    grow_out = "grow_out",
    broodstock = "broodstock",
    research_only = "research_only",
    unknown = "unknown",
};

export enum EventType {

    create = "create",
    transfer = "transfer",
    split = "split",
    merge = "merge",
    measurement = "measurement",
    state = "state",
};

export enum RecordType {

    specimen = "specimen",
    event = "event",
    location = "location",
    genet = "genet",
    other = "other",
};

export enum GenetOriginType {

    wild_collection = "wild_collection",
    sexual_cohort_root = "sexual_cohort_root",
    unknown = "unknown",
    other = "other",
};


/**
 * A geographic coordinate
 */
export interface GeoPoint {
    decimalLatitude: number,
    decimalLongitude: number,
    geodeticDatum?: string,
    coordinateUncertaintyMeters?: number,
}


/**
 * A measured value with a unit
 */
export interface MeasureValue {
    value: number,
    /** UCUM unit code recommended */
    unit: string,
    /** Method used to obtain the measurement */
    method?: string,
}


/**
 * A generic reference to another entity
 */
export interface EntityRef {
    id: string,
    type?: string,
    label?: string,
}


/**
 * A reference to a taxonomic entity
 */
export interface TaxonRef {
    /** Scientific name or label */
    name: string,
    /** External identifier (e.g. LSID) */
    taxonId?: string,
    rank?: string,
}


/**
 * Base class for all authoritative records
 */
export interface Record {
    recordId: string,
    recordType: string,
    /** The organization that owns/issued this record */
    orgId: string,
    createdAt?: string,
    /** ID of the Agent (Person/Service) who created this */
    createdBy?: string,
    updatedAt?: string,
    updatedBy?: string,
}


/**
 * Represents a human user or agent
 */
export interface Person extends Record {
    recordType?: string,
    name: string,
    email: string,
    imageUrl?: string,
}


/**
 * A lightweight reference to a location
 */
export interface LocationRef {
    locationId: string,
    locationType?: string,
    label?: string,
}


/**
 * Reference to a parent location with structural type information
 */
export interface ParentLocationRef extends LocationRef {
    siteType?: string,
    containerType?: string,
    name?: string,
}


/**
 * A record representing a physical or logical location
 */
export interface LocationRecord extends Record {
    recordType: string,
    locationType: string,
    name: string,
    parentLocationRef?: ParentLocationRef,
    siteType?: string,
    containerType?: string,
    positionType?: string,
    geo?: GeoPoint,
    depth?: MeasureValue,
    notes?: string,
    codes?: string[],
}


/**
 * Represents an organization
 */
export interface Organization extends Record {
    recordType?: string,
    name: string,
    /** Domain name associated with the organization */
    domain?: string,
    supportedSiteTypes?: string,
    supportedSpecies?: string[],
}


/**
 * Quantification of the specimen (count, size, etc.)
 */
export interface Quantity {
    count: number,
    countUncertainty?: number,
    surfaceArea?: MeasureValue,
    volume?: MeasureValue,
    biomass?: MeasureValue,
    linearSize?: MeasureValue,
}


/**
 * Derived state of the specimen
 */
export interface SpecimenState {
    disposition?: string,
    health?: string,
    readyForPropagation?: boolean,
    readyForOutplant?: boolean,
}



export interface SpecimenRecordSource {
    datasetId?: string,
    externalRecordId?: string,
    ingestedAt?: string,
}


/**
 * A record representing a biological specimen or group
 */
export interface SpecimenRecord extends Record {
    recordType: string,
    asOf: string,
    taxon: TaxonRef,
    geneticGroupRef?: EntityRef,
    inventoryUnitType: string,
    developmentalStage?: string,
    quantity: Quantity,
    locationRef: LocationRef,
    state?: SpecimenState,
    tags?: string[],
    notes?: string,
    source?: SpecimenRecordSource,
}


/**
 * Time of the event (moment or interval)
 */
export interface EffectiveTime {
    occurredAt?: string,
    startAt?: string,
    endAt?: string,
}


/**
 * Reference to a record affected by the event
 */
export interface SubjectRef {
    recordId: string,
    recordType: string,
    /** Role in the event (source, destination, etc.) */
    role?: string,
}


/**
 * Abstract base for event-specific payloads
 */
export interface EventPayload {
}



export interface StateEventPayload extends EventPayload {
    /** e.g. health, disposition */
    stateType: string,
    stateValue: string,
}



export interface EventSource {
    datasetId?: string,
    externalEventId?: string,
    ingestedAt?: string,
}


/**
 * An event modifying one or more records
 */
export interface Event extends Record {
    recordType: string,
    eventType: string,
    effectiveTime: EffectiveTime,
    subjects: SubjectRef[],
    /** Context location for the event */
    location?: LocationRef,
    /** Type-specific event data */
    payload?: EventPayload,
    notes?: string,
    source?: EventSource,
}


/**
 * Coral-specific taxon reference with species code
 */
export interface CoralTaxonRef {
    /** Registry-backed 4-char species code (e.g., 'apal') */
    speciesCode: string,
    scientificName?: string,
    taxonId?: string,
}



export interface GenetOrigin {
    originType?: string,
    collectedAt?: string,
    collectionLocationRef?: LocationRef,
    notes?: string,
}



export interface GenotypingMetadata {
    /** e.g. SNP panel name, microsatellites */
    method?: string,
    lab?: string,
    assayDate?: string,
    associatedSequences?: string[],
}



export interface GenetPedigree {
    damGenetId?: string,
    sireGenetId?: string,
    cohortId?: string,
}



export interface GenetRecordSource {
    datasetId?: string,
    externalRecordId?: string,
    ingestedAt?: string,
}


/**
 * Coral-specific genet record (clonal lineage)
 */
export interface GenetRecord extends Record {
    recordType: string,
    createdAt: string,
    updatedAt?: string,
    taxon: CoralTaxonRef,
    /** Program-level genet identifier */
    genetCode: string,
    origin?: GenetOrigin,
    genotyping?: GenotypingMetadata,
    pedigree?: GenetPedigree,
    notes?: string,
    source?: GenetRecordSource,
}


/**
 * A location record used in coral restoration (extensible placeholder)
 */
export interface CoralLocationRecord extends LocationRecord {
}


/**
 * A specimen record representing a coral
 */
export interface CoralSpecimenRecord extends SpecimenRecord {
}


/**
 * An event in the coral domain
 */
export interface CoralEvent extends Event {
}
