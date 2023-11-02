import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class FurnitureLangEnglishLang:
    lang_furniture_description: str
    lang_furniture_name: str
