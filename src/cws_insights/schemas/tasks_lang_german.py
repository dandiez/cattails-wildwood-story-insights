import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class TaskLangGerman:
    """Dataset associated with files in 'gameresources/tasks/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_task_complete_dialog: str = Undefined
    lang_task_description: str = Undefined
    lang_task_in_progress_dialog: str = Undefined
    lang_task_title: str = Undefined
