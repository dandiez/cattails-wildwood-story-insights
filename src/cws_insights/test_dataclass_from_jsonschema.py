import dataclasses
import json
import os
import unittest
from typing import Literal

import black
from genson import SchemaBuilder

from cws_insights.common import slug_it

from dataclasses_json import Undefined
from dataclasses_json import dataclass_json

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
            return f"list[{self.items.type_as_string()}]"
        if self.type == "object":
            return self.get_class_name()
        raise ValueError(self.type)

    def attribute_declaration(self, is_required: bool):
        prop_name = self.property_name
        slugged = slug_it(prop_name)
        if slugged != prop_name and not is_required:
            addendum = f"= dataclasses.field(metadata=dataclasses_json.config(field_name={slugged}), default=None)"
        elif slugged != prop_name and is_required:
            addendum = f"= dataclasses.field(metadata=dataclasses_json.config(field_name={slugged}))"
        elif not is_required:
            addendum = f"= None"
        else:
            addendum = ""
        return f"    {slugged}: {self.type_as_string()} {addendum}"

    def yield_contained_objects_and_populate_paths(self) -> tuple[list[str], "JsonSchemaProperty"]:
        path = self.property_name_path
        if self.type == "array":
            prop = self.items
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
    the_schema = JsonSchemaProperty.from_dict(json_schema)
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
    return formatted_and_checked_code

def schema_from_objects(collection: list[dict]):
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})
    for obj in collection:
        builder.add_object(obj)
    return builder.to_schema()

class TestDataclassFromJson(unittest.TestCase):
    def test_simple(self):
        input_schema = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {"lang_building_name": {"type": "string"}},
            "required": ["lang_building_name"],
        }
        root_class_name = "root_class"
        root_class_docstring = "RootClass docstring."
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass:
    lang_building_name: str
"""
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_name, root_class_docstring
        )
        self.assertEqual(expected, actual)

    def test_nested(self):
        input_schema = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "lang_building_name": {"type": "string"},
                "nested": {
                    "type": "object",
                    "properties": {
                        "a_optional": {"type": "string"},
                        "x_mand": {"type": "integer"},
                    },
                    "required": [
                        "x_mand",
                    ],
                },
            },
            "required": ["lang_building_name"],
        }
        root_class_name = "root"
        root_class_docstring = "RootClass docstring."
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_Nested:
    x_mand: int
    a_optional: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    lang_building_name: str
    nested: Root_Nested = None
"""
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_name, root_class_docstring
        )
        self.assertEqual(expected, actual)

    def test_complex(self):
        input_schema = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "a_mandatory_arg": {"type": "string"},
                "an_optional_arg": {"type": "number"},
                "another_mandatory_arg": {"type": "string"},
                "a_simple_list": {"type": "array", "items": {"type": "string"}},
                "a_mandatory_list_with_object": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "a_optional": {"type": "string"},
                            "x_mand": {"type": "integer"},
                        },
                        "required": [
                            "x_mand",
                        ],
                    },
                },
            },
            "required": [
                "a_mandatory_arg",
                "another_mandatory_arg",
                "a_mandatory_list_with_object",
            ],
        }
        root_class_name = "root_class"
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass_AMandatoryListWithObject:
    x_mand: int
    a_optional: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass:
    a_mandatory_arg: str
    a_mandatory_list_with_object: list[RootClass_AMandatoryListWithObject]
    another_mandatory_arg: str
    a_simple_list: list[str] = None
    an_optional_arg: float | int = None
"""
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_name
        )
        self.assertEqual(expected, actual)

    def test_double_nested(self):
        input_schema = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "lang_building_name": {"type": "string"},
                "nested": {
                    "type": "object",
                    "properties": {
                        "a_optional": {"type": "string"},
                        "x_mand": {"type": "integer"},
                        "nested": {
                            "type": "object",
                            "properties": {
                                "b_not_optional": {"type": "string"},
                                "x": {"type": "integer"},
                            },
                            "required": [
                                "b_not_optional",
                            ],
                        },
                    },
                    "required": [
                        "x_mand",
                    ],
                },
            },
            "required": ["lang_building_name"],
        }
        root_class_name = "root_class"
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass_Nested_Nested:
    b_not_optional: str
    x: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass_Nested:
    x_mand: int
    a_optional: str = None
    nested: RootClass_Nested_Nested = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RootClass:
    lang_building_name: str
    nested: RootClass_Nested = None
"""
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_name
        )
        self.assertEqual(expected, actual)

    def test_double_list_and_naming(self):
        record_1 = {
            "a_b": {"c": {"x":1}, "c_d": {"x":2}},
            "a": {"b_c": {"x":3}, "b_c_d": {"x":4}},
            "k": [
                [
                    4, 8
                ]
            ]
        }
        record_2 = {
            "a_b": {"c": {"x":1.23}, "c_d": {"x":2}},
            "a": {"b_c": {"x":3}, "b_c_d": {"x":4}},
            "k": [
                [

                ]
            ],
            "m":[[{"p":True}]]
        }
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_M:
    p: bool


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_A_BCD:
    x: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_A_BC:
    x: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_A:
    b_c: Root_A_BC
    b_c_d: Root_A_BCD


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_AB_CD:
    x: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_AB_C:
    x: float | int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root_AB:
    c: Root_AB_C
    c_d: Root_AB_CD


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    a: Root_A
    a_b: Root_AB
    k: list[list[int]]
    m: list[list[Root_M]] = None
"""
        input_schema = schema_from_objects([record_1, record_2])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_attribute_name,
        )
        self.assertEqual(expected, actual)


