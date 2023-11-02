import dataclasses

from cws_insights.schemas.buildings_lang_english_lang import BuildingLangEnglishLang
from cws_insights.schemas.buildings_lang_german_lang import BuildingLangGermanLang
from cws_insights.schemas.buildings_lang_spanish_lang import BuildingLangSpanishLang
from cws_insights.schemas.buildings_meta import BuildingMeta
from cws_insights.schemas.bundles_meta import BundleMeta
from cws_insights.schemas.colony_layouts_lang_english_lang import (
    ColonyLayoutLangEnglishLang,
)
from cws_insights.schemas.colony_layouts_lang_german_lang import (
    ColonyLayoutLangGermanLang,
)
from cws_insights.schemas.colony_layouts_lang_spanish_lang import (
    ColonyLayoutLangSpanishLang,
)
from cws_insights.schemas.colony_layouts_meta import ColonyLayoutMeta
from cws_insights.schemas.crafting_stations_meta import CraftingStationMeta
from cws_insights.schemas.events_lang_english_lang import EventLangEnglishLang
from cws_insights.schemas.events_lang_german_lang import EventLangGermanLang
from cws_insights.schemas.events_lang_spanish_lang import EventLangSpanishLang
from cws_insights.schemas.events_meta import EventMeta
from cws_insights.schemas.festivals_lang_english_lang import FestivalLangEnglishLang
from cws_insights.schemas.festivals_lang_german_lang import FestivalLangGermanLang
from cws_insights.schemas.festivals_lang_spanish_lang import FestivalLangSpanishLang
from cws_insights.schemas.festivals_meta import FestivalMeta
from cws_insights.schemas.furniture_lang_english_lang import FurnitureLangEnglishLang
from cws_insights.schemas.furniture_lang_german_lang import FurnitureLangGermanLang
from cws_insights.schemas.furniture_lang_spanish_lang import FurnitureLangSpanishLang
from cws_insights.schemas.furniture_meta import FurnitureMeta
from cws_insights.schemas.herbs_meta import HerbMeta
from cws_insights.schemas.items_accessories_meta import ItemAccessoryMeta
from cws_insights.schemas.items_lang_english_lang import ItemLangEnglishLang
from cws_insights.schemas.items_lang_german_lang import ItemLangGermanLang
from cws_insights.schemas.items_lang_spanish_lang import ItemLangSpanishLang
from cws_insights.schemas.items_meta import ItemMeta
from cws_insights.schemas.items_recipes_meta import ItemRecipeMeta
from cws_insights.schemas.languages_lang import LanguageLang
from cws_insights.schemas.mail_lang_english_lang import MailLangEnglishLang
from cws_insights.schemas.mail_lang_german_lang import MailLangGermanLang
from cws_insights.schemas.mail_lang_spanish_lang import MailLangSpanishLang
from cws_insights.schemas.mail_meta import MailMeta
from cws_insights.schemas.map_lang_english_lang import MapLangEnglishLang
from cws_insights.schemas.map_lang_german_lang import MapLangGermanLang
from cws_insights.schemas.map_lang_spanish_lang import MapLangSpanishLang
from cws_insights.schemas.map_meta import MapMeta
from cws_insights.schemas.map_region import MapRegion
from cws_insights.schemas.music_packs_meta import MusicPackMeta
from cws_insights.schemas.npcs_lang_english_lang import NpcLangEnglishLang
from cws_insights.schemas.npcs_lang_german_lang import NpcLangGermanLang
from cws_insights.schemas.npcs_lang_spanish_lang import NpcLangSpanishLang
from cws_insights.schemas.npcs_meta import NpcMeta
from cws_insights.schemas.npcs_shops_meta import NpcShopMeta
from cws_insights.schemas.rival_marriages_meta import RivalMarriageMeta
from cws_insights.schemas.tasks_lang_english_lang import TaskLangEnglishLang
from cws_insights.schemas.tasks_lang_german_lang import TaskLangGermanLang
from cws_insights.schemas.tasks_lang_spanish_lang import TaskLangSpanishLang
from cws_insights.schemas.tasks_meta import TaskMeta
from cws_insights.schemas.time_meta import TimeMeta
from cws_insights.schemas.wedding_venues_lang_english_lang import (
    WeddingVenueLangEnglishLang,
)
from cws_insights.schemas.wedding_venues_lang_german_lang import (
    WeddingVenueLangGermanLang,
)
from cws_insights.schemas.wedding_venues_lang_spanish_lang import (
    WeddingVenueLangSpanishLang,
)
from cws_insights.schemas.wedding_venues_meta import WeddingVenueMeta
from cws_insights.schemas.world_objects_lang_english_lang import (
    WorldObjectLangEnglishLang,
)
from cws_insights.schemas.world_objects_lang_german_lang import (
    WorldObjectLangGermanLang,
)
from cws_insights.schemas.world_objects_lang_spanish_lang import (
    WorldObjectLangSpanishLang,
)
from cws_insights.schemas.world_objects_meta import WorldObjectMeta

