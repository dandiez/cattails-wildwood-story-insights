import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MapLangGermanLang:
    lang_region_name: str
