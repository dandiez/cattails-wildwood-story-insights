import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class FestivalLangGerman:
    """Dataset associated with files in 'gameresources/festivals/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    festival_uid_do_not_translate: str = Undefined
    lang_festival_title: str = Undefined
