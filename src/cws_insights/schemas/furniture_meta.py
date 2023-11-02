import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class FurnitureMeta:
    attachment: str
    is_rotatable: bool
    is_seasonal: bool
    is_solid: bool
    sprite: str
    unlocked: bool
    allow_furniture_ontop: bool = None
    animation_speed: int = None
    blocker_height: int = None
    blocker_height_east: int = None
    blocker_height_north: int = None
    blocker_height_south: int = None
    blocker_height_west: int = None
    blocker_width: int = None
    blocker_width_east: int = None
    blocker_width_north: int = None
    blocker_width_south: int = None
    blocker_width_west: int = None
    blocker_x_mod: int = None
    blocker_x_mod_east: int = None
    blocker_x_mod_north: int = None
    blocker_x_mod_south: int = None
    blocker_x_mod_west: int = None
    blocker_y_mod: int = None
    blocker_y_mod_east: int = None
    blocker_y_mod_north: int = None
    blocker_y_mod_south: int = None
    blocker_y_mod_west: int = None
    crafting_station_uid: str = None
    function: str = None
    is_light: bool = None
    is_table: bool = None
    light_color: list[int] = dataclasses.field(default_factory=list)
    light_intensity: float | int = None
    light_radius: int = None
    light_x_mod: int = None
    light_y_mod: int = None
    tabletop_placement: bool = None
