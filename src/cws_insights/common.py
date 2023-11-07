import json
import os
import os.path

from slugify import slugify

from cws_insights.read_files import JSON

_THIS_DIR = os.path.dirname(__file__)


def slug_it(dirty_str: str) -> str:
    regex_pattern = r"[^-a-z0-9_]+"
    return slugify(
        dirty_str,
        replacements=(("+", "plus"), ("-", "minus"), ("/", "_")),
        regex_pattern=regex_pattern,
    )


CI_CD_GAMERESOURCES_DIR = os.path.abspath(
    os.path.join(
        _THIS_DIR,
        "..",
        "..",
        "cattails-wildwood-story-gameresources",
        "gameresources",
    )
)
MORE_RESOURCES_PATH = os.path.abspath(
    os.path.join(_THIS_DIR, "..", "..", "more_resources")
)

SITE_SRC_DIR = os.path.abspath(
    os.path.join(
        _THIS_DIR,
        "..",
        "..",
        "_site_src",
    )
)
WIKI_CONTENTS_DIR = os.path.abspath(
    os.path.join(_THIS_DIR, "..", "..", "_wiki_contents")
)


def write_json(data: JSON, file_path: str):
    """Write json file and create folders if needed."""
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
