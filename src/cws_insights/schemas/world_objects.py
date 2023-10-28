import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WorldObjects:
    """Dataset associated with files in 'gameresources/world_objects'."""

    build_menu: bool = Undefined
    collisions: bool = Undefined
    sprite_bbox: list = Undefined
    sprite_origin: list = Undefined
    sprites: list = Undefined
    world_object_uid: str = Undefined
