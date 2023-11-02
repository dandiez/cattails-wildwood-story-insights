import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcShopMeta_ShopItems_ItemFilters:
    filter_autumn: bool = None
    filter_day: int = None
    filter_friendship_alabaster: int = None
    filter_spring: bool = None
    filter_summer: bool = None
    filter_winter: bool = None
    filter_year: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcShopMeta_ShopItems:
    item_base_price: int
    item_filters: NpcShopMeta_ShopItems_ItemFilters
    item_name: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class NpcShopMeta:
    allow_selling: bool
    buy_dialog: str
    currency_type: str
    not_enough_currency_dialog: str
    not_enough_inventory_dialog: str
    shop_items: list[NpcShopMeta_ShopItems]
    shop_title: str
    thanks_dialog: str
    cannot_sell_dialog: str = None
    sell_dialog: str = None
    sell_everything_dialog: str = None
    sell_everything_invalid_dialog: str = None
    sell_everything_nothing_dialog: str = None
