import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapRegion_RegionData_WorldObjects:
    type: str
    x: int
    y: int
    plate_1_x: int = None
    plate_1_y: int = None
    plate_2_x: int = None
    plate_2_y: int = None
    plate_3_x: int = None
    plate_3_y: int = None
    plate_4_x: int = None
    plate_4_y: int = None
    plate_5_x: int = None
    plate_5_y: int = None
    power_paw_index: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapRegion_RegionData_Spawners:
    item_uids: list[str]
    percent_chance: int
    type: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapRegion_RegionData_NpcDenFurniture:
    direction: str
    uid: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapRegion_RegionData:
    allow_daily_battles: bool
    background_type: str
    cliff_tiles: list
    custom_sprites: list
    decorative_tiles: list
    herbs_list: list[str]
    interior: bool
    max_bugs: int
    max_herbs: int
    max_mushrooms: int
    max_npc_fighters: int
    max_prey: int
    max_voidlings: int
    pass_time: bool
    path_tiles: list
    prey_list: list[str]
    region_battle_music: str
    region_coordinate: list[int]
    region_music: str
    show_festival_tokens: bool
    show_influence: bool
    show_mews: bool
    show_mole_cash: bool
    show_task_tokens: bool
    spawn_beetles: bool
    spawn_butterflies: bool
    spawn_dragonflies: bool
    spawn_fireflies: bool
    spawn_ladybugs: bool
    spawn_moths: bool
    spawners: list[MapRegion_RegionData_Spawners]
    stair_tiles: list
    template: str
    warps: list
    water_tiles: list
    world_map_portrait_coordinate: list[int]
    world_objects: list[MapRegion_RegionData_WorldObjects]
    audio_ambience: str = None
    influence_locked: bool = None
    influence_map_height: int = None
    influence_map_width: int = None
    is_npc_den: bool = None
    npc_den_floor_style: int = None
    npc_den_furniture: list[MapRegion_RegionData_NpcDenFurniture] = dataclasses.field(
        default_factory=list
    )
    npc_den_grid: list[list[int]] = dataclasses.field(default_factory=list)
    npc_den_wall_style: int = None
    player_colony_owns_region: bool = None
    player_colony_starting_influence: float | int = None
    region_resource: str = None
    region_resource_quantity: int = None
    wake_y: int = None
    water_can_freeze: bool = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapRegion:
    region_data: MapRegion_RegionData
