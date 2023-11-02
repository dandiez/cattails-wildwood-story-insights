import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapMeta:
    assign_squads_npc: str
    darkruins1_region: str
    darkruins1_x: int
    darkruins1_y: int
    darkruins2_region: str
    darkruins2_x: int
    darkruins2_y: int
    darkruins3_region: str
    darkruins3_x: int
    darkruins3_y: int
    darkruins4_region: str
    darkruins4_x: int
    darkruins4_y: int
    doctor_respawn_coordinate: list[int]
    doctor_respawn_dir: str
    doctor_respawn_npc: str
    map_size_horizontal: int
    map_size_vertical: int
    respawn_coordinate: list[int]
    respawn_dir: str
    respawn_region_uid: str
    start_player_coordinate: list[int]
    start_region_coordinate: list[int]
    warp_northeast_region: str
    warp_northeast_x: int
    warp_northeast_y: int
    warp_northwest_region: str
    warp_northwest_x: int
    warp_northwest_y: int
    warp_southeast_region: str
    warp_southeast_x: int
    warp_southeast_y: int
    warp_southwest_region: str
    warp_southwest_x: int
    warp_southwest_y: int
    wedding_officiant_npc: str
