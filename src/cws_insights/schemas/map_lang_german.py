import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MapLangGerman:
    """Dataset associated with files in 'gameresources/map/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_region_name: str = Undefined
