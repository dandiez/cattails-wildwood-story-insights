from cws_insights.merged_data.items import UidStem
from cws_insights.schemas._index import AllResourceData

SEASONS = ("winter", "spring", "summer", "autumn")


def _npc_nice_names(npc_stem_ids: list[UidStem], all_data: AllResourceData):
    # TODO have a merge for NPCs already with name and language and link it to the item instead of the Uidstem
    return [
        all_data.npcs_lang_english_lang[npcstem].lang_npc_name
        for npcstem in npc_stem_ids
    ]
