import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class TasksLangEnglish:
    """Dataset associated with files in 'gameresources/tasks/lang/english'."""

    lang_task_complete_dialog: str = Undefined
    lang_task_description: str = Undefined
    lang_task_in_progress_dialog: str = Undefined
    lang_task_title: str = Undefined