COLLECTION_REL_PATH_TO_DATACLASS_MAPPING = {
    "buildings/lang/english/lang": BuildingLangEnglishLang,
    "buildings/lang/german/lang": BuildingLangGermanLang,
    "buildings/lang/spanish/lang": BuildingLangSpanishLang,
    "buildings/meta": BuildingMeta,
    "bundles/meta": BundleMeta,
    "colony_layouts/lang/english/lang": ColonyLayoutLangEnglishLang,
    "colony_layouts/lang/german/lang": ColonyLayoutLangGermanLang,
    "colony_layouts/lang/spanish/lang": ColonyLayoutLangSpanishLang,
    "colony_layouts/meta": ColonyLayoutMeta,
    "crafting_stations/meta": CraftingStationMeta,
    "events/lang/english/lang": EventLangEnglishLang,
    "events/lang/german/lang": EventLangGermanLang,
    "events/lang/spanish/lang": EventLangSpanishLang,
    "events/meta": EventMeta,
    "festivals/lang/english/lang": FestivalLangEnglishLang,
    "festivals/lang/german/lang": FestivalLangGermanLang,
    "festivals/lang/spanish/lang": FestivalLangSpanishLang,
    "festivals/meta": FestivalMeta,
    "furniture/lang/english/lang": FurnitureLangEnglishLang,
    "furniture/lang/german/lang": FurnitureLangGermanLang,
    "furniture/lang/spanish/lang": FurnitureLangSpanishLang,
    "furniture/meta": FurnitureMeta,
    "herbs/meta": HerbMeta,
    "items/accessories/meta": ItemAccessoryMeta,
    "items/lang/english/lang": ItemLangEnglishLang,
    "items/lang/german/lang": ItemLangGermanLang,
    "items/lang/spanish/lang": ItemLangSpanishLang,
    "items/meta": ItemMeta,
    "items/recipes/meta": ItemRecipeMeta,
    "languages/lang": LanguageLang,
    "mail/lang/english/lang": MailLangEnglishLang,
    "mail/lang/german/lang": MailLangGermanLang,
    "mail/lang/spanish/lang": MailLangSpanishLang,
    "mail/meta": MailMeta,
    "map/lang/english/lang": MapLangEnglishLang,
    "map/lang/german/lang": MapLangGermanLang,
    "map/lang/spanish/lang": MapLangSpanishLang,
    "map/meta": MapMeta,
    "map/region": MapRegion,
    "music/packs/meta": MusicPackMeta,
    "npcs/lang/english/lang": NpcLangEnglishLang,
    "npcs/lang/german/lang": NpcLangGermanLang,
    "npcs/lang/spanish/lang": NpcLangSpanishLang,
    "npcs/meta": NpcMeta,
    "npcs/shops/meta": NpcShopMeta,
    "rival_marriages/meta": RivalMarriageMeta,
    "tasks/lang/english/lang": TaskLangEnglishLang,
    "tasks/lang/german/lang": TaskLangGermanLang,
    "tasks/lang/spanish/lang": TaskLangSpanishLang,
    "tasks/meta": TaskMeta,
    "time/meta": TimeMeta,
    "wedding_venues/lang/english/lang": WeddingVenueLangEnglishLang,
    "wedding_venues/lang/german/lang": WeddingVenueLangGermanLang,
    "wedding_venues/lang/spanish/lang": WeddingVenueLangSpanishLang,
    "wedding_venues/meta": WeddingVenueMeta,
    "world_objects/lang/english/lang": WorldObjectLangEnglishLang,
    "world_objects/lang/german/lang": WorldObjectLangGermanLang,
    "world_objects/lang/spanish/lang": WorldObjectLangSpanishLang,
    "world_objects/meta": WorldObjectMeta,
}

