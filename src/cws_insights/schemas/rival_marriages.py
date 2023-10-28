import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class RivalMarriages:
    """Dataset associated with files in 'gameresources/rival_marriages'."""

    kitten_birthday_day: int = Undefined
    kitten_birthday_season: str = Undefined
    kitten_uids: list = Undefined
    partner_primary_uid: str = Undefined
    partner_secondary_uid: str = Undefined
    prerequisite_events: list = Undefined
    wedding_attendees: list = Undefined
