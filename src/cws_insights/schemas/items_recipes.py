import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemRecipe:
    """Dataset associated with files in 'gameresources/items/recipes'."""

    _special_mappings: ClassVar[dict] = {}
    recipe_uid: str = Undefined
    recipe_variant_1: dict = Undefined
    recipe_variant_2: dict = Undefined
    recipe_variant_3: dict = Undefined
    unlocked: bool = Undefined
