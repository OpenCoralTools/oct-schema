#!/usr/bin/env python3
"""
LinkML Dart Code Generator

Generates Dart classes from LinkML schemas with proper inheritance,
camelCase properties, and JSON serialization support.
"""

import os
from dataclasses import dataclass
from typing import Optional

from jinja2 import Template

try:
    from linkml.generators.oocodegen import OOCodeGenerator
    from linkml_runtime.linkml_model.meta import (
        SlotDefinition,
    )
    from linkml_runtime.utils.schemaview import SchemaView
except ImportError as e:
    raise ImportError(
        "LinkML dependencies not available. Install with: uv sync --group dev"
    ) from e


@dataclass
class DartSlot:
    """Represents a Dart class property/slot"""

    name: str
    dart_type: str
    json_name: str
    required: bool
    description: Optional[str] = None
    is_enum: bool = False
    is_class: bool = False
    is_list: bool = False
    enum_name: Optional[str] = None
    item_type: Optional[str] = None


@dataclass
class DartClass:
    """Represents a Dart class"""

    name: str
    slots: list[DartSlot]
    parent: Optional[str] = None
    parent_required_slots: list[str] = None
    parent_required_slot_names: list[str] = None
    parent_required_slot_types: list[str] = None
    parent_required_slot_json_names: list[str] = None
    is_abstract: bool = False
    description: Optional[str] = None

    def __post_init__(self):
        if self.parent_required_slots is None:
            self.parent_required_slots = []
        if self.parent_required_slot_names is None:
            self.parent_required_slot_names = []
        if self.parent_required_slot_types is None:
            self.parent_required_slot_types = []
        if self.parent_required_slot_json_names is None:
            self.parent_required_slot_json_names = []


@dataclass
class DartEnum:
    """Represents a Dart enum"""

    name: str
    values: list[str]


