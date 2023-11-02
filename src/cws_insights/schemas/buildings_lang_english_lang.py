import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class BuildingLangEnglishLang:
    lang_building_name: str
