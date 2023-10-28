import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Time:
    """Dataset associated with files in 'gameresources/time'."""

    time_tick: int = Undefined
