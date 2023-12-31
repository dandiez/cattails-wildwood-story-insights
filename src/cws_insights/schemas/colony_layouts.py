import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ColonyLayout:
    """Dataset associated with files in 'gameresources/colony_layouts'."""

    _special_mappings: ClassVar[dict] = {}
    background_type: str = Undefined
    buildings: list = Undefined
    decorative_tiles: list = Undefined
    path_tiles: list = Undefined
    player_den_starting_sprite: str = Undefined
    water_tiles: list = Undefined
    world_objects: list = Undefined
