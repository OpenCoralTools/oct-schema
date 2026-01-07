export type RecordId = string;
export type InventoryRecordId = string;
export type OrganizationId = string;
export type SiteId = string;
export type LocationId = string;
export type GenetId = string;
export type CoralId = string;
export type SpeciesId = string;
export type PersonId = string;
export type EventId = string;
export type SpeciesRegisterEntryCode = string;
export type OrganizationRegisterEntryOrgId = string;

export enum CoralSize {

    xs = "xs",
    s = "s",
    m = "m",
    l = "l",
    xl = "xl",
};

export enum ModelType {

    user = "user",
    organization = "organization",
    site = "site",
    group = "group",
    coral = "coral",
    genet = "genet",
    recordType = "recordType",
    event = "event",
    invitation = "invitation",
    unknown = "unknown",
};

export enum SiteType {

    /** Ex-Situ Nursery */
    site_type_nursery_ex_situ = "site_type_nursery_ex_situ",
    /** In-Situ Nursery */
    site_type_nursery_in_situ = "site_type_nursery_in_situ",
    /** Outplanting Site */
    site_type_outplanting = "site_type_outplanting",
    /** Gene Bank */
    site_type_gene_bank = "site_type_gene_bank",
};


/**
 * Base class for all records
 */
export interface Record {
    /** Unique identifier for the record */
    id: string,
    /** Timestamp when the record was created */
    createdAt?: string,
    /** ID of the user who created the record */
    createdById?: string,
    /** Timestamp when the record was last updated */
    updatedAt?: string,
    /** ID of the user who last updated the record */
    updatedById?: string,
    /** ID of the organization this record belongs to */
    organizationId?: string,
}


/**
 * Base class for inventory items that have URL paths
 */
export interface InventoryRecord extends Record {
    /** URL friendly path to this resource */
    urlPath?: string,
    /** Internal path structure */
    internalPath?: string,
    /** URL friendly identifier part */
    slug?: string,
}


/**
 * Represents an organization
 */
export interface Organization extends InventoryRecord {
    /** Name of the entity */
    name: string,
    /** Domain name associated with the organization */
    domain: string,
    /** List of site type IDs supported by the organization */
    siteTypeIds?: string[],
    /** List of species IDs supported by the organization */
    speciesIds?: string[],
}


/**
 * Represents a physical site
 */
export interface Site extends InventoryRecord {
    /** ID of the site type */
    siteTypeId: string,
    /** Name of the entity */
    name: string,
    /** Hierarchy of group IDs */
    groupIdHierarchy?: string[],
    /** Description of the entity */
    description?: string,
}


/**
 * Represents a group of items or a container within a site
 */
export interface Location extends InventoryRecord {
    /** ID of the group type */
    groupTypeId: string,
    /** Name of the entity */
    name: string,
    /** ID of the site this entity belongs to */
    siteId: string,
    /** ID of the parent entity */
    parentId: string,
    /** Description of the entity */
    description?: string,
    /** Capacity of the group */
    capacity?: number,
}


/**
 * Represents a genetic individual
 */
export interface Genet extends InventoryRecord {
    /** Name of the entity */
    name: string,
    /** ID of the species */
    speciesId: string,
    /** ID of the genet type */
    genetTypeId: string,
    /** SeaFoundry ID */
    sfId: string,
    /** Clonal ID if applicable */
    clonalId?: string,
    /** Accession number if applicable */
    accessionNumber?: string,
}


/**
 * Represents a specific coral instance
 */
export interface Coral extends InventoryRecord {
    /** Name of the entity */
    name: string,
    /** ID of the genet */
    genetId: string,
    /** ID of the species */
    speciesId: string,
    /** ID of the site this entity belongs to */
    siteId: string,
    /** ID of the group/location */
    groupId: string,
    /** ID of the coral type */
    coralTypeId: string,
    /** Quantity of items */
    quantity: number,
    /** Size of the coral */
    coral_size?: string,
}


/**
 * Represents a species
 */
export interface Species {
    /** Unique identifier for the record */
    id: string,
    /** Common name of the species */
    common_name?: string,
    /** The genus name */
    genus: string,
    /** The specific name (second part of the binomial name) */
    specific_epithet: string,
}


/**
 * Represents a person (user)
 */
export interface Person extends Record {
    /** Name of the entity */
    name: string,
    /** Email address of the user */
    email: string,
    /** URL to the user's image */
    imageUrl?: string,
}


/**
 * Represents an event in the system history
 */
export interface Event extends InventoryRecord {
    /** ID of the event type */
    eventTypeId: string,
    /** ID of the record associated with the event */
    recordId: string,
    /** Type of the record model */
    recordModelType: string,
}


/**
 * A canonical species record in the registry
 */
export interface SpeciesRegisterEntry {
    /** Unique 4-character species code (e.g. apal) */
    code: string,
    /** The genus name */
    genus: string,
    /** The specific name (second part of the binomial name) */
    specific_epithet: string,
    /** Full scientific name (genus + specific_epithet) */
    scientific_name?: string,
    /** Author and year of the species description */
    scientific_name_authorship?: string,
    /** External identifiers (e.g. worms:12345) */
    external_references?: string[],
    /** List of synonymous scientific names */
    synonyms?: string[],
    /** Previous or deprecated codes for this species */
    deprecated_codes?: string[],
}


/**
 * A canonical organization record in the registry
 */
export interface OrganizationRegisterEntry {
    /** Unique identifier for the organization */
    org_id: string,
    /** Name of the entity */
    name: string,
    /** Website URL of the organization */
    url?: string,
    /** Country where the organization is based */
    country?: string,
    /** Additional metadata as a JSON string or key-value pair */
    metadata?: string,
}
