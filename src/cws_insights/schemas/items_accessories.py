import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemsAccessories:
    """Dataset associated with files in 'gameresources/items/accessories'."""

    accessory_type: str = Undefined
    accessory_uid: str = Undefined
    sorting_priority: int = Undefined
    unlocked: bool = Undefined
