import click
import logging
from linkml.generators.typescriptgen import TypescriptGenerator
from linkml_runtime.utils.schemaview import SchemaView


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    if len(components) == 1:
        return components[0]
    return components[0] + "".join(x.title() for x in components[1:])


@click.command()
@click.argument("yamlfile")
@click.option("--output", "-o", help="Output file")
def cli(yamlfile, output):
    """
    Generate TypeScript from LinkML schema with automatic camelCase aliases.
    """
    logging.basicConfig(level=logging.INFO)

    # Load the schema with imports merged
    view = SchemaView(yamlfile)

    # We need to ensure we are modifying the schema that the generator will use.
    # SchemaView.all_slots() iterates over all slots in the schema closure.
    # We will modify them in place.

    for slot_name, slot in view.all_slots().items():
        if "_" in slot_name:
            camel_name = to_camel_case(slot_name)
            if not slot.alias:
                slot.alias = camel_name
                logging.info(f"Aliasing slot {slot_name} -> {camel_name}")
            elif slot.alias != camel_name:
                logging.debug(f"Slot {slot_name} has alias {slot.alias}, keeping it.")

    # Also iterate over classes to check for slot_usage or attributes that might override
    for class_name, cls in view.all_classes().items():
        for slot_name, slot_usage in cls.slot_usage.items():
            if "_" in slot_name:
                camel_name = to_camel_case(slot_name)
                if not slot_usage.alias:
                    slot_usage.alias = camel_name
                    logging.info(
                        f"Aliasing slot_usage {class_name}.{slot_name} -> {camel_name}"
                    )

        # Attributes (if any)
        for attr_name, attr in cls.attributes.items():
            if "_" in attr_name:
                camel_name = to_camel_case(attr_name)
                if not attr.alias:
                    attr.alias = camel_name
                    logging.info(
                        f"Aliasing attribute {class_name}.{attr_name} -> {camel_name}"
                    )

    # Generate TypeScript using the view's schema which should now be modified
    # Important: mergeimports=True ensures the generator sees the full schema structure
    # but since we modified the view's internal objects, we hope it uses them.
    # The generator uses schemaview if passed? No, it uses schema.
    # If we pass view.schema, it might be the root schema.
    # If imports are not merged into view.schema, we need to merge them.

    # Force merge imports into the schema object if not already
    # view.merge_imports() doesn't exist on SchemaView directly but we can use:
    # from linkml.utils.schema_fixer import SchemaFixer? No.
    # Let's rely on the fact that we modified the objects returned by all_slots(), which come from the closure.
    # But if we pass `view.schema` to the generator, does it traverse the closure or just the root?
    # Generator typically traverses imports.
    # If we modified the imported slot objects in memory, the generator should see them IF it uses the same loader/cache.
    # But Generator creates its own SchemaView usually?

    # We can pass the `schemaview` explicitly if the generator supports it.
    # TypescriptGenerator(schemaview=view)

    gen = TypescriptGenerator(schema=view.schema)
    # Hack: Inject our view so it doesn't reload
    gen.schemaview = view

    ts_output = gen.serialize()

    if output:
        with open(output, "w") as f:
            f.write(ts_output)
    else:
        print(ts_output)


if __name__ == "__main__":
    cli()
