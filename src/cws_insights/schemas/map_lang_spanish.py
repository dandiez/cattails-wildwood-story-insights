import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MapLangSpanish:
    """Dataset associated with files in 'gameresources/map/lang/spanish'."""

    lang_region_name: str = Undefined
