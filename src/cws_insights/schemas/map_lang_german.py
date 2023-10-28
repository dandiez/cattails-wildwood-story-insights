import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MapLangGerman:
    """Dataset associated with files in 'gameresources/map/lang/german'."""

    lang_region_name: str = Undefined
