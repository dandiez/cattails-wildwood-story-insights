import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class RivalMarriageMeta:
    kitten_birthday_day: int
    kitten_birthday_season: str
    kitten_uids: list[str]
    partner_primary_uid: str
    partner_secondary_uid: str
    prerequisite_events: list[str]
    wedding_attendees: list[str]
