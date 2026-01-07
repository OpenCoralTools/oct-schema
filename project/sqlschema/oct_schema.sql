-- # Abstract Class: Record Description: Base class for all records
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Abstract Class: InventoryRecord Description: Base class for inventory items that have URL paths
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Organization Description: Represents an organization
--     * Slot: name Description: Name of the entity
--     * Slot: domain Description: Domain name associated with the organization
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Site Description: Represents a physical site
--     * Slot: site_type_id Description: ID of the site type
--     * Slot: name Description: Name of the entity
--     * Slot: description Description: Description of the entity
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Location Description: Represents a group of items or a container within a site
--     * Slot: group_type_id Description: ID of the group type
--     * Slot: name Description: Name of the entity
--     * Slot: site_id Description: ID of the site this entity belongs to
--     * Slot: parent_id Description: ID of the parent entity
--     * Slot: description Description: Description of the entity
--     * Slot: capacity Description: Capacity of the group
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Genet Description: Represents a genetic individual
--     * Slot: name Description: Name of the entity
--     * Slot: species_id Description: ID of the species
--     * Slot: genet_type_id Description: ID of the genet type
--     * Slot: sf_id Description: SeaFoundry ID
--     * Slot: clonal_id Description: Clonal ID if applicable
--     * Slot: accession_number Description: Accession number if applicable
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Coral Description: Represents a specific coral instance
--     * Slot: name Description: Name of the entity
--     * Slot: genet_id Description: ID of the genet
--     * Slot: species_id Description: ID of the species
--     * Slot: site_id Description: ID of the site this entity belongs to
--     * Slot: group_id Description: ID of the group/location
--     * Slot: coral_type_id Description: ID of the coral type
--     * Slot: quantity Description: Quantity of items
--     * Slot: coral_size Description: Size of the coral
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Species Description: Represents a species
--     * Slot: id Description: Unique identifier for the record
--     * Slot: common_name Description: Common name of the species
--     * Slot: genus Description: The genus name
--     * Slot: specific_epithet Description: The specific name (second part of the binomial name)
-- # Class: Person Description: Represents a person (user)
--     * Slot: name Description: Name of the entity
--     * Slot: email Description: Email address of the user
--     * Slot: image_url Description: URL to the user's image
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: Event Description: Represents an event in the system history
--     * Slot: event_type_id Description: ID of the event type
--     * Slot: record_id Description: ID of the record associated with the event
--     * Slot: record_model_type Description: Type of the record model
--     * Slot: url_path Description: URL friendly path to this resource
--     * Slot: internal_path Description: Internal path structure
--     * Slot: slug Description: URL friendly identifier part
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: created_by_id Description: ID of the user who created the record
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: updated_by_id Description: ID of the user who last updated the record
--     * Slot: organization_id Description: ID of the organization this record belongs to
-- # Class: SpeciesRegisterEntry Description: Represents an entry in the species registry
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: common_name Description: Common name of the species
--     * Slot: genus Description: The genus name
--     * Slot: specific_epithet Description: The specific name (second part of the binomial name)
--     * Slot: scientific_name Description: Full scientific name (genus + specific epithet)
--     * Slot: photo_url Description: URL to a photo of the species
-- # Class: OrganizationRegisterEntry Description: Represents an entry in the organization registry
--     * Slot: id Description: Unique identifier for the record
--     * Slot: created_at Description: Timestamp when the record was created
--     * Slot: updated_at Description: Timestamp when the record was last updated
--     * Slot: name Description: Name of the entity
--     * Slot: description Description: Description of the entity
--     * Slot: region Description: Geographical region of the organization
--     * Slot: website_url Description: Website URL of the organization
--     * Slot: contact_email Description: Contact email for the organization
--     * Slot: logo_url Description: URL to the organization's logo
--     * Slot: is_active Description: Whether the organization is active
-- # Class: Organization_site_type_ids
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: site_type_ids Description: List of site type IDs supported by the organization
-- # Class: Organization_species_ids
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: species_ids Description: List of species IDs supported by the organization
-- # Class: Site_group_id_hierarchy
--     * Slot: Site_id Description: Autocreated FK slot
--     * Slot: group_id_hierarchy Description: Hierarchy of group IDs
-- # Class: SpeciesRegisterEntry_tags
--     * Slot: SpeciesRegisterEntry_id Description: Autocreated FK slot
--     * Slot: tags Description: Tags associated with the species

