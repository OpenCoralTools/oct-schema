# oct-schema

**oct-schema** contains canonical **JSON Schemas** for OpenCoral.Tools (OCT), and **software tools** for working with them.

These schemas define the *meaning*, *structure*, and *constraints* of coral restoration data—independent of any specific application, database, or workflow.

Follow the development at [opencoral.tools](https://opencoral.tools/).


## What this repo is for

This repository answers questions like:

- What *is* a coral genet, formally?
- How is a fragment different from a colony?
- How do we represent cohorts, founders, or parentage?
- What fields are required vs optional?
- What identifiers are valid and how are they referenced?

The schemas here are intended to be:

- validated by machines
- readable by humans
- stable enough to build tooling on top of



## What this repo provides

All generated artifacts live in [`project/`](project/):

- [`project/jsonschema/`](project/jsonschema/) — [JSON Schema](https://json-schema.org/) definitions for validation
- [`project/docs/`](project/docs/) — Markdown documentation for MkDocs
- [`project/excel/`](project/excel/) — Spreadsheet workbook templates
- [`project/node/`](project/node/) — TypeScript types for React/Node.js apps
- [`project/dart/`](project/dart/) — Dart classes for Flutter apps

## What this repo is **not**

- ❌ Not a database schema
- ❌ Not an API specification
- ❌ Not application logic
- ❌ Not a registry of allowed values

Those concerns are intentionally separated.

## Relationship to [`oct-registry`](https://github.com/OpenCoralTools/oct-registry)

`oct-schema` defines **structure and rules**.  
`oct-registry` defines **allowed identifiers and controlled vocabularies**.

For example:

- `oct-schema` may say:  
  > `speciesCode` must be a string that references a valid species identifier
- `oct-registry` provides the authoritative list of those species identifiers

Schemas may reference registry entries by convention or by explicit validation tooling.



## Schema organization

Schemas are versioned and organized by domain, for example:

- taxonomy (species, genera)
- genetics (genets, cohorts, parentage)
- physical entities (fragments, colonies)
- events (fragmentation, outplanting, mortality)
- locations (nurseries, tanks, collection sites)


## Versioning & stability

Until a 1.0 release:

- schemas may change
- fields may be renamed or refined
- breaking changes are possible

That said, changes are made deliberately, with an emphasis on long-term stability.


## Intended users

- Coral restoration practitioners
- Data managers and researchers
- Tool builders (including AI-assisted tooling)
- Anyone translating between formats (CSV ↔ JSON ↔ databases)



## Inspiration

This project is built with [LinkML](https://linkml.io/) which provides rich data modeling with easy artifact generation (JSON Schema, workbooks, docs, libraries).

The approach is heavily inspired by a similar project in behavioral health data: [Open mHealth](https://www.openmhealth.org/)

The closest existing equivalent to `oct-schema` is the very robust [Darwin Core](https://dwc.tdwg.org/). This project aims to find a balance between the scientific rigor (and resulting complexity) of Darwin Core and ease of use in specific domains, and will refer back to Darwin Core as much as makes sense.

## Installation

```bash
uv sync
```

### Development

```bash
uv sync --group dev
```

## License
MIT — Use it, fork it, build on it.

Part of OpenCoral.Tools · [opencoral.tools](https://opencoral.tools)