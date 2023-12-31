import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Task:
    """Dataset associated with files in 'gameresources/tasks'."""

    _special_mappings: ClassVar[dict] = {}
    task_autumn: bool = Undefined
    task_goal_item_uid: str = Undefined
    task_goal_quantity: int = Undefined
    task_goal_type: str = Undefined
    task_npc_uid: str = Undefined
    task_reward_tokens: int = Undefined
    task_spring: bool = Undefined
    task_summer: bool = Undefined
    task_winter: bool = Undefined
