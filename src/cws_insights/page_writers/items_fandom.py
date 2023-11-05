import dataclasses
import os
from typing import TypeAlias, Any



from cws_insights.common import WIKI_CONTENTS_DIR
from cws_insights.merged_data.items import ItemPlus, get_merged_item_data, AllItemPlus
from cws_insights.page_writers.common import SEASONS, _npc_nice_names
from cws_insights.page_writers.items_md import _recipe_variant_as_str
from cws_insights.page_writers.lookups_fandom import UNITS_FANDOM, get_npc_page_link
from cws_insights.read_files import read_all_resource_files
from cws_insights.read_files_data import instantiate_all_resource_data
from cws_insights.schemas._index import AllResourceData
from cws_insights.schemas.items_meta import ItemMeta

SHOPS_IN_FANDOM_TEMPLATE = {
    "alabaster_shop_name",
    "coco_festival_shop_name",
    "ember_shop_name",
    "molay_shop_name",
    "mold_shop_name",
    "molo_shop_name",
    "molu_shop_name",
    "taskboard_shop_name",
}


@dataclasses.dataclass
class WSItem:
    """Data to fill in the fandom item template

    https://cattails-game.fandom.com/wiki/Template:WSItem
    """

    title1: str = ""
    aka_name: str = ""
    image1: str = ""
    description: str = ""
    rarity: str = ""
    sell_value: str = ""
    prey_value: str = ""
    herb_value: str = ""
    sand_value: str = ""
    stone_value: str = ""
    treasure_value: str = ""
    wood_value: str = ""
    catnip_amount: str = ""
    confusion_amount: str = ""
    cures_poison: str = ""
    heal_amount: str = ""
    attack_amount: str = ""
    buddy_xp_amount: str = ""
    hunger_amount: str = ""
    immunity_amount: str = ""
    influence_amount: str = ""
    has_random_effect: str = ""
    special_effect: str = ""
    speed_amount: str = ""
    stealth_amount: str = ""
    swim_amount: str = ""
    venom_amount: str = ""
    can_explode: str = ""
    is_farsighted: str = ""
    is_ranked_herb: str = ""
    is_bush_herb: str = ""
    is_day_or_night_herb: str = ""
    grow_seasons: str = ""
    alabaster_shop: str = ""
    ember_shop: str = ""
    coco_festival_shop: str = ""
    molay_shop: str = ""
    mold_shop: str = ""
    molo_shop: str = ""
    molu_shop: str = ""
    taskboard_shop: str = ""
    love_it: str = ""
    like_it: str = ""
    dislike_it: str = ""
    hate_it: str = ""
    a_gift_from: str = ""
    recipes_consuming: str = ""
    recipes_producing: str = ""
    regions_spawn: str = ""
    regions_herb: str = ""
    regions_prey: str = ""
    regions_world_objects: str = ""

    def yield_lines(self):
        yield "{{WSItem"
        for k, v in dataclasses.asdict(self).items():
            yield f"|{k}={v}"
        yield "}}"

    def set_shop_value(self, shop_title: str, value: str):
        match shop_title:
            case "alabaster_shop_name":
                self.alabaster_shop = value
            case "coco_festival_shop_name":
                self.coco_festival_shop = value
            case "ember_shop_name":
                self.ember_shop = value
            case "molay_shop_name":
                self.molay_shop = value
            case "mold_shop_name":
                self.mold_shop = value
            case "molo_shop_name":
                self.molo_shop = value
            case "molu_shop_name":
                self.molu_shop = value
            case "taskboard_shop_name":
                self.taskboard_shop = value
            case other:
                raise ValueError(other)


Uid: TypeAlias = str
AllWsItem: TypeAlias = dict[Uid, WSItem]


def to_str(property: Any):
    """Return '' if property is None. Otherwise, its string representation."""
    if property is None:
        return ""
    if property is True:
        return "Yes"
    if property is False:
        return "No"
    return str(property)


def to_str_with_units(value: Any, units: str):
    return f"{value} {units}" if value is not None else ""


