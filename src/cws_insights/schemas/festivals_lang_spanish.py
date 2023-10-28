import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class FestivalsLangSpanish:
    """Dataset associated with files in 'gameresources/festivals/lang/spanish'."""

    festival_uid_do_not_translate: str = Undefined
    lang_festival_title: str = Undefined
