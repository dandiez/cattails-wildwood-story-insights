import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class CraftingStation:
    """Dataset associated with files in 'gameresources/crafting_stations'."""

    _special_mappings: ClassVar[dict] = {}
    recipes_list: list = Undefined
