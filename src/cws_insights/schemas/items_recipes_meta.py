import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant3_Output:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant3_Input:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant3:
    input: list[ItemRecipeMeta_RecipeVariant3_Input]
    output: ItemRecipeMeta_RecipeVariant3_Output


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant2_Output:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant2_Input:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant2:
    input: list[ItemRecipeMeta_RecipeVariant2_Input]
    output: ItemRecipeMeta_RecipeVariant2_Output


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant1_Output:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant1_Input:
    quantity: int
    uid: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta_RecipeVariant1:
    input: list[ItemRecipeMeta_RecipeVariant1_Input]
    output: ItemRecipeMeta_RecipeVariant1_Output


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemRecipeMeta:
    recipe_uid: str
    recipe_variant_1: ItemRecipeMeta_RecipeVariant1
    unlocked: bool
    recipe_variant_2: ItemRecipeMeta_RecipeVariant2 = None
    recipe_variant_3: ItemRecipeMeta_RecipeVariant3 = None
