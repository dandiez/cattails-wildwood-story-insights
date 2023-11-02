import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class WeddingVenueMeta_WeddingGuestPositions:
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class WeddingVenueMeta_WeddingWorldObjects:
    type: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class WeddingVenueMeta:
    officiant_spawn_dir: str
    officiant_spawn_x: int
    officiant_spawn_y: int
    player_spawn_dir: str
    player_spawn_x: int
    player_spawn_y: int
    spouse_destination_x: int
    spouse_destination_y: int
    spouse_spawn_x: int
    spouse_spawn_y: int
    wedding_guest_positions: list[WeddingVenueMeta_WeddingGuestPositions]
    wedding_hour_end: int
    wedding_hour_start: int
    wedding_map_uid: str
    wedding_music: str
    wedding_world_objects: list[WeddingVenueMeta_WeddingWorldObjects]
