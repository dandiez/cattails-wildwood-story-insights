import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class CraftingStations:
    """Dataset associated with files in 'gameresources/crafting_stations'."""

    recipes_list: list = Undefined
