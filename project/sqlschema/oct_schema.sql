-- # Abstract Class: Record Description: Base class for all records
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Abstract Class: InventoryRecord Description: Base class for inventory items that have URL paths
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Organization Description: Represents an organization
--     * Slot: name Description: Name of the entity
--     * Slot: domain Description: Domain name associated with the organization
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Site Description: Represents a physical site
--     * Slot: siteTypeId Description: ID of the site type
--     * Slot: name Description: Name of the entity
--     * Slot: description Description: Description of the entity
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Location Description: Represents a group of items or a container within a site
--     * Slot: groupTypeId Description: ID of the group type
--     * Slot: name Description: Name of the entity
--     * Slot: siteId Description: ID of the site this entity belongs to
--     * Slot: parentId Description: ID of the parent entity
--     * Slot: description Description: Description of the entity
--     * Slot: capacity Description: Capacity of the group
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Genet Description: Represents a genetic individual
--     * Slot: name Description: Name of the entity
--     * Slot: speciesId Description: ID of the species
--     * Slot: genetTypeId Description: ID of the genet type
--     * Slot: sfId Description: SeaFoundry ID
--     * Slot: clonalId Description: Clonal ID if applicable
--     * Slot: accessionNumber Description: Accession number if applicable
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Coral Description: Represents a specific coral instance
--     * Slot: name Description: Name of the entity
--     * Slot: genetId Description: ID of the genet
--     * Slot: speciesId Description: ID of the species
--     * Slot: siteId Description: ID of the site this entity belongs to
--     * Slot: groupId Description: ID of the group/location
--     * Slot: coralTypeId Description: ID of the coral type
--     * Slot: quantity Description: Quantity of items
--     * Slot: coral_size Description: Size of the coral
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Species Description: Represents a species
--     * Slot: id Description: Unique identifier for the record
--     * Slot: common_name Description: Common name of the species
--     * Slot: genus Description: The genus name
--     * Slot: specific_epithet Description: The specific name (second part of the binomial name)
-- # Class: Person Description: Represents a person (user)
--     * Slot: name Description: Name of the entity
--     * Slot: email Description: Email address of the user
--     * Slot: imageUrl Description: URL to the user's image
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: Event Description: Represents an event in the system history
--     * Slot: eventTypeId Description: ID of the event type
--     * Slot: recordId Description: ID of the record associated with the event
--     * Slot: recordModelType Description: Type of the record model
--     * Slot: urlPath Description: URL friendly path to this resource
--     * Slot: internalPath Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: createdAt Description: Timestamp when the record was created
--     * Slot: createdById Description: ID of the user who created the record
--     * Slot: updatedAt Description: Timestamp when the record was last updated
--     * Slot: updatedById Description: ID of the user who last updated the record
--     * Slot: organizationId Description: ID of the organization this record belongs to
-- # Class: SpeciesRegisterEntry Description: A canonical species record in the registry
--     * Slot: code Description: Unique 4-character species code (e.g. apal)
--     * Slot: genus Description: The genus name
--     * Slot: specific_epithet Description: The specific name (second part of the binomial name)
--     * Slot: scientific_name Description: Full scientific name (genus + specific_epithet)
--     * Slot: scientific_name_authorship Description: Author and year of the species description
-- # Class: OrganizationRegisterEntry Description: A canonical organization record in the registry
--     * Slot: org_id Description: Unique identifier for the organization
--     * Slot: name Description: Name of the entity
--     * Slot: url Description: Website URL of the organization
--     * Slot: country Description: Country where the organization is based
--     * Slot: metadata Description: Additional metadata as a JSON string or key-value pair
-- # Class: Organization_siteTypeIds
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: siteTypeIds Description: List of site type IDs supported by the organization
-- # Class: Organization_speciesIds
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: speciesIds Description: List of species IDs supported by the organization
-- # Class: Site_groupIdHierarchy
--     * Slot: Site_id Description: Autocreated FK slot
--     * Slot: groupIdHierarchy Description: Hierarchy of group IDs
-- # Class: SpeciesRegisterEntry_external_references
--     * Slot: SpeciesRegisterEntry_code Description: Autocreated FK slot
--     * Slot: external_references Description: External identifiers (e.g. worms:12345)
-- # Class: SpeciesRegisterEntry_synonyms
--     * Slot: SpeciesRegisterEntry_code Description: Autocreated FK slot
--     * Slot: synonyms Description: List of synonymous scientific names
-- # Class: SpeciesRegisterEntry_deprecated_codes
--     * Slot: SpeciesRegisterEntry_code Description: Autocreated FK slot
--     * Slot: deprecated_codes Description: Previous or deprecated codes for this species

