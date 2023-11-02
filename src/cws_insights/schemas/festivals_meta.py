import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class FestivalMeta_FestivalWorldObjects:
    type: str
    x: int
    y: int


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class FestivalMeta:
    festival_calendar_icon: str
    festival_day: int
    festival_hour_end: int
    festival_hour_start: int
    festival_map_uid: str
    festival_music: str
    festival_season: str
    festival_uid: str
    festival_warning_early_dialog_path: str
    festival_warning_late_dialog_path: str
    festival_warning_npc: str
    festival_weather: str
    festival_world_objects: list[FestivalMeta_FestivalWorldObjects]
    festival_force_hour: int = None
