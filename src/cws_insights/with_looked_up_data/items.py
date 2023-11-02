import dataclasses
from collections import defaultdict
from typing import TypeAlias, Callable

from cws_insights.common import WIKI_CONTENTS_DIR
from cws_insights.definitions import Undefined
from cws_insights.read_files_data import instantiate_all_resource_data
from cws_insights.read_files import (
    read_all_resource_files,
)
from cws_insights.schemas._index import AllResourceData
from cws_insights.schemas.herbs_meta import HerbMeta as Herb
from cws_insights.schemas.items_meta import ItemMeta as Item
from cws_insights.schemas.items_lang_english_lang import ItemLangEnglishLang as ItemLangEnglish
from cws_insights.schemas.items_recipes_meta import ItemRecipeMeta as ItemRecipe
from cws_insights.schemas.map_region import MapRegion as Map
from cws_insights.schemas.npcs_meta import NpcMeta as Npc

Uid: TypeAlias = str
UidStem: TypeAlias = str


@dataclasses.dataclass
class ItemFromNpc:
    npc_loves: list[Npc] = dataclasses.field(default_factory=list)
    npc_likes: list[Npc] = dataclasses.field(default_factory=list)
    npc_dislikes: list[Npc] = dataclasses.field(default_factory=list)
    npc_hates: list[Npc] = dataclasses.field(default_factory=list)
    npc_gifts: list[Npc] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ItemFromMap:
    herb_list: list[Map] =dataclasses.field(default_factory=list)
    prey_list: list[Map]=dataclasses.field(default_factory=list)
    spawners: list[Map]=dataclasses.field(default_factory=list)


@dataclasses.dataclass
class ItemFromHerbs:
    ranked_herbs: bool
    bush_herbs: bool
    night_herbs: bool
    autumn: bool
    spring: bool
    summer: bool
    winter: bool


@dataclasses.dataclass
class ItemFromItemRecipe:
    as_input: list[ItemRecipe]
    as_output: list[ItemRecipe]


@dataclasses.dataclass
class ItemPlus:
    item: Item = None
    herb_uid: Uid = None
    item_lang: ItemLangEnglish = None
    sprite: str = None
    from_npc: ItemFromNpc = dataclasses.field(default_factory=ItemFromNpc)
    from_map: ItemFromMap = dataclasses.field(default_factory=ItemFromMap)
    from_herbs: ItemFromHerbs = None
    from_recipes: ItemFromItemRecipe = None


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


def get_stem_from_uid(uid: Uid) -> UidStem:
    return uid.lower().replace(" ", "").replace("[", "").replace("]", "")


def _get_sprite(all_item_plus: AllItemPlus):
    for i in all_item_plus.values():
        i.sprite = get_stem_from_uid(i.item.item_uid) + "_wildwood_story.png"


def _get_npc_data(npcs: dict[Uid, Npc], all_item_plus: AllItemPlus):
    for npc in npcs.values():
        if npc.npc_item_loves is not Undefined:
            for item_uid in npc.npc_item_loves:
                all_item_plus[item_uid].from_npc.npc_loves.append(npc)
        if npc.npc_item_likes is not Undefined:
            for item_uid in npc.npc_item_likes:
                all_item_plus[item_uid].from_npc.npc_likes.append(npc)
        if npc.npc_item_dislikes is not Undefined:
            for item_uid in npc.npc_item_dislikes:
                all_item_plus[item_uid].from_npc.npc_dislikes.append(npc)
        if npc.npc_item_hates is not Undefined:
            for item_uid in npc.npc_item_hates:
                all_item_plus[item_uid].from_npc.npc_hates.append(npc)

        if npc.npc_item_gifts is not Undefined:
            for item_uid in npc.npc_item_gifts:
                all_item_plus[item_uid].from_npc.npc_gifts.append(npc)

def apply_function_to_item_plus_with_groups(item_or_group: ItemPlus | ItemPlusGroup, function_to_apply: Callable):
    if isinstance(item_or_group, ItemPlus):
        function_to_apply(item_or_group)
    if isinstance(item_or_group, ItemPlusGroup):
        for item in item_or_group._contained:
            function_to_apply(item)

def _get_map_data(
    map: dict[Uid, Map], all_item_plus_with_groups: AllItemPlusWithGroups
):
    for region in map.values():
        for herb in region.region_data.herbs_list:
            f = lambda x: x.from_map.herb_list.append(region)
            apply_function_to_item_plus_with_groups(all_item_plus_with_groups[herb], f)
        for prey in region.region_data.prey_list:
            all_item_plus_with_groups[prey].from_map.prey_list.append(region)
        for spawner in region.region_data.spawners:
            for item_id in spawner.item_uids:
                all_item_plus_with_groups[item_id].from_map.spawners.append(region)

def get_merged_item_data(all_resource_data: AllResourceData):
    double_check_assumptions(all_resource_data)

    all_items_indexed_by_uid = {
        item.item_uid: item for item in all_resource_data.items_meta.values() if item.item_uid is not None
    }
    all_item_plus = {
        item.item_uid: ItemPlus(item=item)
        for item in all_items_indexed_by_uid.values()
        if item.item_uid is not None
    }

    grouped_items_by_group_id = _get_grouped_items(all_item_plus)
    _merge_with_item_lang_data(all_resource_data.items_lang_english_lang, all_item_plus)
    _get_sprite(all_item_plus)
    _get_npc_data(all_resource_data.npcs_meta, all_item_plus)
    all_item_plus_with_groups = grouped_items_by_group_id | all_item_plus
    _get_map_data(all_resource_data.map_region, all_item_plus_with_groups)
    return all_item_plus_with_groups


def double_check_assumptions(all_resource_data: AllResourceData):
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


def _merge_with_item_lang_data(
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


def write_item_merged_data(item_merged: dict[Uid, ItemPlus], wiki_contents_dir):
    n = 100
    for k, v in item_merged.items():
        print(k, type(v), v)
        if n == 0:
            break
        n -= 1
    print(item_merged["Blackberries [Poor]"])
    g = item_merged["Blackberries"]
    g.herb_uid = "Blackberries!"
    for k, v in item_merged.items():
        if not isinstance(v, ItemPlus):  # TODO: For writing, get rid of groups
            continue
        if v.herb_uid == "Blackberries!":
            print(v)


def main(gameresources_dir, wiki_contents_dir):
    extensions_to_consider = (".meta", ".lang", ".region")
    all_raw_files = read_all_resource_files(
        gameresources_dir, file_suffixes=extensions_to_consider
    )
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    item_merged = get_merged_item_data(all_resource_data)
    write_item_merged_data(item_merged, wiki_contents_dir)


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
