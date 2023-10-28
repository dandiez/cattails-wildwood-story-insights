import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class BuildingsLangGerman:
    """Dataset associated with files in 'gameresources/buildings/lang/german'."""

    lang_building_name: str = Undefined
