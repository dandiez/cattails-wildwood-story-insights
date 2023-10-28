import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class BuildingsLangSpanish:
    """Dataset associated with files in 'gameresources/buildings/lang/spanish'."""

    lang_building_name: str = Undefined
