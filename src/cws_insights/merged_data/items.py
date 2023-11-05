import dataclasses
import os
from collections import defaultdict
from typing import TypeAlias, Callable

from cws_insights.definitions import Undefined, POWER_POWS

from cws_insights.schemas._index import AllResourceData
from cws_insights.schemas.herbs_meta import HerbMeta as Herb
from cws_insights.schemas.items_meta import ItemMeta as Item
from cws_insights.schemas.items_lang_english_lang import (
    ItemLangEnglishLang as ItemLangEnglish,
)
from cws_insights.schemas.items_recipes_meta import (
    ItemRecipeMeta as ItemRecipe,
    ItemRecipeMeta_RecipeVariant3,
    ItemRecipeMeta_RecipeVariant2,
    ItemRecipeMeta_RecipeVariant1,
)
from cws_insights.schemas.map_region import MapRegion as Map
from cws_insights.schemas.npcs_meta import NpcMeta as Npc
from cws_insights.schemas.npcs_shops_meta import (
    NpcShopMeta as NpcShop,
    NpcShopMeta_ShopItems,
)

Uid: TypeAlias = str
UidStem: TypeAlias = str


@dataclasses.dataclass
class ItemFromNpcShop:
    shop_selling_it: NpcShop = None
    sale_details: NpcShopMeta_ShopItems = None


@dataclasses.dataclass
class ItemFromNpc:
    # TODO use NPC merge object instead of id which has language info
    npc_loves: list[Uid] = dataclasses.field(default_factory=list)
    npc_likes: list[Uid] = dataclasses.field(default_factory=list)
    npc_dislikes: list[Uid] = dataclasses.field(default_factory=list)
    npc_hates: list[Uid] = dataclasses.field(default_factory=list)
    npc_gifts: list[Uid] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ItemfromMapRegion:
    herb_list: list[Uid] = dataclasses.field(default_factory=list)
    prey_list: list[Uid] = dataclasses.field(default_factory=list)
    spawners: list[Uid] = dataclasses.field(default_factory=list)
    world_objects: list[Uid] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ItemFromHerbs:
    ranked_herbs: bool = False
    bush_herbs: bool = False
    night_herbs: bool = False
    autumn: bool = False
    spring: bool = False
    summer: bool = False
    winter: bool = False


RecipeVariant = (
    ItemRecipeMeta_RecipeVariant1
    | ItemRecipeMeta_RecipeVariant2
    | ItemRecipeMeta_RecipeVariant3
)


@dataclasses.dataclass
class ItemFromItemRecipe:
    as_input: list[RecipeVariant] = dataclasses.field(default_factory=list)
    as_output: list[RecipeVariant] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ItemPlus:
    game_version = None
    item_lang: ItemLangEnglish = None
    item: Item = None
    from_shops: list[ItemFromNpcShop] = dataclasses.field(default_factory=list)
    # herb_uid: Uid = None
    # sprite: str = None
    from_npc: ItemFromNpc = dataclasses.field(default_factory=ItemFromNpc)
    from_herbs: ItemFromHerbs = dataclasses.field(default_factory=ItemFromHerbs)
    from_recipes: ItemFromItemRecipe = dataclasses.field(
        default_factory=ItemFromItemRecipe
    )
    from_map: ItemfromMapRegion = dataclasses.field(default_factory=ItemfromMapRegion)


AllItemPlus: TypeAlias = dict[Uid, ItemPlus]


class ItemPlusGroup:
    """Some herbs are sometimes not referred by their uid (includes quality), but by a "group id" without quality."""

    def __init__(self, contained: list[ItemPlus]):
        self._contained: list[ItemPlus] = contained

    def __setattr__(self, key, value):
        if key == "_contained":
            super().__setattr__(key, value)
            return
        for i in self._contained:
            i.__setattr__(key, value)


AllItemPlusWithGroups: TypeAlias = dict[Uid, ItemPlus | ItemPlusGroup]


