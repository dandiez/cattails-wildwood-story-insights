import dataclasses
import os.path

import pandas as pd

from cws_insights.common import SITE_SRC_DIR, CI_CD_GAMERESOURCES_DIR
from cws_insights.definitions import Undefined
from cws_insights.read_files_data import instantiate_all_resource_data
from cws_insights.read_files import (
    read_all_resource_files,
)
from cws_insights.schemas.items_meta import ItemMeta as Item
from cws_insights.schemas.items_lang_english_lang import ItemLangEnglishLang as ItemLangEnglish
from cws_insights.schemas.npcs_meta import NpcMeta as Npc
from cws_insights.schemas.npcs_lang_english_lang import NpcLangEnglishLang as NpcLangEnglish


@dataclasses.dataclass
class Asciis:
    loves: str
    likes: str
    dislikes: str
    hates: str


@dataclasses.dataclass
class TableRecord:
    item: Item
    item_lang: ItemLangEnglish
    npc: Npc
    npc_lang: NpcLangEnglish
    npc_attitude_towards_item: str


def main(gameresources_dir: str, site_src_dir: str, icons: Asciis):
    extensions_to_consider = (".meta", ".lang")
    all_raw_files = read_all_resource_files(
        gameresources_dir, file_suffixes=extensions_to_consider
    )
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    all_items = all_resource_data.items_meta
    all_items_lang = all_resource_data.items_lang_english_lang
    all_npcs = all_resource_data.npcs_meta
    all_npcs_lang = all_resource_data.npcs_lang_english_lang
    all_items_indexed_by_uid = {item.item_uid: item for item in all_items.values()}
    all_items_lang_indexed_by_uid = {
        item_lang.item_uid_do_not_translate: item_lang
        for item_lang in all_items_lang.values()
    }

    npcs_that_can_receive_gifts = {
        npc_stem
        for npc_stem, npc in all_npcs.items()
        if npc.npc_item_loves is not Undefined
    }
    all_item_uids_that_can_be_gifted = set.union(
        *[
            set.union(
                set(npc.npc_item_loves),
                set(npc.npc_item_likes),
                set(npc.npc_item_dislikes),
                set(npc.npc_item_hates),
            )
            for npc_stem, npc in all_npcs.items()
            if npc_stem in npcs_that_can_receive_gifts
        ]
    )

    table_records = [
        TableRecord(
            item=all_items_indexed_by_uid[item_uid],
            item_lang=all_items_lang_indexed_by_uid[item_uid],
            npc=all_npcs[npc_stem],
            npc_lang=all_npcs_lang[npc_stem],
            npc_attitude_towards_item=feeling_towards_item(
                all_npcs[npc_stem], item_uid, icons
            ),
        )
        for item_uid in all_item_uids_that_can_be_gifted
        for npc_stem in npcs_that_can_receive_gifts
    ]
    unpivoted_table = pd.DataFrame(
        [
            {
                "sort": r.item.item_sorting_priority,
                "mews": r.item.item_mews_value,
                "item": r.item_lang.lang_item_name,
                "cat_name": r.npc_lang.lang_npc_name,
                "attitude": r.npc_attitude_towards_item,
            }
            for r in table_records
        ]
    )
    unpivoted_table_sorted = unpivoted_table.sort_values(["sort", "cat_name"])
    pivoted_table = unpivoted_table_sorted.pivot_table(
        values="attitude",
        index=["sort", "mews", "item"],
        columns=["cat_name"],
        aggfunc=lambda x: "-".join(x),
    ).reset_index()
    pivoted_table.to_csv(os.path.join(site_src_dir, "gifts.csv"), index=False)
    as_markdown = pivoted_table.to_markdown(tablefmt="github", index=False)
    download_notice = f"[Download as csv](gifts.csv)"
    text = f"""
# Gifts / Items

{download_notice}

{as_markdown}
    """
    with open(
        os.path.join(site_src_dir, "gifts.md"),
        "w",
        encoding="utf8",
    ) as f:
        f.write(text)


def feeling_towards_item(npc: Npc, item_uid: str, icons: Asciis) -> str:
    feeling = ""
    if item_uid in npc.npc_item_loves:
        feeling += icons.loves
    if item_uid in npc.npc_item_likes:
        feeling += icons.likes
    if item_uid in npc.npc_item_dislikes:
        feeling += icons.dislikes
    if item_uid in npc.npc_item_hates:
        feeling += icons.hates
    return feeling


if __name__ == "__main__":
    gameresources_dir = CI_CD_GAMERESOURCES_DIR
    site_src_dir = SITE_SRC_DIR
    icons = Asciis(
        loves="❤️",
        likes="👍",
        dislikes="👎",
        hates="👿",
    )
    main(gameresources_dir, site_src_dir, icons)
