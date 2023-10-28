import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Bundle:
    """Dataset associated with files in 'gameresources/bundles'."""

    _special_mappings: ClassVar[dict] = {}
    bundle_colony_points: int = Undefined
    bundle_feature_label: str = Undefined
    bundle_item1_quantity: int = Undefined
    bundle_item1_uid: str = Undefined
    bundle_item2_quantity: int = Undefined
    bundle_item2_uid: str = Undefined
    bundle_item3_quantity: int = Undefined
    bundle_item3_uid: str = Undefined
    bundle_item4_quantity: int = Undefined
    bundle_item4_uid: str = Undefined
    bundle_item5_quantity: int = Undefined
    bundle_item5_uid: str = Undefined
    bundle_post_story: bool = Undefined
    bundle_priority: int = Undefined
    bundle_unlock_npc_uids: list = Undefined