CREATE TABLE "Record" (
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Record_id" ON "Record" (id);
CREATE TABLE "InventoryRecord" (
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_InventoryRecord_id" ON "InventoryRecord" (id);
CREATE TABLE "Organization" (
	name TEXT NOT NULL,
	domain TEXT NOT NULL,
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Organization_id" ON "Organization" (id);
CREATE TABLE "Site" (
	site_type_id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Site_id" ON "Site" (id);
CREATE TABLE "Location" (
	group_type_id TEXT NOT NULL,
	name TEXT NOT NULL,
	site_id TEXT NOT NULL,
	parent_id TEXT NOT NULL,
	description TEXT,
	capacity INTEGER,
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Location_id" ON "Location" (id);
CREATE TABLE "Genet" (
	name TEXT NOT NULL,
	species_id TEXT NOT NULL,
	genet_type_id TEXT NOT NULL,
	sf_id TEXT NOT NULL,
	clonal_id TEXT,
	accession_number TEXT,
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Genet_id" ON "Genet" (id);
CREATE TABLE "Coral" (
	name TEXT NOT NULL,
	genet_id TEXT NOT NULL,
	species_id TEXT NOT NULL,
	site_id TEXT NOT NULL,
	group_id TEXT NOT NULL,
	coral_type_id TEXT NOT NULL,
	quantity INTEGER NOT NULL,
	coral_size VARCHAR(2),
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
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
	image_url TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Person_id" ON "Person" (id);
CREATE TABLE "Event" (
	event_type_id TEXT NOT NULL,
	record_id TEXT NOT NULL,
	record_model_type VARCHAR(12) NOT NULL,
	url_path TEXT,
	internal_path TEXT,
	slug TEXT,
	id TEXT NOT NULL,
	created_at DATETIME,
	created_by_id TEXT,
	updated_at DATETIME,
	updated_by_id TEXT,
	organization_id TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Event_id" ON "Event" (id);
CREATE TABLE "SpeciesRegisterEntry" (
	id TEXT NOT NULL,
	created_at DATETIME NOT NULL,
	updated_at DATETIME NOT NULL,
	common_name TEXT,
	genus TEXT NOT NULL,
	specific_epithet TEXT NOT NULL,
	scientific_name TEXT,
	photo_url TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SpeciesRegisterEntry_id" ON "SpeciesRegisterEntry" (id);
CREATE TABLE "OrganizationRegisterEntry" (
	id TEXT NOT NULL,
	created_at DATETIME NOT NULL,
	updated_at DATETIME NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	region TEXT NOT NULL,
	website_url TEXT,
	contact_email TEXT,
	logo_url TEXT,
	is_active BOOLEAN,
	PRIMARY KEY (id)
);CREATE INDEX "ix_OrganizationRegisterEntry_id" ON "OrganizationRegisterEntry" (id);
CREATE TABLE "Organization_site_type_ids" (
	"Organization_id" TEXT,
	site_type_ids TEXT,
	PRIMARY KEY ("Organization_id", site_type_ids),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);CREATE INDEX "ix_Organization_site_type_ids_site_type_ids" ON "Organization_site_type_ids" (site_type_ids);CREATE INDEX "ix_Organization_site_type_ids_Organization_id" ON "Organization_site_type_ids" ("Organization_id");
CREATE TABLE "Organization_species_ids" (
	"Organization_id" TEXT,
	species_ids TEXT,
	PRIMARY KEY ("Organization_id", species_ids),
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id)
);CREATE INDEX "ix_Organization_species_ids_species_ids" ON "Organization_species_ids" (species_ids);CREATE INDEX "ix_Organization_species_ids_Organization_id" ON "Organization_species_ids" ("Organization_id");
CREATE TABLE "Site_group_id_hierarchy" (
	"Site_id" TEXT,
	group_id_hierarchy TEXT,
	PRIMARY KEY ("Site_id", group_id_hierarchy),
	FOREIGN KEY("Site_id") REFERENCES "Site" (id)
);CREATE INDEX "ix_Site_group_id_hierarchy_Site_id" ON "Site_group_id_hierarchy" ("Site_id");CREATE INDEX "ix_Site_group_id_hierarchy_group_id_hierarchy" ON "Site_group_id_hierarchy" (group_id_hierarchy);
CREATE TABLE "SpeciesRegisterEntry_tags" (
	"SpeciesRegisterEntry_id" TEXT,
	tags TEXT,
	PRIMARY KEY ("SpeciesRegisterEntry_id", tags),
	FOREIGN KEY("SpeciesRegisterEntry_id") REFERENCES "SpeciesRegisterEntry" (id)
);CREATE INDEX "ix_SpeciesRegisterEntry_tags_SpeciesRegisterEntry_id" ON "SpeciesRegisterEntry_tags" ("SpeciesRegisterEntry_id");CREATE INDEX "ix_SpeciesRegisterEntry_tags_tags" ON "SpeciesRegisterEntry_tags" (tags);
