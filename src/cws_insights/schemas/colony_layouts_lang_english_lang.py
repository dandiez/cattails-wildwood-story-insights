import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ColonyLayoutLangEnglishLang:
    lang_colony_layout_description: str
    lang_colony_layout_name: str