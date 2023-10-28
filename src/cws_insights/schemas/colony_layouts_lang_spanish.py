import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ColonyLayoutsLangSpanish:
    """Dataset associated with files in 'gameresources/colony_layouts/lang/spanish'."""

    lang_colony_layout_description: str = Undefined
    lang_colony_layout_name: str = Undefined
