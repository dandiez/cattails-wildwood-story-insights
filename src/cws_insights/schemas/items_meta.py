import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemMeta:
    bundle_uids: list[str] = dataclasses.field(default_factory=list)
    gross_item_uids: list[str] = dataclasses.field(default_factory=list)
    item_attack_amount: int = None
    item_buddy_xp_amount: int = None
    item_can_explode: bool = None
    item_can_sell: bool = None
    item_catnip_amount: int = None
    item_confusion_amount: int = None
    item_cures_poison: bool = None
    item_heal_amount: float | int = None
    item_herbs_resource_value: int = None
    item_hunger_amount: int = None
    item_immunity_amount: int = None
    item_influence_amount: int = None
    item_is_farsighted: bool = None
    item_mews_value: int = None
    item_mole_cash_value: int = None
    item_prey_resource_value: int = None
    item_random_effect: bool = None
    item_rarity: str = None
    item_sand_resource_value: int = None
    item_sorting_priority: int = None
    item_special_effect: bool = None
    item_speed_amount: int = None
    item_stealth_amount: int = None
    item_stone_resource_value: int = None
    item_swim_amount: int = None
    item_treasure_resource_value: int = None
    item_uid: str = None
    item_venom_amount: int = None
    item_wood_resource_value: int = None
