import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class CraftingStationMeta:
    recipes_list: list[str]
