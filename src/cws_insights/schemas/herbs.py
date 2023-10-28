import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Herb:
    """Dataset associated with files in 'gameresources/herbs'."""

    _special_mappings: ClassVar[dict] = {}
    autumn: list = Undefined
    bush_herbs: list = Undefined
    night_herbs: list = Undefined
    ranked_herbs: list = Undefined
    spring: list = Undefined
    summer: list = Undefined
    winter: list = Undefined
