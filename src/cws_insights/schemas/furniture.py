import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Furniture:
    """Dataset associated with files in 'gameresources/furniture'."""

    _special_mappings: ClassVar[dict] = {}
    allow_furniture_ontop: bool = Undefined
    animation_speed: int = Undefined
    attachment: str = Undefined
    blocker_height: int = Undefined
    blocker_height_east: int = Undefined
    blocker_height_north: int = Undefined
    blocker_height_south: int = Undefined
    blocker_height_west: int = Undefined
    blocker_width: int = Undefined
    blocker_width_east: int = Undefined
    blocker_width_north: int = Undefined
    blocker_width_south: int = Undefined
    blocker_width_west: int = Undefined
    blocker_x_mod: int = Undefined
    blocker_x_mod_east: int = Undefined
    blocker_x_mod_north: int = Undefined
    blocker_x_mod_south: int = Undefined
    blocker_x_mod_west: int = Undefined
    blocker_y_mod: int = Undefined
    blocker_y_mod_east: int = Undefined
    blocker_y_mod_north: int = Undefined
    blocker_y_mod_south: int = Undefined
    blocker_y_mod_west: int = Undefined
    crafting_station_uid: str = Undefined
    function: str = Undefined
    is_light: bool = Undefined
    is_rotatable: bool = Undefined
    is_seasonal: bool = Undefined
    is_solid: bool = Undefined
    is_table: bool = Undefined
    light_color: list = Undefined
    light_intensity: float = Undefined
    light_radius: int = Undefined
    light_x_mod: int = Undefined
    light_y_mod: int = Undefined
    sprite: str = Undefined
    tabletop_placement: bool = Undefined
    unlocked: bool = Undefined
