import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Festival:
    """Dataset associated with files in 'gameresources/festivals'."""

    _special_mappings: ClassVar[dict] = {}
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
