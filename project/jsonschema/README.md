# JSON Schema

Machine-readable schema definitions for validating coral data.

## Usage

Use these schemas with any JSON Schema validator:

```javascript
import Ajv from 'ajv';
import schema from './oct_schema.schema.json';

const ajv = new Ajv();
const validate = ajv.compile(schema);

const valid = validate(yourData);
```

## Files

- `oct_schema.schema.json` — Complete schema with all definitions
