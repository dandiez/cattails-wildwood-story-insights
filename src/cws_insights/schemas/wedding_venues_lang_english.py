import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WeddingVenuesLangEnglish:
    """Dataset associated with files in 'gameresources/wedding_venues/lang/english'."""

    lang_wedding_venues_description: str = Undefined
    lang_wedding_venues_name: str = Undefined
