import os

from cws_insights.common import WIKI_CONTENTS_DIR
from cws_insights.merged_data.items import ItemPlus, AllItemPlus, get_merged_item_data
from cws_insights.read_files import read_all_resource_files
from cws_insights.read_files_data import instantiate_all_resource_data


def yield_lines_shopping_block(i: ItemPlus):
    shops_selling = [
        shop.shop_selling_it.shop_title
        for shop in i.from_shops
        if shop.shop_selling_it.shop_title != "dev_shop_name"
    ]
    if not shops_selling:
        return
    yield f"# shops selling {i.item_lang.lang_item_name}:"
    for shopdata in i.from_shops:
        if shopdata.shop_selling_it.shop_title == "dev_shop_name":
            continue
        yield f"{shopdata.shop_selling_it.shop_title} sells it for {shopdata.sale_details.item_base_price} {shopdata.shop_selling_it.currency_type}."
        if any(
            v is not None for v in shopdata.sale_details.item_filters.__dict__.values()
        ):
            yield f"can buy it when meeting conditions: "
            for (
                filter_name,
                filter,
            ) in shopdata.sale_details.item_filters.__dict__.items():
                if filter is not None:
                    yield f"{filter_name} = {filter}"


def yield_lines_from_item_plus(i: ItemPlus):
    yield f"# {i.item_lang.lang_item_name}"
    yield i.item_lang.lang_item_description
    yield f"raritiy: {i.item.item_rarity}"
    if i.item.item_mews_value is not None:
        yield f"sell value: {i.item.item_mews_value} Mews"
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
    write_item_merged_data(item_merged, wiki_contents_dir)


if __name__ == "__main__":
    gameresources_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Cattails Wildwood Story\gameresources"
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
