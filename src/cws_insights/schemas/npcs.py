import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Npc:
    """Dataset associated with files in 'gameresources/npcs'."""

    _special_mappings: ClassVar[dict] = {}
    dialog_objects: list = Undefined
    intro_dialog_objects: list = Undefined
    npc_accessories: list = Undefined
    npc_appearance_ears: str = Undefined
    npc_appearance_face: str = Undefined
    npc_appearance_tail: str = Undefined
    npc_appearance_torso: str = Undefined
    npc_birthday_day: int = Undefined
    npc_birthday_season: str = Undefined
    npc_buddy_system_active_trait: str = Undefined
    npc_buddy_system_enabled: bool = Undefined
    npc_buddy_system_passive_trait: str = Undefined
    npc_can_be_festival_opponent: bool = Undefined
    npc_cat_voice: int = Undefined
    npc_cat_voice_pitch_modifier: float | int = Undefined
    npc_colors_belly: list = Undefined
    npc_colors_ear_outer_left: list = Undefined
    npc_colors_ear_outer_right: list = Undefined
    npc_colors_ears_inner: list = Undefined
    npc_colors_eyes_left: list = Undefined
    npc_colors_eyes_right: list = Undefined
    npc_colors_face: list = Undefined
    npc_colors_face_stripes: list = Undefined
    npc_colors_feet: list = Undefined
    npc_colors_muzzle: list = Undefined
    npc_colors_nose: list = Undefined
    npc_colors_patches_one: list = Undefined
    npc_colors_patches_two: list = Undefined
    npc_colors_paw_back_one: list = Undefined
    npc_colors_paw_back_two: list = Undefined
    npc_colors_paw_front_one: list = Undefined
    npc_colors_paw_front_two: list = Undefined
    npc_colors_point: list = Undefined
    npc_colors_rosettes: list = Undefined
    npc_colors_speckles: list = Undefined
    npc_colors_stripes: list = Undefined
    npc_colors_stripes_two: list = Undefined
    npc_colors_tail: list = Undefined
    npc_colors_tail_tip: list = Undefined
    npc_colors_torso: list = Undefined
    npc_direction: str = Undefined
    npc_enabled: bool = Undefined
    npc_festival_games: list = Undefined
    npc_festival_shop_uid: str = Undefined
    npc_friendship_difficulty_modifier: float = Undefined
    npc_has_colony_options: bool = Undefined
    npc_has_healing: bool = Undefined
    npc_has_influence_options: bool = Undefined
    npc_has_museum_donate: bool = Undefined
    npc_has_name_change: bool = Undefined
    npc_has_shop: bool = Undefined
    npc_is_befriendable: bool = Undefined
    npc_is_datable: bool = Undefined
    npc_is_kitten: bool = Undefined
    npc_item_dislikes: list = Undefined
    npc_item_gifts: list = Undefined
    npc_item_hates: list = Undefined
    npc_item_likes: list = Undefined
    npc_item_loves: list = Undefined
    npc_loyalty: str = Undefined
    npc_map_uid: str = Undefined
    npc_mole_appearance: str = Undefined
    npc_schedule: list = Undefined
    npc_shop_uid: str = Undefined
    npc_show_friendship_rank: bool = Undefined
    npc_spirit_appearance: str = Undefined
    npc_spirit_voice: str = Undefined
    npc_starting_dating_rank: int = Undefined
    npc_starting_friendship_rank: int = Undefined
    npc_starting_marriage_rank: int = Undefined
    npc_type: str = Undefined
    npc_wedding_guest_override_list: list = Undefined
    npc_x: int = Undefined
    npc_y: int = Undefined
