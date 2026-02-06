# Load environment variables from config.public.mk
set dotenv-load := true
set dotenv-filename := "config.public.mk"

# Environment variables with defaults
schema_name := env_var_or_default("LINKML_SCHEMA_NAME", "oct_schema")
source_schema_dir := env_var_or_default("LINKML_SCHEMA_SOURCE_DIR", "src/oct_schema/schema")
config_yaml := env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "config.yaml")

# Directory variables
dest := "project"
source_schema_path := source_schema_dir / schema_name + ".yaml"

# Default: list commands
_default:
    @just --list

# Install project dependencies
install:
    uv sync --group dev

# Generate all project artifacts
gen-project:
    uv run gen-project --config-file {{config_yaml}} -d {{dest}} {{source_schema_path}}
    # Generate TypeScript
    @mkdir -p {{dest}}/node/src
    uv run python scripts/gen_ts_camel.py {{source_schema_path}} -o {{dest}}/node/src/{{schema_name}}.ts
    # Generate Dart
    @mkdir -p {{dest}}/dart/lib
    uv run python scripts/dartgen.py {{source_schema_path}} -o {{dest}}/dart/lib/{{schema_name}}.dart

# Clean generated files
clean:
    rm -rf {{dest}}

# Run linting on schema
lint:
    uv run linkml-lint {{source_schema_dir}}
