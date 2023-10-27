import dataclasses
import json
import os.path
from collections import defaultdict
from pathlib import Path
from typing import TypeAlias, Collection

import json5

JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


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


def read_all(gameresources_root_path: str, file_suffixes: Collection[str]) -> dict:
    """Nested dict which mimics the OS folder and file structure."""
    all_resources = defaultdict(list)
    for path, dirnames, filenames in os.walk(gameresources_root_path):
        rel_path = os.path.relpath(path, gameresources_root_path)
        for f in filenames:
            if Path(f).suffix in file_suffixes:
                full_path = os.path.join(path, f)
                r = ResourceFile.from_file_path(gameresources_root_path, full_path)
                all_resources[rel_path].append(r)
    return all_resources


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    extensions_to_consider = (".meta", ".lang")
    all_data = read_all(gameresources_dir, file_suffixes=extensions_to_consider)
    for k, v in all_data.items():
        print(f"Found '{len(v)}' files in '{k}'")
