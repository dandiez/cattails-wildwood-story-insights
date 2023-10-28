import os.path

from slugify import slugify



def slug_it(dirty_str: str) -> str:
    regex_pattern = r"[^-a-z0-9_]+"
    return slugify(
        dirty_str,
        replacements=(("+", "plus"), ("-", "minus"), ("/", "_")),
        regex_pattern=regex_pattern,
    )


