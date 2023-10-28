import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Map:
    """Dataset associated with files in 'gameresources/map'."""

    _special_mappings: ClassVar[dict] = {}
    assign_squads_npc: str = Undefined
    darkruins1_region: str = Undefined
    darkruins1_x: int = Undefined
    darkruins1_y: int = Undefined
    darkruins2_region: str = Undefined
    darkruins2_x: int = Undefined
    darkruins2_y: int = Undefined
    darkruins3_region: str = Undefined
    darkruins3_x: int = Undefined
    darkruins3_y: int = Undefined
    darkruins4_region: str = Undefined
    darkruins4_x: int = Undefined
    darkruins4_y: int = Undefined
    doctor_respawn_coordinate: list = Undefined
    doctor_respawn_dir: str = Undefined
    doctor_respawn_npc: str = Undefined
    map_size_horizontal: int = Undefined
    map_size_vertical: int = Undefined
    respawn_coordinate: list = Undefined
    respawn_dir: str = Undefined
    respawn_region_uid: str = Undefined
    start_player_coordinate: list = Undefined
    start_region_coordinate: list = Undefined
    warp_northeast_region: str = Undefined
    warp_northeast_x: int = Undefined
    warp_northeast_y: int = Undefined
    warp_northwest_region: str = Undefined
    warp_northwest_x: int = Undefined
    warp_northwest_y: int = Undefined
    warp_southeast_region: str = Undefined
    warp_southeast_x: int = Undefined
    warp_southeast_y: int = Undefined
    warp_southwest_region: str = Undefined
    warp_southwest_x: int = Undefined
    warp_southwest_y: int = Undefined
    wedding_officiant_npc: str = Undefined
