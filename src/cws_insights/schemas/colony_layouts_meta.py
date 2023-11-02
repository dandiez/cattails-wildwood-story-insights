import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta_DecorativeTiles:
    tile_index: int
    tile_x: int
    tile_y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta_WaterTiles:
    tile_x: int
    tile_y: int
    type: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta_PathTiles:
    tile_x: int
    tile_y: int
    type: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta_WorldObjects:
    uid: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta_Buildings:
    uid: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutMeta:
    background_type: str
    buildings: list[ColonyLayoutMeta_Buildings]
    decorative_tiles: list[ColonyLayoutMeta_DecorativeTiles]
    path_tiles: list[ColonyLayoutMeta_PathTiles]
    player_den_starting_sprite: str
    water_tiles: list[ColonyLayoutMeta_WaterTiles]
    world_objects: list[ColonyLayoutMeta_WorldObjects]
