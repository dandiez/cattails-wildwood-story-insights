import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Events:
    """Dataset associated with files in 'gameresources/events'."""

    event_blocks: list = Undefined
    event_blocks_affirm: list = Undefined
    event_blocks_agree: list = Undefined
    event_blocks_charlotte: list = Undefined
    event_blocks_deny: list = Undefined
    event_blocks_disagree: list = Undefined
    event_blocks_eat_honey: list = Undefined
    event_blocks_fight: list = Undefined
    event_blocks_forgot: list = Undefined
    event_blocks_friends: list = Undefined
    event_blocks_give: list = Undefined
    event_blocks_heard: list = Undefined
    event_blocks_ignore: list = Undefined
    event_blocks_lie: list = Undefined
    event_blocks_listen: list = Undefined
    event_blocks_never: list = Undefined
    event_blocks_no: list = Undefined
    event_blocks_no_honey: list = Undefined
    event_blocks_post: list = Undefined
    event_blocks_safe: list = Undefined
    event_blocks_spark: list = Undefined
    event_blocks_take: list = Undefined
    event_blocks_talk: list = Undefined
    event_blocks_truth: list = Undefined
    event_blocks_work: list = Undefined
    event_blocks_yes: list = Undefined
    event_chance: int = Undefined
    event_filters: dict = Undefined
    event_high_priority: bool = Undefined
    event_map_uid: str = Undefined
    event_music: str = Undefined
    event_unique: bool = Undefined
