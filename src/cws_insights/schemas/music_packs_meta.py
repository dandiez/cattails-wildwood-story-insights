import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MusicPackMeta:
    pack_type: str
    music_autumn: str = None
    music_autumn_1_3: str = None
    music_autumn_4_7: str = None
    music_autumn_8_10: str = None
    music_day: str = None
    music_level_1_25: str = None
    music_level_26_50: str = None
    music_level_51_75: str = None
    music_level_76_100: str = None
    music_night: str = None
    music_spring: str = None
    music_spring_1_3: str = None
    music_spring_4_7: str = None
    music_spring_8_10: str = None
    music_summer: str = None
    music_summer_1_3: str = None
    music_summer_4_7: str = None
    music_summer_8_10: str = None
    music_track: str = None
    music_winter: str = None
    music_winter_1_3: str = None
    music_winter_4_7: str = None
    music_winter_8_10: str = None
