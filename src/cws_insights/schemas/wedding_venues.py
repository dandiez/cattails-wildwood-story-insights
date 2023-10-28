import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WeddingVenue:
    """Dataset associated with files in 'gameresources/wedding_venues'."""

    _special_mappings: ClassVar[dict] = {}
    officiant_spawn_dir: str = Undefined
    officiant_spawn_x: int = Undefined
    officiant_spawn_y: int = Undefined
    player_spawn_dir: str = Undefined
    player_spawn_x: int = Undefined
    player_spawn_y: int = Undefined
    spouse_destination_x: int = Undefined
    spouse_destination_y: int = Undefined
    spouse_spawn_x: int = Undefined
    spouse_spawn_y: int = Undefined
    wedding_guest_positions: list = Undefined
    wedding_hour_end: int = Undefined
    wedding_hour_start: int = Undefined
    wedding_map_uid: str = Undefined
    wedding_music: str = Undefined
    wedding_world_objects: list = Undefined
