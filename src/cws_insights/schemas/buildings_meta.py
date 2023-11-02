import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class BuildingMeta:
    blocker_height: int
    blocker_width: int
    build_menu: bool
    building_type: str
    decor_sprite: str
    interior_region_id: str
    interior_warp_x: int
    interior_warp_y: int
    lock_dialog_key: str
    npc_lock_list: list[str]
    sprite: str
    unlocked: bool
