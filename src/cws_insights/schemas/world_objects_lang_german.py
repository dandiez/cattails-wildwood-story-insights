import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WorldObjectLangGerman:
    """Dataset associated with files in 'gameresources/world_objects/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    lang_world_object_name: str = Undefined
