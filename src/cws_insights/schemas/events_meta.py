import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksNever:
    block_type: str
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksHeard:
    block_type: str
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksForgot:
    block_type: str
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksSafe:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksTake:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksFriends:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksIgnore:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksListen:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksLie:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksTruth:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksNo_Choice2Consequences:
    friendship_change_zephyr: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksNo_Choice1Consequences:
    friendship_change_zephyr: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksNo:
    block_type: str
    cat_uid: str = None
    choice_1_consequences: EventMeta_EventBlocksNo_Choice1Consequences = None
    choice_1_key: str = None
    choice_1_path: str = None
    choice_2_consequences: EventMeta_EventBlocksNo_Choice2Consequences = None
    choice_2_key: str = None
    choice_2_path: str = None
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksYes:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksDeny:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksAffirm:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksDisagree:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksAgree:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksEatHoney:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksNoHoney:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksCharlotte:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    npc_uid: str = None
    seconds: float | int = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksSpark:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksPost:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksFight:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    seconds: float | int = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksTalk:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    seconds: float | int = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksWork:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    direction: str = None
    emote_type: str = None
    lang_key: str = None
    npc_uid: str = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocksGive:
    block_type: str
    cat_uid: str = None
    emote_type: str = None
    lang_key: str = None
    speaker_uid: str = None
    target: str = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocks_Choice4Consequences:
    friendship_change_bob: int
    friendship_change_buttercup: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocks_Choice3Consequences:
    friendship_change_buttercup: int = None
    friendship_change_jag: int = None
    friendship_change_zephyr: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocks_Choice2Consequences:
    friendship_change_alabaster: int = None
    friendship_change_bob: int = None
    friendship_change_buttercup: int = None
    friendship_change_champ: int = None
    friendship_change_charlotte: int = None
    friendship_change_elli: int = None
    friendship_change_ember: int = None
    friendship_change_glimmer: int = None
    friendship_change_jag: int = None
    friendship_change_krampy: int = None
    friendship_change_phantom: int = None
    friendship_change_rosemary: int = None
    friendship_change_spark: int = None
    friendship_change_talon: int = None
    friendship_change_zephyr: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocks_Choice1Consequences:
    friendship_change_alabaster: int = None
    friendship_change_bob: int = None
    friendship_change_champ: int = None
    friendship_change_charlotte: int = None
    friendship_change_coco: int = None
    friendship_change_elli: int = None
    friendship_change_ember: int = None
    friendship_change_fliss: int = None
    friendship_change_glimmer: int = None
    friendship_change_jag: int = None
    friendship_change_krampy: int = None
    friendship_change_lainey: int = None
    friendship_change_phantom: int = None
    friendship_change_rosemary: int = None
    friendship_change_spark: int = None
    friendship_change_talon: int = None
    friendship_change_zephyr: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventBlocks:
    block_type: str
    behavior: str = None
    cat_uid: str = None
    choice_1_consequences: EventMeta_EventBlocks_Choice1Consequences = None
    choice_1_key: str = None
    choice_1_path: str = None
    choice_2_consequences: EventMeta_EventBlocks_Choice2Consequences = None
    choice_2_key: str = None
    choice_2_path: str = None
    choice_3_consequences: EventMeta_EventBlocks_Choice3Consequences = None
    choice_3_key: str = None
    choice_3_path: str = None
    choice_4_consequences: EventMeta_EventBlocks_Choice4Consequences = None
    choice_4_key: str = None
    choice_4_path: str = None
    direction: str = None
    emote_type: str = None
    item_uid: str = None
    lang_key: str = None
    npc_uid: str = None
    seconds: float | int = None
    speaker_uid: str = None
    speed_mod: float | int = None
    target: str = None
    x: int = None
    y: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta_EventFilters:
    filter_autumn: bool = None
    filter_blizzard: bool = None
    filter_friendship_alabaster: int = None
    filter_friendship_bob: int = None
    filter_friendship_buttercup: int = None
    filter_friendship_champ: int = None
    filter_friendship_charlotte: int = None
    filter_friendship_coco: int = None
    filter_friendship_elli: int = None
    filter_friendship_fliss: int = None
    filter_friendship_garlic: int = None
    filter_friendship_jag: int = None
    filter_friendship_krampy: int = None
    filter_friendship_lainey: int = None
    filter_friendship_rosemary: int = None
    filter_friendship_spark: int = None
    filter_friendship_talon: int = None
    filter_friendship_zephyr: int = None
    filter_has_met_alabaster: bool = None
    filter_has_met_bob: bool = None
    filter_has_met_buttercup: bool = None
    filter_has_met_champ: bool = None
    filter_has_met_charlotte: bool = None
    filter_has_met_coco: bool = None
    filter_has_met_elli: bool = None
    filter_has_met_ember: bool = None
    filter_has_met_fliss: bool = None
    filter_has_met_garlic: bool = None
    filter_has_met_glimmer: bool = None
    filter_has_met_jag: bool = None
    filter_has_met_krampy: bool = None
    filter_has_met_lainey: bool = None
    filter_has_met_phantom: bool = None
    filter_has_met_rosemary: bool = None
    filter_has_met_spark: bool = None
    filter_has_met_talon: bool = None
    filter_has_met_zephyr: bool = None
    filter_hour: int = None
    filter_hour_max: int = None
    filter_player_is_dating_alabaster: bool = None
    filter_player_is_dating_bob: bool = None
    filter_player_is_dating_buttercup: bool = None
    filter_player_is_dating_champ: bool = None
    filter_player_is_dating_elli: bool = None
    filter_player_is_dating_fliss: bool = None
    filter_player_is_dating_krampy: bool = None
    filter_player_is_dating_lainey: bool = None
    filter_player_is_dating_spark: bool = None
    filter_player_is_dating_talon: bool = None
    filter_player_is_dating_zephyr: bool = None
    filter_player_is_married_to_alabaster: bool = None
    filter_player_is_married_to_bob: bool = None
    filter_player_is_married_to_buttercup: bool = None
    filter_player_is_married_to_champ: bool = None
    filter_player_is_married_to_elli: bool = None
    filter_player_is_married_to_fliss: bool = None
    filter_player_is_married_to_krampy: bool = None
    filter_player_is_married_to_lainey: bool = None
    filter_player_is_married_to_spark: bool = None
    filter_player_is_married_to_talon: bool = None
    filter_player_is_married_to_zephyr: bool = None
    filter_rival_marriage_completed_alabasterandfliss: bool = None
    filter_rival_marriage_completed_bobandbuttercup: bool = None
    filter_rival_marriage_completed_elliandchamp: bool = None
    filter_rival_marriage_completed_krampyandtalon: bool = None
    filter_rival_marriage_completed_sparkandlainey: bool = None
    filter_snow: bool = None
    filter_spring: bool = None
    filter_storm: bool = None
    filter_summer: bool = None
    filter_sun: bool = None
    filter_time: str = None
    filter_winter: bool = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class EventMeta:
    event_blocks: list[EventMeta_EventBlocks]
    event_chance: int
    event_filters: EventMeta_EventFilters
    event_high_priority: bool
    event_map_uid: str
    event_music: str
    event_unique: bool
    event_blocks_affirm: list[EventMeta_EventBlocksAffirm] = dataclasses.field(
        default_factory=list
    )
    event_blocks_agree: list[EventMeta_EventBlocksAgree] = dataclasses.field(
        default_factory=list
    )
    event_blocks_charlotte: list[EventMeta_EventBlocksCharlotte] = dataclasses.field(
        default_factory=list
    )
    event_blocks_deny: list[EventMeta_EventBlocksDeny] = dataclasses.field(
        default_factory=list
    )
    event_blocks_disagree: list[EventMeta_EventBlocksDisagree] = dataclasses.field(
        default_factory=list
    )
    event_blocks_eat_honey: list[EventMeta_EventBlocksEatHoney] = dataclasses.field(
        default_factory=list
    )
    event_blocks_fight: list[EventMeta_EventBlocksFight] = dataclasses.field(
        default_factory=list
    )
    event_blocks_forgot: list[EventMeta_EventBlocksForgot] = dataclasses.field(
        default_factory=list
    )
    event_blocks_friends: list[EventMeta_EventBlocksFriends] = dataclasses.field(
        default_factory=list
    )
    event_blocks_give: list[EventMeta_EventBlocksGive] = dataclasses.field(
        default_factory=list
    )
    event_blocks_heard: list[EventMeta_EventBlocksHeard] = dataclasses.field(
        default_factory=list
    )
    event_blocks_ignore: list[EventMeta_EventBlocksIgnore] = dataclasses.field(
        default_factory=list
    )
    event_blocks_lie: list[EventMeta_EventBlocksLie] = dataclasses.field(
        default_factory=list
    )
    event_blocks_listen: list[EventMeta_EventBlocksListen] = dataclasses.field(
        default_factory=list
    )
    event_blocks_never: list[EventMeta_EventBlocksNever] = dataclasses.field(
        default_factory=list
    )
    event_blocks_no: list[EventMeta_EventBlocksNo] = dataclasses.field(
        default_factory=list
    )
    event_blocks_no_honey: list[EventMeta_EventBlocksNoHoney] = dataclasses.field(
        default_factory=list
    )
    event_blocks_post: list[EventMeta_EventBlocksPost] = dataclasses.field(
        default_factory=list
    )
    event_blocks_safe: list[EventMeta_EventBlocksSafe] = dataclasses.field(
        default_factory=list
    )
    event_blocks_spark: list[EventMeta_EventBlocksSpark] = dataclasses.field(
        default_factory=list
    )
    event_blocks_take: list[EventMeta_EventBlocksTake] = dataclasses.field(
        default_factory=list
    )
    event_blocks_talk: list[EventMeta_EventBlocksTalk] = dataclasses.field(
        default_factory=list
    )
    event_blocks_truth: list[EventMeta_EventBlocksTruth] = dataclasses.field(
        default_factory=list
    )
    event_blocks_work: list[EventMeta_EventBlocksWork] = dataclasses.field(
        default_factory=list
    )
    event_blocks_yes: list[EventMeta_EventBlocksYes] = dataclasses.field(
        default_factory=list
    )
