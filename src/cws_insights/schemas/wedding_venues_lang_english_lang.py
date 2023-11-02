import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class WeddingVenueLangEnglishLang:
    lang_wedding_venues_description: str
    lang_wedding_venues_name: str
