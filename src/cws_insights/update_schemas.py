"""Write the schemas as dataclasses from inspecting the gameresources files."""
import dataclasses
import os.path
from collections import defaultdict
from typing import Collection

import black
import inflect

from cws_insights.common import slug_it
from cws_insights.dataclass_from_json import (
    schema_from_objects,
    get_dataclass_python_code_from_json_schema,
)
from cws_insights.read_files import (
    read_all_resource_files,
    ResourceFile,
    ResourcesRelPath,
)

SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), "schemas")


@dataclasses.dataclass
class ModuleClassNames:
    module_name: str
    class_name: str


@dataclasses.dataclass
class ClassDefinition:
    full_class_code: str
    class_name: str


@dataclasses.dataclass
class IndexModule:
    """Data and methods to produce schemas/_index.py."""

    _map: dict[ResourcesRelPath, ModuleClassNames] = dataclasses.field(
        default_factory=dict
    )

    def __setitem__(self, key, item):
        self._map[key] = item

    def write(self, schemas_dir: str, file_name="_index.py"):
        module_as_str = self.get_code()
        with open(os.path.join(schemas_dir, file_name), "w") as f:
            f.write(module_as_str)

    def get_code(self) -> str:
        self._sort_mapping()
        module_as_str = f"""import dataclasses

{self._get_imports()}

{self._get_path_to_class_map()}

{self._get_path_to_var_map()}

{self._get_index_dataclass()}
"""
        module_as_str = black.format_str(module_as_str, mode=black.FileMode())
        return module_as_str

    def _sort_mapping(self):
        self._map = {
            k: v for k, v in sorted(self._map.items(), key=lambda item: item[0])
        }

    def _get_imports(self):
        return "\n".join(
            [
                f"from cws_insights.schemas.{module_class_names.module_name} import {module_class_names.class_name}"
                for module_class_names in self._map.values()
            ]
        )

    def _get_path_to_class_map(self) -> str:
        collection_rel_path_to_dataclass_mapping = "\n".join(
            [
                f"    '{rel_path}':{module_and_class_name.class_name},"
                for rel_path, module_and_class_name in self._map.items()
            ]
        )
        collection_rel_path_to_dataclass_mapping_str = (
            "COLLECTION_REL_PATH_TO_DATACLASS_MAPPING={\n"
            + collection_rel_path_to_dataclass_mapping
            + "}"
        )
        return collection_rel_path_to_dataclass_mapping_str

    def _get_path_to_var_map(self):
        collection_rel_path_to_variable_mapping = "\n".join(
            [
                f"    '{rel_path}':'{module_and_class_name.module_name}',"
                for rel_path, module_and_class_name in self._map.items()
            ]
        )
        collection_rel_path_to_variable_mapping_str = (
            "COLLECTION_REL_PATH_TO_VARIABLE_MAPPING={\n"
            + collection_rel_path_to_variable_mapping
            + "}"
        )
        return collection_rel_path_to_variable_mapping_str

    def _get_index_dataclass(self):
        attribute_lines = [
            f"    {mcn.module_name}: dict[str, {mcn.class_name}] = None"
            for mcn in self._map.values()
        ]
        all_attribute_lines_as_str = "\n".join(attribute_lines)
        def_as_str = f'''@dataclasses.dataclass
class AllResourceData:
    """All resource data indexed by file stem."""

{all_attribute_lines_as_str}
'''
        return def_as_str


@dataclasses.dataclass
class KeyAttributeMapper:
    """Manage the dict keys to valid python attributes conversion and tracking."""

    special_mapping: dict = dataclasses.field(default_factory=dict)

    def key_to_attribute(self, key: str):
        """Get the python attribute corresponding to a given json key.

        Also keep track of those keys that had to be sluggified to be valid python attributes.
        """
        slugged = slug_it(key)
        if slugged == key:
            return key
        if slugged in self.special_mapping:
            if self.special_mapping[slugged] != key:
                raise ValueError(
                    f"Cannot have two keys '{self.special_mapping[slugged]}' and '{key}' mapping to the same attribute '{slugged}'."
                )
        self.special_mapping[key] = slugged
        return slugged


@dataclasses.dataclass
class DataModule:
    """Data and methods to produce schemas/[dataset].py."""

    rel_path: ResourcesRelPath = None
    resource_files: list[ResourceFile] = None
    class_name: str = None

    @property
    def module_name(self):
        return slug_it(self.rel_path.lower())

    def get_root_property_name(self) -> str:
        parts = self.rel_path.replace("_", "/").split("/")
        inflect_engine = inflect.engine()
        parts = [inflect_engine.singular_noun(word) or word for word in parts]
        small_case = [p.lower() for p in parts]
        return "_".join(small_case)

    def write(self, schemas_dir: str):
        """Write the module py file containing the dataclass code."""
        dataclass_code = self.get_code()
        file_path = os.path.join(schemas_dir, self.module_name + ".py")
        with open(file_path, "w") as f:
            f.write(dataclass_code)

    def get_code(self) -> str:
        records = [obj.contents for obj in self.resource_files]
        schema = schema_from_objects(records)
        module_code, class_name = get_dataclass_python_code_from_json_schema(
            json_schema=schema, root_property_name=self.get_root_property_name()
        )
        self.class_name = class_name
        return module_code


def main(
    gameresources_dir: str, extensions_to_consider: Collection[str], schemas_dir: str
):
    all_data = read_all_resource_files(
        gameresources_dir, file_suffixes=extensions_to_consider
    )
    clean_schemas_dir(schemas_dir)
    index = IndexModule()
    for collection_rel_path, collection in all_data.items():
        data_module = DataModule(collection_rel_path, collection)
        data_module.write(schemas_dir)
        index[collection_rel_path] = ModuleClassNames(
            module_name=data_module.module_name, class_name=data_module.class_name
        )
    index.write(schemas_dir)


def clean_schemas_dir(schemas_dir: str):
    """Wipe all py files from the schemas dir and initialise it with an __init__.py."""
    files = os.listdir(schemas_dir)
    for file_name in files:
        if file_name.endswith(".py"):
            os.remove(os.path.join(schemas_dir, file_name))
    with open(os.path.join(schemas_dir, "__init__.py"), "w") as f:
        f.write('"""Autogenerated schemas based on gameresources files."""\n')


def get_all_unique_keys_with_their_types(collection: list[ResourceFile]):
    """Go through all resource files in a collection and get all unique keys and their types."""
    key_types = defaultdict(set)
    for f in collection:
        for k, v in f.contents.items():
            key_types[k].add(type(v))
    return key_types


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    extensions_to_consider = (".meta", ".lang", ".region")
    schemas_dir = SCHEMAS_DIR
    main(gameresources_dir, extensions_to_consider, schemas_dir)