def get_merged_item_data(all_resource_data: AllResourceData) -> AllItemPlus:
    _double_check_assumptions(all_resource_data)
    all_items_indexed_by_uid = {
        item.item_uid: item
        for item in all_resource_data.items_meta.values()
        if item.item_uid is not None
    }
    all_item_plus = {
        item.item_uid: ItemPlus(item=item)
        for item in all_items_indexed_by_uid.values()
        if item.item_uid is not None
    }
    grouped_items_by_group_id = _get_grouped_items(all_item_plus)
    _merge_item_lang(all_resource_data.items_lang_english_lang, all_item_plus)
    _merge_sprite(all_item_plus)
    _merge_npc(all_resource_data.npcs_meta, all_item_plus)
    all_item_plus_with_groups = grouped_items_by_group_id | all_item_plus
    _merge_map_regions(all_resource_data.map_region, all_item_plus_with_groups)
    _merge_herbs(all_resource_data.herbs_meta, all_item_plus_with_groups)
    _merge_shop(all_resource_data.npcs_shops_meta, all_item_plus)
    _merge_recipe(all_resource_data.items_recipes_meta, all_item_plus)
    return all_item_plus


def _double_check_assumptions(all_resource_data: AllResourceData):
    for stem, item in all_resource_data.items_meta.items():
        if item.item_uid is None:
            continue
        assert (
            stem == get_stem_from_uid(item.item_uid) + "item"
        ), f"{stem} is not equal {get_stem_from_uid(item.item_uid)}"


def _get_grouped_items(all_item_plus):
    groups = defaultdict(list)
    for item_uid, item_plus in all_item_plus.items():
        for quality in ["[Poor]", "[Fair]", "[Good]"]:
            if quality in item_uid:
                group_id = item_uid.split(quality)[0].strip()
                groups[group_id].append(item_plus)
    grouped_items_by_group_id = {
        group_id: ItemPlusGroup(group_list) for group_id, group_list in groups.items()
    }
    return grouped_items_by_group_id


def _merge_item_lang(
    items_lang: dict[UidStem, ItemLangEnglish], item_plus: AllItemPlus
):
    all_items_lang_indexed_by_uid = {
        item_lang.item_uid_do_not_translate: item_lang
        for item_lang in items_lang.values()
    }
    for uid, item_lang in all_items_lang_indexed_by_uid.items():
        try:
            item_plus[uid].item_lang = item_lang
        except KeyError:
            print(
                f"skipping over lang with uid {uid}, which does not have a matching item."
            )


def _merge_sprite(all_item_plus: AllItemPlus):
    for i in all_item_plus.values():
        i.sprite = get_stem_from_uid(i.item.item_uid) + "_wildwood_story.png"


def _merge_npc(npcs: dict[Uid, Npc], all_item_plus: AllItemPlus):
    for npc_uid, npc in npcs.items():
        if npc.npc_item_loves is not Undefined:
            for item_uid in npc.npc_item_loves:
                all_item_plus[item_uid].from_npc.npc_loves.append(npc_uid)
        if npc.npc_item_likes is not Undefined:
            for item_uid in npc.npc_item_likes:
                all_item_plus[item_uid].from_npc.npc_likes.append(npc_uid)
        if npc.npc_item_dislikes is not Undefined:
            for item_uid in npc.npc_item_dislikes:
                all_item_plus[item_uid].from_npc.npc_dislikes.append(npc_uid)
        if npc.npc_item_hates is not Undefined:
            for item_uid in npc.npc_item_hates:
                all_item_plus[item_uid].from_npc.npc_hates.append(npc_uid)

        if npc.npc_item_gifts is not Undefined:
            for item_uid in npc.npc_item_gifts:
                all_item_plus[item_uid].from_npc.npc_gifts.append(npc_uid)


