import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class FurnitureLangGerman:
    """Dataset associated with files in 'gameresources/furniture/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_furniture_description: str = Undefined
    lang_furniture_name: str = Undefined
