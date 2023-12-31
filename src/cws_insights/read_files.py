import dataclasses
import json
import os.path
from collections import defaultdict
from pathlib import Path
from typing import TypeAlias, Collection

import json5

from cws_insights.schemas._index import (
    AllResourceData,
    COLLECTION_REL_PATH_TO_VARIABLE_MAPPING,
    COLLECTION_REL_PATH_TO_DATACLASS_MAPPING,
)

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
ResourcesRelPath: TypeAlias = str


def read_as_json(file_path: str):
    """Read a C.W.S. file as if it were a json."""
    try:
        # fast but fails when there are trailing commas
        with open(file_path, encoding="utf8") as f:
            return json.load(f)
    except Exception:
        with open(file_path, encoding="utf8") as f:
            return json5.load(f)


@dataclasses.dataclass
class ResourceFile:
    """Represents a game resource file."""

    rel_path: str
    stem: str
    extension: str
    contents: JSON

    @classmethod
    def from_file_path(cls, gameresources_root_path, full_path):
        return cls(
            rel_path=os.path.relpath(full_path, gameresources_root_path),
            stem=Path(full_path).stem,
            extension=Path(full_path).suffix,
            contents=read_as_json(file_path=full_path),
        )


AllResourceFiles: TypeAlias = dict[ResourcesRelPath, list[ResourceFile]]


def read_all_resource_files(
    gameresources_root_path: str, file_suffixes: Collection[str]
) -> AllResourceFiles:
    """Nested dict which mimics the OS folder and file structure."""
    all_resources = defaultdict(list)
    for path, dirnames, filenames in os.walk(gameresources_root_path):
        rel_path = os.path.relpath(path, gameresources_root_path)
        rel_path = "/".join(
            os.path.normpath(rel_path).split(os.path.sep)
        )  # consistent win/linux
        for f in filenames:
            if Path(f).suffix in file_suffixes:
                full_path = os.path.join(path, f)
                r = ResourceFile.from_file_path(gameresources_root_path, full_path)
                all_resources[rel_path].append(r)
    return all_resources


def instantiate_all_resource_data(
    all_resource_files: AllResourceFiles,
) -> AllResourceData:
    all_data = AllResourceData()
    for rel_path, files in all_resource_files.items():
        attribute = COLLECTION_REL_PATH_TO_VARIABLE_MAPPING[rel_path]
        class_type = COLLECTION_REL_PATH_TO_DATACLASS_MAPPING[rel_path]
        setattr(
            all_data,
            attribute,
            {
                f.stem: instantiate_resource_data_from_dict(class_type, f.contents)
                for f in files
            },
        )
    return all_data


def instantiate_resource_data_from_dict(class_type: type, data_dict: dict):
    """If the class type has the special mappings defined, use them."""
    return class_type(
        **{class_type._special_mappings.get(k, k): v for k, v in data_dict.items()}
    )


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    extensions_to_consider = (".meta", ".lang")
    all_raw_data = read_all_resource_files(
        gameresources_dir, file_suffixes=extensions_to_consider
    )
    for k, v in all_raw_data.items():
        print(f"Found '{len(v)}' files in '{k}'")
    all_data = instantiate_all_resource_data(all_raw_data)
