import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemAccessory:
    """Dataset associated with files in 'gameresources/items/accessories'."""

    _special_mappings: ClassVar[dict] = {}
    accessory_type: str = Undefined
    accessory_uid: str = Undefined
    sorting_priority: int = Undefined
    unlocked: bool = Undefined
