import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class TaskLangGermanLang:
    lang_task_complete_dialog: str
    lang_task_description: str
    lang_task_in_progress_dialog: str
    lang_task_title: str
