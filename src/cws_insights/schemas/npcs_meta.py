import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_NpcFestivalGames:
    festival_uid: str
    game_id: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_DialogObjects_DialogFilters:
    filter_accessory_equipped: str = None
    filter_autumn: bool = None
    filter_birthday: bool = None
    filter_blizzard: bool = None
    filter_dating: int = None
    filter_dating_max: int = None
    filter_fog: bool = None
    filter_friendship: int = None
    filter_friendship_max: int = None
    filter_has_kittens: bool = None
    filter_has_met_alabaster: bool = None
    filter_has_met_aster: bool = None
    filter_has_met_aurora: bool = None
    filter_has_met_basil: bool = None
    filter_has_met_bubby: bool = None
    filter_has_met_buttercup: bool = None
    filter_has_met_champ: bool = None
    filter_has_met_charlotte: bool = None
    filter_has_met_coco: bool = None
    filter_has_met_elli: bool = None
    filter_has_met_ember: bool = None
    filter_has_met_garlic: bool = None
    filter_has_met_glimmer: bool = None
    filter_has_met_jack: bool = None
    filter_has_met_jag: bool = None
    filter_has_met_krampy: bool = None
    filter_has_met_lainey: bool = None
    filter_has_met_lux: bool = None
    filter_has_met_phantom: bool = None
    filter_has_met_rosemary: bool = None
    filter_has_met_salem: bool = None
    filter_has_met_spark: bool = None
    filter_has_met_talon: bool = None
    filter_has_met_zephyr: bool = None
    filter_hour: int = None
    filter_hour_max: int = None
    filter_is_at_festival: bool = None
    filter_is_in_den: bool = None
    filter_is_inside: bool = None
    filter_is_ngp: bool = None
    filter_kitten_age: int = None
    filter_kitten_age_max: int = None
    filter_map_uid_bobden: bool = None
    filter_map_uid_buttercupden: bool = None
    filter_map_uid_champden: bool = None
    filter_map_uid_cocoden: bool = None
    filter_map_uid_eastcentral: bool = None
    filter_map_uid_emberandsparkden: bool = None
    filter_map_uid_festivalplaza: bool = None
    filter_map_uid_flissandlaineyden: bool = None
    filter_map_uid_garlicden: bool = None
    filter_map_uid_glimmerden: bool = None
    filter_map_uid_krampyden: bool = None
    filter_map_uid_molecave: bool = None
    filter_map_uid_playercolony: bool = None
    filter_map_uid_talonden: bool = None
    filter_map_uid_temple: bool = None
    filter_map_uid_westcentral: bool = None
    filter_marriage: int = None
    filter_marriage_max: int = None
    filter_npc_is_present_fliss: bool = None
    filter_npc_is_present_krampy: bool = None
    filter_npc_is_present_lainey: bool = None
    filter_npc_is_present_spark: bool = None
    filter_npc_is_present_talon: bool = None
    filter_npc_sitting: bool = None
    filter_npc_x_max: int = None
    filter_npc_x_min: int = None
    filter_npc_y_max: int = None
    filter_npc_y_min: int = None
    filter_player_birthday: bool = None
    filter_player_health_max: int = None
    filter_player_hunger_max: int = None
    filter_player_is_dating: bool = None
    filter_player_is_dating_buttercup: bool = None
    filter_player_is_dating_champ: bool = None
    filter_player_is_dating_charlotte: bool = None
    filter_player_is_dating_coco: bool = None
    filter_player_is_dating_elli: bool = None
    filter_player_is_dating_ember: bool = None
    filter_player_is_dating_glimmer: bool = None
    filter_player_is_dating_krampy: bool = None
    filter_player_is_dating_rosemary: bool = None
    filter_player_is_dating_spark: bool = None
    filter_player_is_dating_theforestguardian: bool = None
    filter_player_is_married: bool = None
    filter_player_is_married_to_alabaster: bool = None
    filter_player_is_married_to_bob: bool = None
    filter_player_is_married_to_buttercup: bool = None
    filter_player_is_married_to_champ: bool = None
    filter_player_is_married_to_charlotte: bool = None
    filter_player_is_married_to_coco: bool = None
    filter_player_is_married_to_elli: bool = None
    filter_player_is_married_to_ember: bool = None
    filter_player_is_married_to_fliss: bool = None
    filter_player_is_married_to_garlic: bool = None
    filter_player_is_married_to_glimmer: bool = None
    filter_player_is_married_to_jag: bool = None
    filter_player_is_married_to_krampy: bool = None
    filter_player_is_married_to_lainey: bool = None
    filter_player_is_married_to_phantom: bool = None
    filter_player_is_married_to_rosemary: bool = None
    filter_player_is_married_to_spark: bool = None
    filter_player_is_married_to_talon: bool = None
    filter_player_is_married_to_theforestguardian: bool = None
    filter_player_is_married_to_zephyr: bool = None
    filter_rain: bool = None
    filter_rival_marriage_completed_alabasterandfliss: bool = None
    filter_rival_marriage_completed_bobandbuttercup: bool = None
    filter_rival_marriage_completed_elliandchamp: bool = None
    filter_rival_marriage_completed_krampyandtalon: bool = None
    filter_rival_marriage_completed_sparkandlainey: bool = None
    filter_season_day: int = None
    filter_season_day_max: int = None
    filter_snow: bool = None
    filter_spring: bool = None
    filter_storm: bool = None
    filter_summer: bool = None
    filter_sun: bool = None
    filter_time: str = None
    filter_wc_fate: int = None
    filter_winter: bool = None
    filter_year: int = None
    filter_year_max: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_DialogObjects:
    dialog_filters: NpcMeta_DialogObjects_DialogFilters
    dialog_lang_key: str
    dialog_unique: bool
    dialog_weight: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_IntroDialogObjects_DialogFilters:
    filter_birthday: bool = None
    filter_cave_index: int = None
    filter_dating: int = None
    filter_dating_max: int = None
    filter_friendship: int = None
    filter_friendship_max: int = None
    filter_is_at_festival: bool = None
    filter_kitten_age: int = None
    filter_kitten_age_max: int = None
    filter_marriage: int = None
    filter_marriage_max: int = None
    filter_mine_level: int = None
    filter_mine_stairs_found: bool = None
    filter_mine_three_unlocked: bool = None
    filter_mine_two_unlocked: bool = None
    filter_ngp_parent: str = None
    filter_player_birthday: bool = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_IntroDialogObjects:
    dialog_filters: NpcMeta_IntroDialogObjects_DialogFilters
    dialog_lang_key: str
    dialog_unique: bool
    dialog_weight: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta_NpcSchedule:
    behavior: str
    direction: str
    type: str
    x: int
    y: int
    building_uid: str = None
    festival_uid: str = None
    hour: int = None
    minute: int = None
    region: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcMeta:
    dialog_objects: list[NpcMeta_DialogObjects]
    intro_dialog_objects: list[NpcMeta_IntroDialogObjects]
    npc_direction: str
    npc_enabled: bool
    npc_is_befriendable: bool
    npc_is_datable: bool
    npc_map_uid: str
    npc_type: str
    npc_x: int
    npc_y: int
    npc_accessories: list[str] = dataclasses.field(default_factory=list)
    npc_appearance_ears: str = None
    npc_appearance_face: str = None
    npc_appearance_tail: str = None
    npc_appearance_torso: str = None
    npc_birthday_day: int = None
    npc_birthday_season: str = None
    npc_buddy_system_active_trait: str = None
    npc_buddy_system_enabled: bool = None
    npc_buddy_system_passive_trait: str = None
    npc_can_be_festival_opponent: bool = None
    npc_cat_voice: int = None
    npc_cat_voice_pitch_modifier: float | int = None
    npc_colors_belly: list[int] = dataclasses.field(default_factory=list)
    npc_colors_ear_outer_left: list[int] = dataclasses.field(default_factory=list)
    npc_colors_ear_outer_right: list[int] = dataclasses.field(default_factory=list)
    npc_colors_ears_inner: list[int] = dataclasses.field(default_factory=list)
    npc_colors_eyes_left: list[int] = dataclasses.field(default_factory=list)
    npc_colors_eyes_right: list[int] = dataclasses.field(default_factory=list)
    npc_colors_face: list[int] = dataclasses.field(default_factory=list)
    npc_colors_face_stripes: list[int] = dataclasses.field(default_factory=list)
    npc_colors_feet: list[int] = dataclasses.field(default_factory=list)
    npc_colors_muzzle: list[int] = dataclasses.field(default_factory=list)
    npc_colors_nose: list[int] = dataclasses.field(default_factory=list)
    npc_colors_patches_one: list[int] = dataclasses.field(default_factory=list)
    npc_colors_patches_two: list[int] = dataclasses.field(default_factory=list)
    npc_colors_paw_back_one: list[int] = dataclasses.field(default_factory=list)
    npc_colors_paw_back_two: list[int] = dataclasses.field(default_factory=list)
    npc_colors_paw_front_one: list[int] = dataclasses.field(default_factory=list)
    npc_colors_paw_front_two: list[int] = dataclasses.field(default_factory=list)
    npc_colors_point: list[int] = dataclasses.field(default_factory=list)
    npc_colors_rosettes: list[int] = dataclasses.field(default_factory=list)
    npc_colors_speckles: list[int] = dataclasses.field(default_factory=list)
    npc_colors_stripes: list[int] = dataclasses.field(default_factory=list)
    npc_colors_stripes_two: list[int] = dataclasses.field(default_factory=list)
    npc_colors_tail: list[int] = dataclasses.field(default_factory=list)
    npc_colors_tail_tip: list[int] = dataclasses.field(default_factory=list)
    npc_colors_torso: list[int] = dataclasses.field(default_factory=list)
    npc_festival_games: list[NpcMeta_NpcFestivalGames] = dataclasses.field(
        default_factory=list
    )
    npc_festival_shop_uid: str = None
    npc_friendship_difficulty_modifier: float | int = None
    npc_has_colony_options: bool = None
    npc_has_healing: bool = None
    npc_has_influence_options: bool = None
    npc_has_museum_donate: bool = None
    npc_has_name_change: bool = None
    npc_has_shop: bool = None
    npc_is_kitten: bool = None
    npc_item_dislikes: list[str] = dataclasses.field(default_factory=list)
    npc_item_gifts: list[str] = dataclasses.field(default_factory=list)
    npc_item_hates: list[str] = dataclasses.field(default_factory=list)
    npc_item_likes: list[str] = dataclasses.field(default_factory=list)
    npc_item_loves: list[str] = dataclasses.field(default_factory=list)
    npc_loyalty: str = None
    npc_mole_appearance: str = None
    npc_schedule: list[NpcMeta_NpcSchedule] = dataclasses.field(default_factory=list)
    npc_shop_uid: str = None
    npc_show_friendship_rank: bool = None
    npc_spirit_appearance: str = None
    npc_spirit_voice: str = None
    npc_starting_dating_rank: int = None
    npc_starting_friendship_rank: int = None
    npc_starting_marriage_rank: int = None
    npc_wedding_guest_override_list: list[str] = dataclasses.field(default_factory=list)
