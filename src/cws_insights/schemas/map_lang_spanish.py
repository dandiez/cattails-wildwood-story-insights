import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MapLangSpanish:
    """Dataset associated with files in 'gameresources/map/lang/spanish'."""

    _special_mappings: ClassVar[dict] = {}
    lang_region_name: str = Undefined
