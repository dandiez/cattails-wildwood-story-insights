import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class BundleMeta:
    bundle_colony_points: int
    bundle_feature_label: str
    bundle_item1_quantity: int
    bundle_item1_uid: str
    bundle_item2_quantity: int
    bundle_item2_uid: str
    bundle_item3_quantity: int
    bundle_item3_uid: str
    bundle_item4_quantity: int
    bundle_item4_uid: str
    bundle_item5_quantity: int
    bundle_item5_uid: str
    bundle_priority: int
    bundle_unlock_npc_uids: list[str]
    bundle_post_story: bool = None
