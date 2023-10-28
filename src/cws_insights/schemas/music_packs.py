import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MusicPack:
    """Dataset associated with files in 'gameresources/music/packs'."""

    _special_mappings: ClassVar[dict] = {}
    music_autumn: str = Undefined
    music_autumn_1_3: str = Undefined
    music_autumn_4_7: str = Undefined
    music_autumn_8_10: str = Undefined
    music_day: str = Undefined
    music_level_1_25: str = Undefined
    music_level_26_50: str = Undefined
    music_level_51_75: str = Undefined
    music_level_76_100: str = Undefined
    music_night: str = Undefined
    music_spring: str = Undefined
    music_spring_1_3: str = Undefined
    music_spring_4_7: str = Undefined
    music_spring_8_10: str = Undefined
    music_summer: str = Undefined
    music_summer_1_3: str = Undefined
    music_summer_4_7: str = Undefined
    music_summer_8_10: str = Undefined
    music_track: str = Undefined
    music_winter: str = Undefined
    music_winter_1_3: str = Undefined
    music_winter_4_7: str = Undefined
    music_winter_8_10: str = Undefined
    pack_type: str = Undefined
