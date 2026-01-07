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
export type SpeciesRegisterEntryId = string;
export type OrganizationRegisterEntryId = string;

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
    coralSize?: string,
}


/**
 * Represents a species
 */
export interface Species {
    /** Unique identifier for the record */
    id: string,
    /** Common name of the species */
    commonName?: string,
    /** The genus name */
    genus: string,
    /** The specific name (second part of the binomial name) */
    specificEpithet: string,
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
 * Represents an entry in the species registry
 */
export interface SpeciesRegisterEntry {
    /** Unique identifier for the record */
    id: string,
    /** Timestamp when the record was created */
    createdAt: string,
    /** Timestamp when the record was last updated */
    updatedAt: string,
    /** Common name of the species */
    commonName?: string,
    /** The genus name */
    genus: string,
    /** The specific name (second part of the binomial name) */
    specificEpithet: string,
    /** Full scientific name (genus + specific epithet) */
    scientificName?: string,
    /** URL to a photo of the species */
    photoUrl?: string,
    /** Tags associated with the species */
    tags?: string[],
}


/**
 * Represents an entry in the organization registry
 */
export interface OrganizationRegisterEntry {
    /** Unique identifier for the record */
    id: string,
    /** Timestamp when the record was created */
    createdAt: string,
    /** Timestamp when the record was last updated */
    updatedAt: string,
    /** Name of the entity */
    name: string,
    /** Description of the entity */
    description?: string,
    /** Geographical region of the organization */
    region: string,
    /** Website URL of the organization */
    websiteUrl?: string,
    /** Contact email for the organization */
    contactEmail?: string,
    /** URL to the organization's logo */
    logoUrl?: string,
    /** Whether the organization is active */
    isActive?: boolean,
}
