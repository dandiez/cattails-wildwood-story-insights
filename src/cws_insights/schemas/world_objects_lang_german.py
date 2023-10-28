import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class WorldObjectsLangGerman:
    """Dataset associated with files in 'gameresources/world_objects/lang/german'."""

    lang_world_object_name: str = Undefined
