import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Items:
    """Dataset associated with files in 'gameresources/items'."""

    bundle_uids: list = Undefined
    gross_item_uids: list = Undefined
    item_attack_amount: int = Undefined
    item_buddy_xp_amount: int = Undefined
    item_can_explode: bool = Undefined
    item_can_sell: bool = Undefined
    item_catnip_amount: int = Undefined
    item_confusion_amount: int = Undefined
    item_cures_poison: bool = Undefined
    item_heal_amount: float | int = Undefined
    item_herbs_resource_value: int = Undefined
    item_hunger_amount: int = Undefined
    item_immunity_amount: int = Undefined
    item_influence_amount: int = Undefined
    item_is_farsighted: bool = Undefined
    item_mews_value: int = Undefined
    item_mole_cash_value: int = Undefined
    item_prey_resource_value: int = Undefined
    item_random_effect: bool = Undefined
    item_rarity: str = Undefined
    item_sand_resource_value: int = Undefined
    item_sorting_priority: int = Undefined
    item_special_effect: bool = Undefined
    item_speed_amount: int = Undefined
    item_stealth_amount: int = Undefined
    item_stone_resource_value: int = Undefined
    item_swim_amount: int = Undefined
    item_treasure_resource_value: int = Undefined
    item_uid: str = Undefined
    item_venom_amount: int = Undefined
    item_wood_resource_value: int = Undefined
