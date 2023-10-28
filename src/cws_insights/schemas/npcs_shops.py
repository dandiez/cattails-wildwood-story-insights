import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class NpcShop:
    """Dataset associated with files in 'gameresources/npcs/shops'."""

    _special_mappings: ClassVar[dict] = {}
    allow_selling: bool = Undefined
    buy_dialog: str = Undefined
    cannot_sell_dialog: str = Undefined
    currency_type: str = Undefined
    not_enough_currency_dialog: str = Undefined
    not_enough_inventory_dialog: str = Undefined
    sell_dialog: str = Undefined
    sell_everything_dialog: str = Undefined
    sell_everything_invalid_dialog: str = Undefined
    sell_everything_nothing_dialog: str = Undefined
    shop_items: list = Undefined
    shop_title: str = Undefined
    thanks_dialog: str = Undefined
