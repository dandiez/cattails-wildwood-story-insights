import os
from dataclasses import asdict

from cws_insights.common import WIKI_CONTENTS_DIR
from cws_insights.merged_data.items import ItemPlus, AllItemPlus, get_merged_item_data
from cws_insights.read_files import read_all_resource_files
from cws_insights.read_files_data import instantiate_all_resource_data
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
        if any(
            v is not None for v in filters_as_dict.values()
        ):
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

def yield_lines_from_item_plus(i: ItemPlus):
    yield f"# {i.item_lang.lang_item_name}"
    yield i.item_lang.lang_item_description
    yield from yield_lines_item_attributes(i.item)
    yield from yield_lines_shopping_block(i)


def write_item_merged_data(item_merged: AllItemPlus, wiki_contents_dir: str):
    os.makedirs(wiki_contents_dir, exist_ok=True)
    for item_uid, item in item_merged.items():
        file = os.path.join(wiki_contents_dir, item_uid + ".md")
        lines = list(yield_lines_from_item_plus(item))
        text = "\n\n".join(lines)
        with open(file, "w") as f:
            f.write(text)
        print(f"written {file}")


def main(gameresources_dir, wiki_contents_dir):
    all_raw_files = read_all_resource_files(gameresources_dir)
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    item_merged = get_merged_item_data(all_resource_data)
    write_item_merged_data(item_merged, os.path.join(wiki_contents_dir, "items"))


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