COLLECTION_REL_PATH_TO_VARIABLE_MAPPING = {
    "buildings/lang/english/lang": "buildings_lang_english_lang",
    "buildings/lang/german/lang": "buildings_lang_german_lang",
    "buildings/lang/spanish/lang": "buildings_lang_spanish_lang",
    "buildings/meta": "buildings_meta",
    "bundles/meta": "bundles_meta",
    "colony_layouts/lang/english/lang": "colony_layouts_lang_english_lang",
    "colony_layouts/lang/german/lang": "colony_layouts_lang_german_lang",
    "colony_layouts/lang/spanish/lang": "colony_layouts_lang_spanish_lang",
    "colony_layouts/meta": "colony_layouts_meta",
    "crafting_stations/meta": "crafting_stations_meta",
    "events/lang/english/lang": "events_lang_english_lang",
    "events/lang/german/lang": "events_lang_german_lang",
    "events/lang/spanish/lang": "events_lang_spanish_lang",
    "events/meta": "events_meta",
    "festivals/lang/english/lang": "festivals_lang_english_lang",
    "festivals/lang/german/lang": "festivals_lang_german_lang",
    "festivals/lang/spanish/lang": "festivals_lang_spanish_lang",
    "festivals/meta": "festivals_meta",
    "furniture/lang/english/lang": "furniture_lang_english_lang",
    "furniture/lang/german/lang": "furniture_lang_german_lang",
    "furniture/lang/spanish/lang": "furniture_lang_spanish_lang",
    "furniture/meta": "furniture_meta",
    "herbs/meta": "herbs_meta",
    "items/accessories/meta": "items_accessories_meta",
    "items/lang/english/lang": "items_lang_english_lang",
    "items/lang/german/lang": "items_lang_german_lang",
    "items/lang/spanish/lang": "items_lang_spanish_lang",
    "items/meta": "items_meta",
    "items/recipes/meta": "items_recipes_meta",
    "languages/lang": "languages_lang",
    "mail/lang/english/lang": "mail_lang_english_lang",
    "mail/lang/german/lang": "mail_lang_german_lang",
    "mail/lang/spanish/lang": "mail_lang_spanish_lang",
    "mail/meta": "mail_meta",
    "map/lang/english/lang": "map_lang_english_lang",
    "map/lang/german/lang": "map_lang_german_lang",
    "map/lang/spanish/lang": "map_lang_spanish_lang",
    "map/meta": "map_meta",
    "map/region": "map_region",
    "music/packs/meta": "music_packs_meta",
    "npcs/lang/english/lang": "npcs_lang_english_lang",
    "npcs/lang/german/lang": "npcs_lang_german_lang",
    "npcs/lang/spanish/lang": "npcs_lang_spanish_lang",
    "npcs/meta": "npcs_meta",
    "npcs/shops/meta": "npcs_shops_meta",
    "rival_marriages/meta": "rival_marriages_meta",
    "tasks/lang/english/lang": "tasks_lang_english_lang",
    "tasks/lang/german/lang": "tasks_lang_german_lang",
    "tasks/lang/spanish/lang": "tasks_lang_spanish_lang",
    "tasks/meta": "tasks_meta",
    "time/meta": "time_meta",
    "wedding_venues/lang/english/lang": "wedding_venues_lang_english_lang",
    "wedding_venues/lang/german/lang": "wedding_venues_lang_german_lang",
    "wedding_venues/lang/spanish/lang": "wedding_venues_lang_spanish_lang",
    "wedding_venues/meta": "wedding_venues_meta",
    "world_objects/lang/english/lang": "world_objects_lang_english_lang",
    "world_objects/lang/german/lang": "world_objects_lang_german_lang",
    "world_objects/lang/spanish/lang": "world_objects_lang_spanish_lang",
    "world_objects/meta": "world_objects_meta",
}


