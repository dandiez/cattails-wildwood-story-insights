import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WeddingVenueLangGerman:
    """Dataset associated with files in 'gameresources/wedding_venues/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_wedding_venues_description: str = Undefined
    lang_wedding_venues_name: str = Undefined