class DartGenerator(OOCodeGenerator):
    """
    Generates Dart code from a LinkML schema
    """

    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.1"
    valid_formats = ["text"]
    uses_schemaloader = False
    template_file = os.path.join(os.path.dirname(__file__), "dart_template.jinja2")

    def __init__(self, schema, **kwargs):
        super().__init__(schema, **kwargs)
        if not self.template_file:
            self.template_file = os.path.join(
                os.path.dirname(__file__), "dart_template.jinja2"
            )
        # Ensure camelCase conversion for slots
        self._add_camelcase_aliases()

    def _add_camelcase_aliases(self):
        """Add camelCase aliases for snake_case slots"""
        for slot_name, slot in self.schemaview.all_slots().items():
            if "_" in slot_name and not slot.alias:
                slot.alias = self._to_camel_case(slot_name)

    @staticmethod
    def _to_camel_case(snake_str: str) -> str:
        """Convert snake_case to camelCase"""
        components = snake_str.split("_")
        if len(components) == 1:
            return components[0]
        return components[0] + "".join(x.title() for x in components[1:])

    def map_type(self, slot: SlotDefinition) -> str:
        """Map LinkML type to Dart type"""
        range_name = slot.range if hasattr(slot, "range") else None

        # Check if it's an enum
        if range_name and range_name in self.schemaview.all_enums():
            return range_name

        # Check if it's a class
        if range_name and range_name in self.schemaview.all_classes():
            return range_name

        # Map built-in types
        type_map = {
            "string": "String",
            "str": "String",
            "integer": "int",
            "int": "int",
            "float": "double",
            "double": "double",
            "boolean": "bool",
            "bool": "bool",
            "date": "String",  # Dart doesn't have built-in date, use String
            "datetime": "String",
            "time": "String",
            "uri": "String",
            "uriorcurie": "String",
        }

        if range_name in type_map:
            return type_map[range_name]

        # Default to String for unknown types
        return "String"

    def get_slot_name(self, slot: SlotDefinition) -> str:
        """Get the Dart property name for a slot"""
        # Use alias if available (camelCase), otherwise convert
        if slot.alias:
            return slot.alias
        if "_" in slot.name:
            return self._to_camel_case(slot.name)
        return slot.name

    def get_json_name(self, slot: SlotDefinition) -> str:
        """Get the JSON property name (use alias or original name)"""
        return slot.alias if slot.alias else slot.name

    def generate_enums(self, enums: dict) -> list[DartEnum]:
        """Generate Dart enum definitions"""
        dart_enums = []
        for enum_name, enum_def in enums.items():
            values = []
            if enum_def.permissible_values:
                for pv_name, pv in enum_def.permissible_values.items():
                    values.append(pv_name)
            dart_enums.append(DartEnum(name=enum_name, values=values))
        return dart_enums

    def generate_classes(self) -> list[DartClass]:
        """Generate Dart class definitions"""
        dart_classes = []
        sv = self.schemaview

        # Get all classes, sorted by inheritance order (parents first)
        all_classes = list(sv.all_classes().items())
        # Sort: abstract classes and classes without parents first
        sorted_classes = sorted(
            all_classes,
            key=lambda x: (
                0 if x[1].abstract else 1,  # Abstract first
                0 if not x[1].is_a else 1,  # No parent first
            ),
        )

        for class_name, class_def in sorted_classes:
            # Get all slots for this class (including inherited)
            all_slot_names = sv.class_slots(class_name)

            # Get slots defined directly in this class (not inherited)
            direct_slot_names = set(class_def.slots) if class_def.slots else set()
            direct_slot_names.update(
                class_def.attributes.keys() if class_def.attributes else []
            )

            # If no direct slots, check if this class adds any slots via slot_usage
            if not direct_slot_names and class_def.slot_usage:
                direct_slot_names.update(class_def.slot_usage.keys())

            direct_slots = []
            for slot_name in all_slot_names:
                # Only include if it's a direct slot of this class
                if slot_name in direct_slot_names:
                    slot = sv.get_slot(slot_name)
                    if slot:
                        direct_slots.append(slot)
                    elif slot_name in class_def.attributes:
                        # It's an attribute, use it directly
                        attr = class_def.attributes[slot_name]
                        direct_slots.append(attr)

            dart_slots = []
            for slot in direct_slots:
                dart_type = self.map_type(slot)
                slot_name = self.get_slot_name(slot)
                json_name = self.get_json_name(slot)
                is_required = slot.required if hasattr(slot, "required") else False

                # Check if it's multivalued (list)
                is_multivalued = (
                    slot.multivalued if hasattr(slot, "multivalued") else False
                )

                is_enum = dart_type in sv.all_enums()
                is_class = dart_type in sv.all_classes()

                dart_slot = DartSlot(
                    name=slot_name,
                    dart_type=f"List<{dart_type}>" if is_multivalued else dart_type,
                    json_name=json_name,
                    required=is_required,
                    description=slot.description
                    if hasattr(slot, "description")
                    else None,
                    is_enum=is_enum
                    and not is_multivalued,  # Only mark as enum if not a list
                    is_class=is_class and not is_multivalued,
                    is_list=is_multivalued,
                    enum_name=dart_type if (is_enum and not is_multivalued) else None,
                    item_type=dart_type if is_multivalued else None,
                )
                dart_slots.append(dart_slot)

            # Get parent class name and ALL required slots (including inherited) for super() call
            parent_name = None
            parent_required_slots = []
            parent_required_slot_names = []  # Dart property names
            if class_def.is_a:
                parent_name = class_def.is_a
                # Get ALL required slots from parent (including inherited)
                # This is what the parent constructor needs
                parent_all_slots = sv.class_slots(parent_name)
                for ps in parent_all_slots:
                    parent_slot = sv.get_slot(ps)
                    if parent_slot and parent_slot.required:
                        # Convert to camelCase for Dart
                        camel_name = self.get_slot_name(parent_slot)
                        # Get the Dart type (including List<> if multivalued)
                        is_multivalued = (
                            parent_slot.multivalued
                            if hasattr(parent_slot, "multivalued")
                            else False
                        )
                        dart_type = self.map_type(parent_slot)
                        if is_multivalued:
                            dart_type = f"List<{dart_type}>"
                        parent_required_slots.append(ps)  # Original slot name
                        parent_required_slot_names.append(camel_name)  # Dart name

            # Check which required parent slots are already in child class
            child_slot_names = {s.name for s in dart_slots}
            missing_parent_slot_info = []
            for ps, camel_name in zip(
                parent_required_slots, parent_required_slot_names
            ):
                if camel_name not in child_slot_names:
                    # Get the type for this slot
                    parent_slot = sv.get_slot(ps)
                    if parent_slot:
                        dart_type = self.map_type(parent_slot)
                        # Check if multivalued
                        is_multivalued = (
                            parent_slot.multivalued
                            if hasattr(parent_slot, "multivalued")
                            else False
                        )
                        if is_multivalued:
                            dart_type = f"List<{dart_type}>"
                    else:
                        dart_type = "String"
                    missing_parent_slot_info.append((camel_name, dart_type, ps))

            dart_class = DartClass(
                name=class_name,
                slots=dart_slots,
                parent=parent_name,
                parent_required_slots=parent_required_slots,
                parent_required_slot_names=[
                    info[0] for info in missing_parent_slot_info
                ],
                parent_required_slot_types=[
                    info[1] for info in missing_parent_slot_info
                ],
                parent_required_slot_json_names=[
                    info[2] for info in missing_parent_slot_info
                ],
                is_abstract=class_def.abstract
                if hasattr(class_def, "abstract")
                else False,
                description=class_def.description
                if hasattr(class_def, "description")
                else None,
            )
            dart_classes.append(dart_class)

        return dart_classes

    def default_value_for_type(self, range_name: str) -> str:
        """Return default value for a Dart type"""
        type_defaults = {
            "String": '""',
            "int": "0",
            "double": "0.0",
            "bool": "false",
        }
        return type_defaults.get(range_name, "null")

    def serialize(self, output=None) -> str:
        """Serialize a schema to Dart code"""
        sv: SchemaView = self.schemaview

        enums = self.generate_enums(sv.all_enums())
        classes = self.generate_classes()

        # Get enum names for template
        enum_names = set(sv.all_enums().keys())

        with open(self.template_file, "r") as f:
            template_str = f.read()

        template_obj = Template(template_str)
        out_str = template_obj.render(
            gen=self,
            schema=sv.schema,
            view=sv,
            enums=enums,
            classes=classes,
            enum_names=enum_names,
        )

        if output is not None:
            with open(output, "w") as out:
                out.write(out_str)
        return out_str


if __name__ == "__main__":
    import click

    @click.command()
    @click.argument("yamlfile")
    @click.option("--output", "-o", help="Output file")
    def cli(yamlfile, output):
        """Generate Dart code from LinkML schema"""
        from linkml_runtime.utils.schemaview import SchemaView

        view = SchemaView(yamlfile)
        gen = DartGenerator(schema=view.schema)
        gen.schemaview = view

        dart_output = gen.serialize(output=output)
        if not output:
            print(dart_output)

    cli()
