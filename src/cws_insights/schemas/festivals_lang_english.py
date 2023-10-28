import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class FestivalsLangEnglish:
    """Dataset associated with files in 'gameresources/festivals/lang/english'."""

    festival_uid_do_not_translate: str = Undefined
    lang_festival_title: str = Undefined
