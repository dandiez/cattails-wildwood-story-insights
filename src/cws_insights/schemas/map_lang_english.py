import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MapLangEnglish:
    """Dataset associated with files in 'gameresources/map/lang/english'."""

    lang_region_name: str = Undefined
