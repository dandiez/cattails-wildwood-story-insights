import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WorldObjectsLangEnglish:
    """Dataset associated with files in 'gameresources/world_objects/lang/english'."""

    lang_world_object_name: str = Undefined
