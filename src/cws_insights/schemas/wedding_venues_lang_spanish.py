import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WeddingVenueLangSpanish:
    """Dataset associated with files in 'gameresources/wedding_venues/lang/spanish'."""

    _special_mappings: ClassVar[dict] = {}
    lang_wedding_venues_description: str = Undefined
    lang_wedding_venues_name: str = Undefined