CREATE TABLE "Record" (
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Record_id" ON "Record" (id);
CREATE TABLE "InventoryRecord" (
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_InventoryRecord_id" ON "InventoryRecord" (id);
CREATE TABLE "Organization" (
	name TEXT NOT NULL,
	domain TEXT NOT NULL,
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Organization_id" ON "Organization" (id);
CREATE TABLE "Site" (
	"siteTypeId" TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Site_id" ON "Site" (id);
CREATE TABLE "Location" (
	"groupTypeId" TEXT NOT NULL,
	name TEXT NOT NULL,
	"siteId" TEXT NOT NULL,
	"parentId" TEXT NOT NULL,
	description TEXT,
	capacity INTEGER,
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Location_id" ON "Location" (id);
CREATE TABLE "Genet" (
	name TEXT NOT NULL,
	"speciesId" TEXT NOT NULL,
	"genetTypeId" TEXT NOT NULL,
	"sfId" TEXT NOT NULL,
	"clonalId" TEXT,
	"accessionNumber" TEXT,
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Genet_id" ON "Genet" (id);
CREATE TABLE "Coral" (
	name TEXT NOT NULL,
	"genetId" TEXT NOT NULL,
	"speciesId" TEXT NOT NULL,
	"siteId" TEXT NOT NULL,
	"groupId" TEXT NOT NULL,
	"coralTypeId" TEXT NOT NULL,
	quantity INTEGER NOT NULL,
	coral_size VARCHAR(2),
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Coral_id" ON "Coral" (id);
CREATE TABLE "Species" (
	id TEXT NOT NULL,
	common_name TEXT,
	genus TEXT NOT NULL,
	specific_epithet TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Species_id" ON "Species" (id);
CREATE TABLE "Person" (
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	"imageUrl" TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Person_id" ON "Person" (id);
CREATE TABLE "Event" (
	"eventTypeId" TEXT NOT NULL,
	"recordId" TEXT NOT NULL,
	"recordModelType" VARCHAR(12) NOT NULL,
	"urlPath" TEXT,
	"internalPath" TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	"createdAt" DATETIME,
	"createdById" TEXT,
	"updatedAt" DATETIME,
	"updatedById" TEXT,
	"organizationId" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Event_id" ON "Event" (id);
CREATE TABLE "SpeciesRegisterEntry" (
	code TEXT NOT NULL,
	genus TEXT NOT NULL,
	specific_epithet TEXT NOT NULL,
	scientific_name TEXT,
	scientific_name_authorship TEXT,
	PRIMARY KEY (code)
);CREATE INDEX "ix_SpeciesRegisterEntry_code" ON "SpeciesRegisterEntry" (code);
CREATE TABLE "OrganizationRegisterEntry" (
	org_id TEXT NOT NULL,
	name TEXT NOT NULL,
	url TEXT,
	country TEXT,
	metadata TEXT,
	PRIMARY KEY (org_id)
);CREATE INDEX "ix_OrganizationRegisterEntry_org_id" ON "OrganizationRegisterEntry" (org_id);
CREATE TABLE "Organization_siteTypeIds" (
	"Organization_id" TEXT,
	"siteTypeIds" TEXT,
	PRIMARY KEY ("Organization_id", "siteTypeIds"),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);CREATE INDEX "ix_Organization_siteTypeIds_Organization_id" ON "Organization_siteTypeIds" ("Organization_id");CREATE INDEX "ix_Organization_siteTypeIds_siteTypeIds" ON "Organization_siteTypeIds" ("siteTypeIds");
CREATE TABLE "Organization_speciesIds" (
	"Organization_id" TEXT,
	"speciesIds" TEXT,
	PRIMARY KEY ("Organization_id", "speciesIds"),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);CREATE INDEX "ix_Organization_speciesIds_speciesIds" ON "Organization_speciesIds" ("speciesIds");CREATE INDEX "ix_Organization_speciesIds_Organization_id" ON "Organization_speciesIds" ("Organization_id");
CREATE TABLE "Site_groupIdHierarchy" (
	"Site_id" TEXT,
	"groupIdHierarchy" TEXT,
	PRIMARY KEY ("Site_id", "groupIdHierarchy"),
	FOREIGN KEY("Site_id") REFERENCES "Site" (id)
);CREATE INDEX "ix_Site_groupIdHierarchy_Site_id" ON "Site_groupIdHierarchy" ("Site_id");CREATE INDEX "ix_Site_groupIdHierarchy_groupIdHierarchy" ON "Site_groupIdHierarchy" ("groupIdHierarchy");
CREATE TABLE "SpeciesRegisterEntry_external_references" (
	"SpeciesRegisterEntry_code" TEXT,
	external_references TEXT,
	PRIMARY KEY ("SpeciesRegisterEntry_code", external_references),
	FOREIGN KEY("SpeciesRegisterEntry_code") REFERENCES "SpeciesRegisterEntry" (code)
);CREATE INDEX "ix_SpeciesRegisterEntry_external_references_external_references" ON "SpeciesRegisterEntry_external_references" (external_references);CREATE INDEX "ix_SpeciesRegisterEntry_external_references_SpeciesRegisterEntry_code" ON "SpeciesRegisterEntry_external_references" ("SpeciesRegisterEntry_code");
CREATE TABLE "SpeciesRegisterEntry_synonyms" (
	"SpeciesRegisterEntry_code" TEXT,
	synonyms TEXT,
	PRIMARY KEY ("SpeciesRegisterEntry_code", synonyms),
	FOREIGN KEY("SpeciesRegisterEntry_code") REFERENCES "SpeciesRegisterEntry" (code)
);CREATE INDEX "ix_SpeciesRegisterEntry_synonyms_SpeciesRegisterEntry_code" ON "SpeciesRegisterEntry_synonyms" ("SpeciesRegisterEntry_code");CREATE INDEX "ix_SpeciesRegisterEntry_synonyms_synonyms" ON "SpeciesRegisterEntry_synonyms" (synonyms);
CREATE TABLE "SpeciesRegisterEntry_deprecated_codes" (
	"SpeciesRegisterEntry_code" TEXT,
	deprecated_codes TEXT,
	PRIMARY KEY ("SpeciesRegisterEntry_code", deprecated_codes),
	FOREIGN KEY("SpeciesRegisterEntry_code") REFERENCES "SpeciesRegisterEntry" (code)
);CREATE INDEX "ix_SpeciesRegisterEntry_deprecated_codes_SpeciesRegisterEntry_code" ON "SpeciesRegisterEntry_deprecated_codes" ("SpeciesRegisterEntry_code");CREATE INDEX "ix_SpeciesRegisterEntry_deprecated_codes_deprecated_codes" ON "SpeciesRegisterEntry_deprecated_codes" (deprecated_codes);
