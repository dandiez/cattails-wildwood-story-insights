import os.path

from slugify import slugify

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
SITE_SRC_DIR = os.path.abspath(
    os.path.join(
        _THIS_DIR,
        "..",
        "..",
        "_site_src",
    )
)
