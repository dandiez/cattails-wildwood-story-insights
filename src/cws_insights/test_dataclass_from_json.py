import unittest

from cws_insights.dataclass_from_json import (
    get_dataclass_python_code_from_json_schema,
    schema_from_objects,
)


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
        self.assertEqual((expected, "RootClass"), actual)

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
        self.assertEqual((expected, "Root"), actual)

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
    a_simple_list: list[str] = dataclasses.field(default_factory=list)
    an_optional_arg: float | int = None
"""
        actual = get_dataclass_python_code_from_json_schema(
            input_schema, root_class_name
        )
        self.assertEqual((expected, "RootClass"), actual)

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
        self.assertEqual((expected, "RootClass"), actual)

    def test_double_list_and_naming(self):
        record_1 = {
            "a_b": {"c": {"x": 1}, "c_d": {"x": 2}},
            "a": {"b_c": {"x": 3}, "b_c_d": {"x": 4}},
            "k": [[4, 8]],
        }
        record_2 = {
            "a_b": {"c": {"x": 1.23}, "c_d": {"x": 2}},
            "a": {"b_c": {"x": 3}, "b_c_d": {"x": 4}},
            "k": [[7]],
            "m": [[{"p": True}]],
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
    m: list[list[Root_M]] = dataclasses.field(default_factory=list)
"""
        input_schema = schema_from_objects([record_1, record_2])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema,
            root_class_attribute_name,
        )
        self.assertEqual((expected, "Root"), actual)

    def test_empty_list(self):
        record_1 = {"a_b": []}
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    a_b: list
"""
        input_schema = schema_from_objects([record_1])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema,
            root_class_attribute_name,
        )
        self.assertEqual((expected, "Root"), actual)

    def test_illegal_attribute(self):
        record_1 = {"a_+_b": 4}
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    a_plus_b: int = dataclasses.field(
        metadata=dataclasses_json.config(field_name="a_+_b")
    )
"""
        input_schema = schema_from_objects([record_1])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema,
            root_class_attribute_name,
        )
        self.assertEqual((expected, "Root"), actual)

    def test_illegal_attribute_optional(self):
        record_1 = {"a_+_b": 4, "k": 3}
        record_2 = {"k": 5}
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    k: int
    a_plus_b: int = dataclasses.field(
        metadata=dataclasses_json.config(field_name="a_+_b"), default=None
    )
"""
        input_schema = schema_from_objects([record_1, record_2])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema,
            root_class_attribute_name,
        )
        self.assertEqual((expected, "Root"), actual)

    def test_defaults_for_optionals(self):
        record_1 = {"a": 4, "b": False, "c": "hi", "d": ["hi", "there"]}
        record_2 = {}
        expected = """import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class Root:
    a: int = None
    b: bool = None
    c: str = None
    d: list[str] = dataclasses.field(default_factory=list)
"""
        input_schema = schema_from_objects([record_1, record_2])
        root_class_attribute_name = "root"
        actual = get_dataclass_python_code_from_json_schema(
            input_schema,
            root_class_attribute_name,
        )
        self.assertEqual((expected, "Root"), actual)
