import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class BuildingsLangEnglish:
    """Dataset associated with files in 'gameresources/buildings/lang/english'."""

    lang_building_name: str = Undefined
