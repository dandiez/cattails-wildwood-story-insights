import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class BuildingLangGerman:
    """Dataset associated with files in 'gameresources/buildings/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_building_name: str = Undefined
