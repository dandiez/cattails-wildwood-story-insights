import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class BuildingLangEnglish:
    """Dataset associated with files in 'gameresources/buildings/lang/english'."""

    _special_mappings: ClassVar[dict] = {}
    lang_building_name: str = Undefined
