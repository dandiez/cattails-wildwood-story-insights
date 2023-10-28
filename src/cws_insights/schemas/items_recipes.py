import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemsRecipes:
    """Dataset associated with files in 'gameresources/items/recipes'."""

    recipe_uid: str = Undefined
    recipe_variant_1: dict = Undefined
    recipe_variant_2: dict = Undefined
    recipe_variant_3: dict = Undefined
    unlocked: bool = Undefined