@dataclasses.dataclass
class AllResourceData:
    """All resource data indexed by file stem."""

    buildings_lang_english_lang: dict[str, BuildingLangEnglishLang] = None
    buildings_lang_german_lang: dict[str, BuildingLangGermanLang] = None
    buildings_lang_spanish_lang: dict[str, BuildingLangSpanishLang] = None
    buildings_meta: dict[str, BuildingMeta] = None
    bundles_meta: dict[str, BundleMeta] = None
    colony_layouts_lang_english_lang: dict[str, ColonyLayoutLangEnglishLang] = None
    colony_layouts_lang_german_lang: dict[str, ColonyLayoutLangGermanLang] = None
    colony_layouts_lang_spanish_lang: dict[str, ColonyLayoutLangSpanishLang] = None
    colony_layouts_meta: dict[str, ColonyLayoutMeta] = None
    crafting_stations_meta: dict[str, CraftingStationMeta] = None
    events_lang_english_lang: dict[str, EventLangEnglishLang] = None
    events_lang_german_lang: dict[str, EventLangGermanLang] = None
    events_lang_spanish_lang: dict[str, EventLangSpanishLang] = None
    events_meta: dict[str, EventMeta] = None
    festivals_lang_english_lang: dict[str, FestivalLangEnglishLang] = None
    festivals_lang_german_lang: dict[str, FestivalLangGermanLang] = None
    festivals_lang_spanish_lang: dict[str, FestivalLangSpanishLang] = None
    festivals_meta: dict[str, FestivalMeta] = None
    furniture_lang_english_lang: dict[str, FurnitureLangEnglishLang] = None
    furniture_lang_german_lang: dict[str, FurnitureLangGermanLang] = None
    furniture_lang_spanish_lang: dict[str, FurnitureLangSpanishLang] = None
    furniture_meta: dict[str, FurnitureMeta] = None
    herbs_meta: dict[str, HerbMeta] = None
    items_accessories_meta: dict[str, ItemAccessoryMeta] = None
    items_lang_english_lang: dict[str, ItemLangEnglishLang] = None
    items_lang_german_lang: dict[str, ItemLangGermanLang] = None
    items_lang_spanish_lang: dict[str, ItemLangSpanishLang] = None
    items_meta: dict[str, ItemMeta] = None
    items_recipes_meta: dict[str, ItemRecipeMeta] = None
    languages_lang: dict[str, LanguageLang] = None
    mail_lang_english_lang: dict[str, MailLangEnglishLang] = None
    mail_lang_german_lang: dict[str, MailLangGermanLang] = None
    mail_lang_spanish_lang: dict[str, MailLangSpanishLang] = None
    mail_meta: dict[str, MailMeta] = None
    map_lang_english_lang: dict[str, MapLangEnglishLang] = None
    map_lang_german_lang: dict[str, MapLangGermanLang] = None
    map_lang_spanish_lang: dict[str, MapLangSpanishLang] = None
    map_meta: dict[str, MapMeta] = None
    map_region: dict[str, MapRegion] = None
    music_packs_meta: dict[str, MusicPackMeta] = None
    npcs_lang_english_lang: dict[str, NpcLangEnglishLang] = None
    npcs_lang_german_lang: dict[str, NpcLangGermanLang] = None
    npcs_lang_spanish_lang: dict[str, NpcLangSpanishLang] = None
    npcs_meta: dict[str, NpcMeta] = None
    npcs_shops_meta: dict[str, NpcShopMeta] = None
    rival_marriages_meta: dict[str, RivalMarriageMeta] = None
    tasks_lang_english_lang: dict[str, TaskLangEnglishLang] = None
    tasks_lang_german_lang: dict[str, TaskLangGermanLang] = None
    tasks_lang_spanish_lang: dict[str, TaskLangSpanishLang] = None
    tasks_meta: dict[str, TaskMeta] = None
    time_meta: dict[str, TimeMeta] = None
    wedding_venues_lang_english_lang: dict[str, WeddingVenueLangEnglishLang] = None
    wedding_venues_lang_german_lang: dict[str, WeddingVenueLangGermanLang] = None
    wedding_venues_lang_spanish_lang: dict[str, WeddingVenueLangSpanishLang] = None
    wedding_venues_meta: dict[str, WeddingVenueMeta] = None
    world_objects_lang_english_lang: dict[str, WorldObjectLangEnglishLang] = None
    world_objects_lang_german_lang: dict[str, WorldObjectLangGermanLang] = None
    world_objects_lang_spanish_lang: dict[str, WorldObjectLangSpanishLang] = None
    world_objects_meta: dict[str, WorldObjectMeta] = None
