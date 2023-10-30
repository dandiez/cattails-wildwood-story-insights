import json
import os
import tempfile
import unittest

from cws_insights.common import slug_it
from cws_insights.read_files import ResourceFile, read_all_resource_files, JSON
from cws_insights.update_schemas import (
    KeyAttributeMapper,
    get_all_unique_keys_with_their_types,
    ModuleClassNames,
    IndexModule,
    DataModule,
)


def write_json(data: JSON, file_path: str):
    """Write json file and create folders if needed."""
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f)


class TestReadFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.gamesourcedir = tempfile.TemporaryDirectory()
        self.gamesourcedir_path = self.gamesourcedir.name
        write_json(
            {"name": "Alabaster"},
            os.path.join(self.gamesourcedir_path, "npc", "alabaster.meta"),
        )
        write_json(
            {"lang_name": "Alabaster"},
            os.path.join(
                self.gamesourcedir_path, "npc", "lang", "english", "alabaster.meta"
            ),
        )

    def test_read_all_resource_files(self):
        expected = {
            "npc": [
                ResourceFile(
                    rel_path=os.path.join("npc", "alabaster.meta"),
                    stem="alabaster",
                    extension=".meta",
                    contents={"name": "Alabaster"},
                )
            ],
            "npc/lang/english": [
                ResourceFile(
                    rel_path=os.path.join("npc", "lang", "english", "alabaster.meta"),
                    stem="alabaster",
                    extension=".meta",
                    contents={"lang_name": "Alabaster"},
                )
            ],
        }
        self.assertEqual(
            expected, read_all_resource_files(self.gamesourcedir_path, (".meta",))
        )

    def tearDown(self) -> None:
        self.gamesourcedir.cleanup()


class TestCommon(unittest.TestCase):
    def test_slug_it(self):
        self.assertEqual("a_b", slug_it("a_b"))
        self.assertEqual("a__b__c", slug_it("a__b__c"))
        self.assertEqual("a_plus_b", slug_it("a_+_b"))
        self.assertEqual("a_minus_b", slug_it("a_-_b"))