def _merge_map_regions(
    map: dict[Uid, Map], all_item_plus_with_groups: AllItemPlusWithGroups
):
    for region_id, region in map.items():
        for herb in region.region_data.herbs_list:
            f = lambda x: x.from_map.herb_list.append(region_id)
            apply_function_to_item_plus_with_groups(all_item_plus_with_groups[herb], f)
        for prey in region.region_data.prey_list:
            all_item_plus_with_groups[prey].from_map.prey_list.append(region_id)
        for spawner in region.region_data.spawners:
            for item_id in spawner.item_uids:
                all_item_plus_with_groups[item_id].from_map.spawners.append(region_id)
        for world_object in region.region_data.world_objects:
            if world_object.power_paw_index is not None:
                paw_item = POWER_POWS[f"Power Paw {world_object.power_paw_index}"]
                all_item_plus_with_groups[paw_item].from_map.world_objects.append(
                    region_id
                )


def _merge_herbs(
    herbs_meta: dict[Uid, Herb], all_item_plus_with_groups: AllItemPlusWithGroups
):
    for herb_ui, herb in herbs_meta.items():
        for night_herb_uid in herb.night_herbs:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[night_herb_uid]
            ):
                item.from_herbs.night_herbs = True
        for bush_herb_uid in herb.bush_herbs:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[bush_herb_uid]
            ):
                item.from_herbs.bush_herbs = True
        for ranked_herb_uid in herb.ranked_herbs:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[ranked_herb_uid]
            ):
                item.from_herbs.ranked_herbs = True
        for autum_herb_uid in herb.autumn:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[autum_herb_uid]
            ):
                item.from_herbs.autumn = True
        for spring_herb_uid in herb.spring:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[spring_herb_uid]
            ):
                item.from_herbs.spring = True
        for summer_herb_uid in herb.summer:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[summer_herb_uid]
            ):
                item.from_herbs.summer = True
        for winter_herb_uid in herb.winter:
            for item in yield_items_in_itemplus_or_group(
                all_item_plus_with_groups[winter_herb_uid]
            ):
                item.from_herbs.winter = True


def _merge_shop(npcs_shops_meta: dict[Uid, NpcShop], all_item_plus: AllItemPlus):
    for npc_shop_id, npc_shop in npcs_shops_meta.items():
        for shop_item in npc_shop.shop_items:
            lookup_name = POWER_POWS.get(shop_item.item_name, shop_item.item_name)
            split = lookup_name.split(" ", maxsplit=1)
            if split[-1] in ("XP", "Mews", "Mole Cash"):
                continue
            all_item_plus[lookup_name].from_shops.append(
                ItemFromNpcShop(shop_selling_it=npc_shop, sale_details=shop_item)
            )


def _merge_recipe(
    items_recipes_meta: dict[UidStem, ItemRecipe], all_item_plus: AllItemPlus
):
    for recipe_uid, recipe in items_recipes_meta.items():
        for variant in [
            recipe.recipe_variant_1,
            recipe.recipe_variant_2,
            recipe.recipe_variant_3,
        ]:
            if variant is None:
                continue
            for inp in variant.input:
                all_item_plus[inp.uid].from_recipes.as_input.append(variant)
            all_item_plus[variant.output.uid].from_recipes.as_output.append(variant)


def get_stem_from_uid(uid: Uid) -> UidStem:
    return uid.lower().replace(" ", "").replace("[", "").replace("]", "")


def apply_function_to_item_plus_with_groups(
    item_or_group: ItemPlus | ItemPlusGroup, function_to_apply: Callable
):
    if isinstance(item_or_group, ItemPlus):
        function_to_apply(item_or_group)
    if isinstance(item_or_group, ItemPlusGroup):
        for item in item_or_group._contained:
            function_to_apply(item)


def yield_items_in_itemplus_or_group(item_or_group: ItemPlus | ItemPlusGroup):
    if isinstance(item_or_group, ItemPlus):
        yield item_or_group
    if isinstance(item_or_group, ItemPlusGroup):
        for item in item_or_group._contained:
            yield item
