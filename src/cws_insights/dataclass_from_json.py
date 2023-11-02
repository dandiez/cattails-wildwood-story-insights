"""Write dataclass python code to match records of data in json files."""

import dataclasses
from typing import Literal

import black
from dataclasses_json import dataclass_json, Undefined
from genson import SchemaBuilder

from cws_insights.common import slug_it

PROP_TYPE_TO_TYPE_AS_STR = {
    "string": "str",
    "number": "float | int",
    "integer": "int",
    "boolean": "bool",
}


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JsonSchemaProperty:
    type: Literal["str", "boolean", "array", "object", "number", "integer"]
    properties: dict[str, "JsonSchemaProperty"] = None
    required: list[str] = None
    items: "JsonSchemaProperty" = None
    property_name_path: list[str] = None

    @property
    def property_name(self):
        return self.property_name_path[-1]

    def get_class_name(self):
        prop_name_path = self.property_name_path
        class_name_parts = []
        for prop_name in prop_name_path:
            prop_in_caps = "".join([word.capitalize() for word in prop_name.split("_")])
            class_name_parts.append(prop_in_caps)
        return "_".join(class_name_parts)

    def type_as_string(self):

        if self.type in PROP_TYPE_TO_TYPE_AS_STR:
            return PROP_TYPE_TO_TYPE_AS_STR[self.type]
        if self.type == "array":
            if self.items is None:
                return "list"
            return f"list[{self.items.type_as_string()}]"
        if self.type == "object":
            return self.get_class_name()
        raise ValueError(self.type)

    def attribute_declaration(self, is_required: bool):
        prop_name = self.property_name
        slugged = slug_it(prop_name)
        is_list = self.type == "array"
        if slugged != prop_name and not is_required and not is_list:
            addendum = f"= dataclasses.field(metadata=dataclasses_json.config(field_name='{prop_name}'), default=None)"
        elif slugged != prop_name and not is_required and is_list:
            addendum = f"= dataclasses.field(metadata=dataclasses_json.config(field_name='{prop_name}'), default_factory=list)"
        elif slugged != prop_name and is_required:
            addendum = f"= dataclasses.field(metadata=dataclasses_json.config(field_name='{prop_name}'))"
        elif not is_required and not is_list:
            addendum = f"= None"
        elif not is_required and is_list:
            addendum = f"= dataclasses.field(default_factory=list)"
        else:
            addendum = ""
        return f"    {slugged}: {self.type_as_string()} {addendum}"

    def yield_contained_objects_and_populate_paths(self) -> tuple[list[str], "JsonSchemaProperty"]:
        path = self.property_name_path
        if self.type == "array":
            prop = self.items
            if prop is None:
                return
            prop.property_name_path = path[:] # + ["_item"]
            if prop.type == "object":
                yield prop
                yield from prop.yield_contained_objects_and_populate_paths()
            elif prop.type == "array":
                # prop.items.property_name_path = path[:]
                yield from prop.yield_contained_objects_and_populate_paths()

        if self.type == "object":
            for prop_name, prop in self.properties.items():
                prop.property_name_path = path[:] + [prop_name]
                if prop.type == "object":
                    yield prop
                    yield from prop.yield_contained_objects_and_populate_paths()
                elif prop.type == "array":
                    # prop.items.property_name_path = path[:] + [prop_name]
                    yield from prop.yield_contained_objects_and_populate_paths()


def yield_class_definitions_from_json_schema_property(
    json_schema_prop: JsonSchemaProperty,
):
    internal_objects = list(json_schema_prop.yield_contained_objects_and_populate_paths())
    yield get_class_def_as_str(json_schema_prop)
    for prop in internal_objects:
        yield get_class_def_as_str(prop)


def get_class_def_as_str(json_schema_prop):
    class_name = json_schema_prop.get_class_name()
    class_def_lines = [
        "@dataclasses_json.dataclass_json",
        "@dataclasses.dataclass",
        f"class {class_name}:",
        "",
    ]
    property_names_orig = json_schema_prop.properties.keys()
    mandatory_props = json_schema_prop.required or []
    props_in_order = sorted(
        property_names_orig, key=lambda p: (p not in mandatory_props, p)
    )
    for prop_name in props_in_order:
        prop = json_schema_prop.properties[prop_name]
        class_def_lines.append(
            prop.attribute_declaration(
                is_required=prop_name in mandatory_props
            )
        )
    return class_def_lines


def get_dataclass_python_code_from_json_schema(
    json_schema: dict, root_property_name: str, root_class_docstring: str = None
):
    the_schema: JsonSchemaProperty = JsonSchemaProperty.from_dict(json_schema)
    the_schema.property_name_path = [root_property_name]
    all_lines = yield_class_definitions_from_json_schema_property(
        the_schema
    )
    all_lines = list(all_lines)
    all_lines.append(["import dataclasses", "import dataclasses_json"])
    all_lines = reversed(all_lines)
    block_str = []
    for block in all_lines:
        block_str.append("\n".join(block))
    module_code = "\n".join(block_str)
    formatted_and_checked_code = black.format_str(module_code, mode=black.FileMode())
    return formatted_and_checked_code, the_schema.get_class_name()


def schema_from_objects(collection: list[dict]):
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})
    for obj in collection:
        builder.add_object(obj)
    return builder.to_schema()
