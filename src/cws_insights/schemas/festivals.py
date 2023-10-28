import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Festivals:
    """Dataset associated with files in 'gameresources/festivals'."""

    festival_calendar_icon: str = Undefined
    festival_day: int = Undefined
    festival_force_hour: int = Undefined
    festival_hour_end: int = Undefined
    festival_hour_start: int = Undefined
    festival_map_uid: str = Undefined
    festival_music: str = Undefined
    festival_season: str = Undefined
    festival_uid: str = Undefined
    festival_warning_early_dialog_path: str = Undefined
    festival_warning_late_dialog_path: str = Undefined
    festival_warning_npc: str = Undefined
    festival_weather: str = Undefined
    festival_world_objects: list = Undefined
