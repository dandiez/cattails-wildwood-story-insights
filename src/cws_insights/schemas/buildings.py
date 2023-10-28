import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Building:
    """Dataset associated with files in 'gameresources/buildings'."""

    _special_mappings: ClassVar[dict] = {}
    blocker_height: int = Undefined
    blocker_width: int = Undefined
    build_menu: bool = Undefined
    building_type: str = Undefined
    decor_sprite: str = Undefined
    interior_region_id: str = Undefined
    interior_warp_x: int = Undefined
    interior_warp_y: int = Undefined
    lock_dialog_key: str = Undefined
    npc_lock_list: list = Undefined
    sprite: str = Undefined
    unlocked: bool = Undefined
