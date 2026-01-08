#!/usr/bin/env python3
"""
Generate Dart code from JSON Schema using quicktype.

This script wraps quicktype to handle JSON Schemas that only have $defs
without a root type. It creates a temporary schema with a root type that
references all definitions.
"""

import json
import subprocess
import sys
import tempfile
import os
from pathlib import Path


def fix_missing_refs(obj, defs):
    """Recursively fix missing $ref references by replacing with a generic object type."""
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref_path = obj["$ref"]
            # Extract the definition name from the ref (e.g., "#/$defs/EventPayload" -> "EventPayload")
            if ref_path.startswith("#/$defs/"):
                def_name = ref_path.replace("#/$defs/", "")
                if def_name not in defs:
                    # Replace missing ref with a generic object type
                    print(
                        f"Warning: Missing definition '{def_name}', replacing with generic object",
                        file=sys.stderr,
                    )
                    return {"type": "object", "additionalProperties": True}
        # Recursively process nested objects
        return {k: fix_missing_refs(v, defs) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_missing_refs(item, defs) for item in obj]
    else:
        return obj


def create_wrapped_schema(json_schema_path: str) -> str:
    """Create a temporary JSON Schema with a root type that references all $defs."""
    with open(json_schema_path, "r") as f:
        schema = json.load(f)

    # Extract $defs
    defs = schema.get("$defs", {})
    if not defs:
        raise ValueError("JSON Schema has no $defs section")

    # Fix missing references in defs
    defs = fix_missing_refs(defs, defs)

    # Create a root type with properties that reference each definition
    # This tells quicktype to generate separate classes for each type
    root_properties = {}
    for def_name in defs.keys():
        root_properties[def_name] = {"$ref": f"#/$defs/{def_name}"}

    # Create wrapped schema with properties at root level
    # This ensures quicktype generates separate classes for each definition
    wrapped_schema = {
        "$schema": schema.get("$schema", "http://json-schema.org/draft-07/schema#"),
        "type": "object",
        "properties": root_properties,
        "$defs": defs,
    }

    # Create temporary file
    temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump(wrapped_schema, temp_file, indent=2)
    temp_file.close()

    return temp_file.name


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate Dart code from JSON Schema using quicktype"
    )
    parser.add_argument("json_schema", help="Path to JSON Schema file")
    parser.add_argument("-o", "--output", required=True, help="Output Dart file path")

    args = parser.parse_args()

    # Create wrapped schema
    try:
        wrapped_schema_path = create_wrapped_schema(args.json_schema)
    except Exception as e:
        print(f"Error processing JSON Schema: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        # Ensure output directory exists
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Run quicktype
        cmd = [
            "npx",
            "--yes",
            "quicktype",
            "--lang",
            "dart",
            "--src-lang",
            "schema",
            "--src",
            wrapped_schema_path,
            "-o",
            args.output,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print("quicktype failed:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(1)

        # Clean up temporary file
        os.unlink(wrapped_schema_path)

        print(f"Successfully generated Dart code: {args.output}")

    except Exception as e:
        # Clean up temporary file on error
        if os.path.exists(wrapped_schema_path):
            os.unlink(wrapped_schema_path)
        print(f"Error generating Dart code: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
