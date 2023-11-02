import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemAccessoryMeta:
    accessory_type: str
    accessory_uid: str
    sorting_priority: int
    unlocked: bool