class TestUpdateSchemas(unittest.TestCase):
    def test_class_name_from_path(self):
        self.assertEqual("NpcLangEnglish", DataModule("npcs/lang/english").class_name)

    def test_dataclass_types_from_set(self):
        self.assertEqual("str", DataModule.get_dataclass_types_as_str({str}))
        self.assertEqual(
            "float|int", DataModule.get_dataclass_types_as_str({float, int})
        )

    def test_key_to_attribute_mapper(self):
        mapper = KeyAttributeMapper()
        attribute_name = mapper.key_to_attribute("this_key_can_be_an_attribute")
        self.assertEqual("this_key_can_be_an_attribute", attribute_name)
        self.assertEqual(dict(), mapper.special_mapping)
        attribute_name = mapper.key_to_attribute("this_key_has_a_+_and_a_-_symbol")
        self.assertEqual("this_key_has_a_plus_and_a_minus_symbol", attribute_name)
        self.assertEqual(
            {
                "this_key_has_a_+_and_a_-_symbol": "this_key_has_a_plus_and_a_minus_symbol"
            },
            mapper.special_mapping,
        )
        _ = mapper.key_to_attribute("a_+_b")
        self.assertEqual(
            {
                "this_key_has_a_+_and_a_-_symbol": "this_key_has_a_plus_and_a_minus_symbol",
                "a_+_b": "a_plus_b",
            },
            mapper.special_mapping,
        )

    def test_get_special_mapping_lines(self):
        mapper = KeyAttributeMapper()
        actual = DataModule.get_special_mapping_lines(mapper)
        self.assertEqual("_special_mappings: ClassVar[dict] = {}", actual)

        mapper = KeyAttributeMapper(
            {
                "a_+_b": "a_plus_b",
                "a_-_b": "a_minus_b",
            }
        )
        actual = DataModule.get_special_mapping_lines(mapper)
        expected = "_special_mappings: ClassVar[dict] = {'a_+_b': 'a_plus_b', 'a_-_b': 'a_minus_b'}"

        self.assertEqual(expected, actual)

    def test_get_dataclass_attribute_definitions_as_str(self):
        key_types = {
            "age": {float, int},
            "name": {str},
            "controller_+_text": {str},
        }
        mappings = KeyAttributeMapper({"controller_+_text": "controller_plus_text"})
        actual = DataModule.get_dataclass_attribute_definitions_as_str(
            key_types, mappings
        )
        expected = """age: float|int = Undefined
    controller_plus_text: str = Undefined
    name: str = Undefined"""
        self.assertEqual(expected, actual)

    def test_get_all_unique_keys_with_their_types(self):
        resources = [
            ResourceFile(
                rel_path="npc",
                stem="alabaster",
                extension=".meta",
                contents={"name": "Alabaster", "age": 5},
            ),
            ResourceFile(
                rel_path="npc",
                stem="something_else",
                extension=".meta",
                contents={"name": "Something else", "age": 4.2, "a_+_b": "42"},
            ),
        ]
        actual = get_all_unique_keys_with_their_types(resources)
        expected = {"name": {str}, "age": {float, int}, "a_+_b": {str}}
        self.assertEqual(expected, actual)

    def test_get_python_module_with_dataclass_as_str(self):
        collection = [
            ResourceFile(
                rel_path="npc",
                stem="alabaster",
                extension=".meta",
                contents={"name": "Alabaster", "age": 5},
            ),
            ResourceFile(
                rel_path="npc",
                stem="something_else",
                extension=".meta",
                contents={"name": "Something else", "age": 4.2, "a_+_b": "42"},
            ),
        ]
        collection_rel_path = "npc/something"
        data_module = DataModule(
            rel_path=collection_rel_path, resource_files=collection
        )
        actual = data_module.get_code()
        expected = '''import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class NpcSomething:
    """Dataset associated with files in \'gameresources/npc/something\'."""

    _special_mappings: ClassVar[dict] = {"a_+_b": "a_plus_b"}
    a_plus_b: str = Undefined
    age: float | int = Undefined
    name: str = Undefined
'''

        self.assertEqual(expected, actual)
        self.assertEqual("NpcSomething", data_module.class_name)
        self.assertEqual("npc_something", data_module.module_name)

    def test_get_python_module_with_dataclass_as_str_empty_mappings(self):
        collection = [
            ResourceFile(
                rel_path="npc",
                stem="alabaster",
                extension=".meta",
                contents={"name": "Alabaster", "age": 5},
            ),
        ]
        collection_rel_path = "npc/something"
        data_module = DataModule(
            rel_path=collection_rel_path, resource_files=collection
        )
        actual = data_module.get_code()
        expected = '''import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class NpcSomething:
    """Dataset associated with files in \'gameresources/npc/something\'."""

    _special_mappings: ClassVar[dict] = {}
    age: int = Undefined
    name: str = Undefined
'''
        self.assertEqual(expected, actual)

    def test_get_index_module_code(self):
        index = IndexModule(
            {
                "npcs": ModuleClassNames(module_name="npcs", class_name="Npcs"),
                "npcs/lang/english": ModuleClassNames(
                    module_name="npcs_lang_english", class_name="NpcsLangEnglish"
                ),
            }
        )
        actual = index.get_code()
        expected = '''import dataclasses

from cws_insights.schemas.npcs import Npcs
from cws_insights.schemas.npcs_lang_english import NpcsLangEnglish

COLLECTION_REL_PATH_TO_DATACLASS_MAPPING = {
    "npcs": Npcs,
    "npcs/lang/english": NpcsLangEnglish,
}

COLLECTION_REL_PATH_TO_VARIABLE_MAPPING = {
    "npcs": "npcs",
    "npcs/lang/english": "npcs_lang_english",
}


@dataclasses.dataclass
class AllResourceData:
    """All resource data indexed by file stem."""

    npcs: dict[str, Npcs] = None
    npcs_lang_english: dict[str, NpcsLangEnglish] = None
'''
        self.assertEqual(expected, actual)
