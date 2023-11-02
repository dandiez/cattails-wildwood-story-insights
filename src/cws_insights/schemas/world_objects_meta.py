import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class WorldObjectMeta:
    build_menu: bool
    sprite_bbox: list[int]
    sprite_origin: list[int]
    sprites: list[str]
    world_object_uid: str
    collisions: bool = None
