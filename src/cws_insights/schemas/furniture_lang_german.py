import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class FurnitureLangGerman:
    """Dataset associated with files in 'gameresources/furniture/lang/german'."""

    lang_furniture_description: str = Undefined
    lang_furniture_name: str = Undefined