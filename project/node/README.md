# TypeScript Types

TypeScript type definitions for use in Node.js, React, and other TypeScript/JavaScript projects.

## Installation

Copy `src/oct_schema.ts` into your project, or import directly.

## Usage

```typescript
import { Coral } from './oct_schema';

const coral: Coral = {
  name: 'APAL001'
};
```

## Features

- Full type safety for all schema classes
- camelCase property names (JSON keys preserved for serialization)
- Works with React, Node.js, and any TypeScript project
