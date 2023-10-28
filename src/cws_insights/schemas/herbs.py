import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Herbs:
    """Dataset associated with files in 'gameresources/herbs'."""

    autumn: list = Undefined
    bush_herbs: list = Undefined
    night_herbs: list = Undefined
    ranked_herbs: list = Undefined
    spring: list = Undefined
    summer: list = Undefined
    winter: list = Undefined
