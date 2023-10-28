import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Time:
    """Dataset associated with files in 'gameresources/time'."""

    _special_mappings: ClassVar[dict] = {}
    time_tick: int = Undefined
