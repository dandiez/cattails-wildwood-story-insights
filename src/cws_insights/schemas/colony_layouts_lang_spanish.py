import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ColonyLayoutLangSpanish:
    """Dataset associated with files in 'gameresources/colony_layouts/lang/spanish'."""

    _special_mappings: ClassVar[dict] = {}
    lang_colony_layout_description: str = Undefined
    lang_colony_layout_name: str = Undefined
