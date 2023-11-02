import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class TaskMeta:
    task_autumn: bool
    task_goal_quantity: int
    task_goal_type: str
    task_npc_uid: str
    task_reward_tokens: int
    task_spring: bool
    task_summer: bool
    task_winter: bool
    task_goal_item_uid: str = None