def hunger_to_str(hunger_amount: int):
    if hunger_amount is not None:
        return str(hunger_amount // 100) + "hunger bars"
    return ""


def populate_attributes(wsi: WSItem, i: ItemMeta):
    # main_properties = {
    wsi.rarity = to_str(i.item_rarity)
    #   "Item uid: {}": i.item_uid,
    #    "Sorting priority: {}": i.item_sorting_priority,

    wsi.catnip_amount = to_str(i.item_catnip_amount)
    wsi.confusion_amount = to_str(i.item_confusion_amount)
    wsi.cures_poison = to_str(i.item_cures_poison)
    wsi.heal_amount = to_str(i.item_heal_amount)
    wsi.attack_amount = to_str(i.item_attack_amount)
    wsi.buddy_xp_amount = to_str(i.item_buddy_xp_amount)
    wsi.hunger_amount = to_str(i.item_hunger_amount)
    wsi.attack_amount = to_str(i.item_attack_amount)
    wsi.immunity_amount = to_str(i.item_immunity_amount)
    wsi.influence_amount = to_str(i.item_influence_amount)
    wsi.has_random_effect = to_str(i.item_random_effect)
    wsi.special_effect = to_str(i.item_special_effect)
    wsi.speed_amount = to_str(i.item_speed_amount)
    wsi.stealth_amount = to_str(i.item_stealth_amount)
    wsi.swim_amount = to_str(i.item_swim_amount)
    wsi.venom_amount = to_str(i.item_venom_amount)
    wsi.can_explode = to_str(i.item_can_explode)
    wsi.is_farsighted = to_str(i.item_is_farsighted)

    mews = to_str_with_units(i.item_mews_value, UNITS_FANDOM.mews)
    mole = to_str_with_units(i.item_mole_cash_value, UNITS_FANDOM.mole_cash)
    sell_value_str = ", ".join((mews, mole)) if mews or mole else ""
    wsi.sell_value = sell_value_str

    wsi.prey_value = to_str_with_units(i.item_prey_resource_value, UNITS_FANDOM.prey)
    wsi.herb_value = to_str_with_units(i.item_herbs_resource_value, UNITS_FANDOM.herb)
    wsi.sand_value = to_str_with_units(i.item_sand_resource_value, UNITS_FANDOM.sand)
    wsi.stone_value = to_str_with_units(i.item_stone_resource_value, UNITS_FANDOM.stone)
    wsi.treasure_value = to_str_with_units(
        i.item_treasure_resource_value, UNITS_FANDOM.treasure
    )
    wsi.wood_value = to_str_with_units(i.item_wood_resource_value, UNITS_FANDOM.wood)


def populate_map_regions(wsi: WSItem, i: ItemPlus):
    regions = i.from_map
    if regions.spawners:
        wsi.regions_spawn = ", ".join(sorted(set(regions.spawners)))
    if regions.prey_list:
        wsi.regions_prey = ", ".join(sorted(set(regions.prey_list)))
    if regions.herb_list:
        wsi.regions_herb = ", ".join(sorted(set(regions.herb_list)))
    if regions.world_objects:
        wsi.regions_world_objects = ", ".join(sorted(set(regions.world_objects)))


def populate_herb(wsi: WSItem, i: ItemPlus):
    herb_data = i.from_herbs
    if any(v for v in dataclasses.asdict(herb_data).values()):
        if herb_data.ranked_herbs:
            wsi.is_ranked_herb = "Yes, it can be found in different qualities."
        else:
            wsi.is_ranked_herb = "No, it only exists in one quality."
        wsi.is_bush_herb = to_str(herb_data.bush_herbs)
        wsi.is_day_or_night_herb = "night" if herb_data.night_herbs else "daytime"
        seasons = [s for s in SEASONS if dataclasses.asdict(herb_data)[s]]
        wsi.grow_seasons = ", ".join(seasons)


def populate_shopping(wsi: WSItem, i: ItemPlus):
    for shop in i.from_shops:
        if shop.shop_selling_it.shop_title == "dev_shop_name":
            continue
        value_with_units = to_str_with_units(
            shop.sale_details.item_base_price,
            UNITS_FANDOM.from_shop_currency_type(shop.shop_selling_it.currency_type),
        )
        conditions = _shop_availability_conditions(shop.sale_details.item_filters)
        shop_str = value_with_units + conditions
        wsi.set_shop_value(shop.shop_selling_it.shop_title, shop_str)


def _shop_availability_conditions(filters) -> str:
    filters_as_dict = filters.__dict__
    if any(v is not None for v in filters_as_dict.values()):
        return f" *can buy it when meeting conditions: " + ", ".join(
            list(_enumerated_conditions(filters))
        )
    return ""


def _enumerated_conditions(filters):
    if filters.filter_day is not None:
        yield f"at least we are on day {filters.filter_day}"
    if filters.filter_year is not None:
        yield f"at least we are on year {filters.filter_year}"
    if filters.filter_friendship_alabaster is not None:
        yield f"at least we have a friendship level {filters.filter_friendship_alabaster} with Alabaster"
    if filters.filter_autumn:
        yield f"it is autumn"
    if filters.filter_spring:
        yield f"it is spring"
    if filters.filter_summer:
        yield f"it is summer"
    if filters.filter_winter:
        yield f"it is winter"


def populate_npc_data(wsi: WSItem, i: ItemPlus, all_data: AllResourceData):
    from_npcs = i.from_npc
    if any(dataclasses.asdict(from_npcs).values()):
        if from_npcs.npc_loves:
            wsi.love_it = ", ".join(get_npc_page_link(npc) for npc in
                _npc_nice_names(from_npcs.npc_loves, all_data)
            )
        if from_npcs.npc_likes:
            wsi.like_it = ", ".join(get_npc_page_link(npc) for npc in
                _npc_nice_names(from_npcs.npc_likes, all_data)
            )
        if from_npcs.npc_dislikes:
            wsi.dislike_it = ", ".join(get_npc_page_link(npc) for npc in
                _npc_nice_names(from_npcs.npc_dislikes, all_data)
            )
        if from_npcs.npc_hates:
            wsi.hate_it =", ".join(get_npc_page_link(npc) for npc in
                _npc_nice_names(from_npcs.npc_hates, all_data)
            )
        if from_npcs.npc_gifts:
            wsi.a_gift_from = ", ".join(get_npc_page_link(npc) for npc in
                _npc_nice_names(from_npcs.npc_gifts, all_data)
            )

def populate_recipes(wsi: WSItem, i: ItemPlus):
    if i.from_recipes.as_output:
        wsi.recipes_producing = "\n\n ".join(_recipe_variant_as_str(r) for r in i.from_recipes.as_output)
    if i.from_recipes.as_input:
        wsi.recipes_consuming = "\n\n ".join(_recipe_variant_as_str(r) for r in i.from_recipes.as_input)



def prepare_item(i: ItemPlus, all_resource_data: AllResourceData) -> WSItem:
    wsi = WSItem()
    wsi.title1 = i.item_lang.item_uid_do_not_translate
    wsi.aka_name = i.item_lang.lang_item_name if i.item_lang.lang_item_name != i.item_lang.item_uid_do_not_translate else ""
    wsi.image1 = i.item.item_uid + ".png"
    wsi.description = i.item_lang.lang_item_description
    populate_attributes(wsi, i.item)
    populate_map_regions(wsi, i)
    populate_herb(wsi, i)
    populate_shopping(wsi, i)
    populate_npc_data(wsi, i, all_resource_data)
    populate_recipes(wsi, i)
    return wsi

def get_all_ws_items(
    item_merged: AllItemPlus, all_resource_data: AllResourceData
) -> AllWsItem:
    return {
        item_uid: prepare_item(i, all_resource_data)
        for item_uid, i in item_merged.items()
    }


def write_all_ws_items(item_merged: AllWsItem, wiki_contents_dir: str):
    os.makedirs(wiki_contents_dir, exist_ok=True)
    for item_uid, item in item_merged.items():
        file = os.path.join(wiki_contents_dir, item_uid + ".mediawiki")
        lines = list(item.yield_lines())
        text = "\n".join(lines)
        with open(file, "w") as f:
            f.write(text)
        print(f"written {file}")


def main(gameresources_dir, wiki_contents_dir):
    all_raw_files = read_all_resource_files(gameresources_dir)
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    item_merged = get_merged_item_data(all_resource_data)
    ws_items = get_all_ws_items(item_merged, all_resource_data)
    write_all_ws_items(ws_items, os.path.join(wiki_contents_dir, "fandom_items"))


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
