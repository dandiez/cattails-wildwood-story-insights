import os
from dataclasses import asdict

from cws_insights.common import WIKI_CONTENTS_DIR
from cws_insights.merged_data.items import (
    ItemPlus,
    AllItemPlus,
    get_merged_item_data,
    UidStem,
    RecipeVariant,
)
from cws_insights.read_files import read_all_resource_files
from cws_insights.read_files_data import instantiate_all_resource_data
from cws_insights.schemas._index import AllResourceData
from cws_insights.schemas.items_meta import ItemMeta


def yield_lines_shopping_block(i: ItemPlus):
    non_dev_shops = [
        shop
        for shop in i.from_shops
        if shop.shop_selling_it.shop_title != "dev_shop_name"
    ]
    if not non_dev_shops:
        return
    yield f"# shops selling {i.item_lang.lang_item_name}:"
    for shop in non_dev_shops:
        yield f"{shop.shop_selling_it.shop_title} sells it for {shop.sale_details.item_base_price} {shop.shop_selling_it.currency_type}."
        filters = shop.sale_details.item_filters
        filters_as_dict = filters.__dict__
        if any(v is not None for v in filters_as_dict.values()):
            yield f"  can buy it when meeting conditions: "
            if filters.filter_day is not None:
                yield f"    - at least {filters.filter_day} have passed"
            if filters.filter_year is not None:
                yield f"    - at least we are on year {filters.filter_year}"
            if filters.filter_friendship_alabaster is not None:
                yield f"    - at least we have a friendship level {filters.filter_friendship_alabaster} with Alabaster"
            if filters.filter_autumn:
                yield f"    - it is autumn"
            if filters.filter_spring:
                yield f"    - it is spring"
            if filters.filter_summer:
                yield f"    - it is summer"
            if filters.filter_winter:
                yield f"    - it is winter"


def yield_lines_item_attributes(i: ItemMeta):
    for k, v in asdict(i).items():
        if not k.startswith("item_"):
            continue
        if v is not None:
            yield f"{k}: {v}"


def _npc_nice_names(npc_stem_ids: list[UidStem], all_data: AllResourceData):
    # TODO have a merge for NPCs already with name and language and link it to the item instead of the Uidstem
    return [
        all_data.npcs_lang_english_lang[npcstem].lang_npc_name
        for npcstem in npc_stem_ids
    ]


def yield_lines_npc_block(i: ItemPlus, all_data: AllResourceData):
    from_npcs = i.from_npc
    if any(asdict(from_npcs).values()):
        yield f"# Gift guide"
        if from_npcs.npc_loves:
            yield f"NPCs that love {i.item_lang.lang_item_name}: " + ", ".join(
                _npc_nice_names(from_npcs.npc_loves, all_data)
            )
        if from_npcs.npc_likes:
            yield f"NPCs that like {i.item_lang.lang_item_name}: " + ", ".join(
                _npc_nice_names(from_npcs.npc_likes, all_data)
            )
        if from_npcs.npc_dislikes:
            yield f"NPCs that dislike {i.item_lang.lang_item_name}: " + ", ".join(
                _npc_nice_names(from_npcs.npc_dislikes, all_data)
            )
        if from_npcs.npc_hates:
            yield f"NPCs that hate {i.item_lang.lang_item_name}: " + ", ".join(
                _npc_nice_names(from_npcs.npc_hates, all_data)
            )
        if from_npcs.npc_gifts:
            yield f"A gift from: " + ", ".join(
                _npc_nice_names(from_npcs.npc_gifts, all_data)
            )


SEASONS = ("winter", "spring", "summer", "autumn")


def yield_lines_item_herb(i: ItemPlus):
    herb_data = i.from_herbs
    if any(v for v in asdict(herb_data).values()):
        yield f"# Herb data"
        if herb_data.ranked_herbs:
            yield f"{i.item_lang.lang_item_name} is a ranked herb which can be found in different qualities."
        else:
            yield f"{i.item_lang.lang_item_name} is not a ranked herb and only exists in one quality."
        yield f"{i.item_lang.lang_item_name} is{' not ' if not herb_data.bush_herbs else ' '}a bush herb."
        yield f"{i.item_lang.lang_item_name} is a{' night ' if herb_data.night_herbs else ' daytime '}herb."
        seasons = [s for s in SEASONS if asdict(herb_data)[s]]
        if seasons:
            yield f"{i.item_lang.lang_item_name} grow seasons: " + ", ".join(seasons)


def _recipe_variant_as_str(variant: RecipeVariant) -> str:
    v = variant
    return (
        " + ".join([f"{inp.quantity} {inp.uid}" for inp in v.input])
        + f" --> {v.output.quantity} {v.output.uid}"
    )


def yield_lines_recipes(i: ItemPlus):
    # TODO: Improve this after merging recipes with crafting stations, etc.
    if not (i.from_recipes.as_input or i.from_recipes.as_output):
        return
    yield f"# Recipes"
    if i.from_recipes.as_output:
        yield f"Recipes that produce {i.item_lang.lang_item_name}:"
        for r in i.from_recipes.as_output:
            yield _recipe_variant_as_str(r)
    if i.from_recipes.as_input:
        yield f"Recipes that consume {i.item_lang.lang_item_name}:"
        for r in i.from_recipes.as_input:
            yield _recipe_variant_as_str(r)

def yield_lines_from_map_regions(i: ItemPlus , all_data: AllResourceData):
    regions = i.from_map
    if any((regions.spawners, regions.prey_list, regions.herb_list)):
        yield "# Map regions"
    if regions.spawners:
        yield f"{i.item_lang.lang_item_name} spawns in " + ', '.join(set(regions.spawners))
    if regions.prey_list:
        yield f"{i.item_lang.lang_item_name} is prey in " + ', '.join(set(regions.prey_list))
    if regions.herb_list:
        yield f"{i.item_lang.lang_item_name} grows as herb in "+ ', '.join(set(regions.herb_list))
    if regions.world_objects:
        yield f"{i.item_lang.lang_item_name} can be found in "+ ', '.join(set(regions.world_objects))

def yield_lines_from_item_plus(i: ItemPlus, all_resource_data: AllResourceData):
    yield f"# {i.item_lang.lang_item_name}"
    yield i.item_lang.lang_item_description
    yield from yield_lines_item_attributes(i.item)
    yield from yield_lines_from_map_regions(i, all_resource_data)
    yield from yield_lines_item_herb(i)
    yield from yield_lines_shopping_block(i)
    yield from yield_lines_npc_block(i, all_resource_data)
    yield from yield_lines_recipes(i)



def write_item_merged_data(
    item_merged: AllItemPlus, wiki_contents_dir: str, all_resource_data: AllResourceData
):
    os.makedirs(wiki_contents_dir, exist_ok=True)
    for item_uid, item in item_merged.items():
        file = os.path.join(wiki_contents_dir, item_uid + ".md")
        lines = list(yield_lines_from_item_plus(item, all_resource_data))
        text = "\n\n".join(lines)
        with open(file, "w") as f:
            f.write(text)
        print(f"written {file}")


def main(gameresources_dir, wiki_contents_dir):
    all_raw_files = read_all_resource_files(gameresources_dir)
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    item_merged = get_merged_item_data(all_resource_data)
    write_item_merged_data(
        item_merged, os.path.join(wiki_contents_dir, "items"), all_resource_data
    )


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
