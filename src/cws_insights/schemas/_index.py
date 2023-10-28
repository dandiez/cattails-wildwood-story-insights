import dataclasses

from cws_insights.schemas.buildings import Building
from cws_insights.schemas.buildings_lang_english import BuildingLangEnglish
from cws_insights.schemas.buildings_lang_german import BuildingLangGerman
from cws_insights.schemas.buildings_lang_spanish import BuildingLangSpanish
from cws_insights.schemas.bundles import Bundle
from cws_insights.schemas.colony_layouts import ColonyLayout
from cws_insights.schemas.colony_layouts_lang_english import ColonyLayoutLangEnglish
from cws_insights.schemas.colony_layouts_lang_german import ColonyLayoutLangGerman
from cws_insights.schemas.colony_layouts_lang_spanish import ColonyLayoutLangSpanish
from cws_insights.schemas.crafting_stations import CraftingStation
from cws_insights.schemas.events import Event
from cws_insights.schemas.events_lang_english import EventLangEnglish
from cws_insights.schemas.events_lang_german import EventLangGerman
from cws_insights.schemas.events_lang_spanish import EventLangSpanish
from cws_insights.schemas.festivals import Festival
from cws_insights.schemas.festivals_lang_english import FestivalLangEnglish
from cws_insights.schemas.festivals_lang_german import FestivalLangGerman
from cws_insights.schemas.festivals_lang_spanish import FestivalLangSpanish
from cws_insights.schemas.furniture import Furniture
from cws_insights.schemas.furniture_lang_english import FurnitureLangEnglish
from cws_insights.schemas.furniture_lang_german import FurnitureLangGerman
from cws_insights.schemas.furniture_lang_spanish import FurnitureLangSpanish
from cws_insights.schemas.herbs import Herb
from cws_insights.schemas.items import Item
from cws_insights.schemas.items_accessories import ItemAccessory
from cws_insights.schemas.items_lang_english import ItemLangEnglish
from cws_insights.schemas.items_lang_german import ItemLangGerman
from cws_insights.schemas.items_lang_spanish import ItemLangSpanish
from cws_insights.schemas.items_recipes import ItemRecipe
from cws_insights.schemas.languages import Language
from cws_insights.schemas.mail import Mail
from cws_insights.schemas.mail_lang_english import MailLangEnglish
from cws_insights.schemas.mail_lang_german import MailLangGerman
from cws_insights.schemas.mail_lang_spanish import MailLangSpanish
from cws_insights.schemas.map import Map
from cws_insights.schemas.map_lang_english import MapLangEnglish
from cws_insights.schemas.map_lang_german import MapLangGerman
from cws_insights.schemas.map_lang_spanish import MapLangSpanish
from cws_insights.schemas.music_packs import MusicPack
from cws_insights.schemas.npcs import Npc
from cws_insights.schemas.npcs_lang_english import NpcLangEnglish
from cws_insights.schemas.npcs_lang_german import NpcLangGerman
from cws_insights.schemas.npcs_lang_spanish import NpcLangSpanish
from cws_insights.schemas.npcs_shops import NpcShop
from cws_insights.schemas.rival_marriages import RivalMarriage
from cws_insights.schemas.tasks import Task
from cws_insights.schemas.tasks_lang_english import TaskLangEnglish
from cws_insights.schemas.tasks_lang_german import TaskLangGerman
from cws_insights.schemas.tasks_lang_spanish import TaskLangSpanish
from cws_insights.schemas.time import Time
from cws_insights.schemas.wedding_venues import WeddingVenue
from cws_insights.schemas.wedding_venues_lang_english import WeddingVenueLangEnglish
from cws_insights.schemas.wedding_venues_lang_german import WeddingVenueLangGerman
from cws_insights.schemas.wedding_venues_lang_spanish import WeddingVenueLangSpanish
from cws_insights.schemas.world_objects import WorldObject
from cws_insights.schemas.world_objects_lang_english import WorldObjectLangEnglish
from cws_insights.schemas.world_objects_lang_german import WorldObjectLangGerman
from cws_insights.schemas.world_objects_lang_spanish import WorldObjectLangSpanish

COLLECTION_REL_PATH_TO_DATACLASS_MAPPING = {
    "buildings": Building,
    "buildings/lang/english": BuildingLangEnglish,
    "buildings/lang/german": BuildingLangGerman,
    "buildings/lang/spanish": BuildingLangSpanish,
    "bundles": Bundle,
    "colony_layouts": ColonyLayout,
    "colony_layouts/lang/english": ColonyLayoutLangEnglish,
    "colony_layouts/lang/german": ColonyLayoutLangGerman,
    "colony_layouts/lang/spanish": ColonyLayoutLangSpanish,
    "crafting_stations": CraftingStation,
    "events": Event,
    "events/lang/english": EventLangEnglish,
    "events/lang/german": EventLangGerman,
    "events/lang/spanish": EventLangSpanish,
    "festivals": Festival,
    "festivals/lang/english": FestivalLangEnglish,
    "festivals/lang/german": FestivalLangGerman,
    "festivals/lang/spanish": FestivalLangSpanish,
    "furniture": Furniture,
    "furniture/lang/english": FurnitureLangEnglish,
    "furniture/lang/german": FurnitureLangGerman,
    "furniture/lang/spanish": FurnitureLangSpanish,
    "herbs": Herb,
    "items": Item,
    "items/accessories": ItemAccessory,
    "items/lang/english": ItemLangEnglish,
    "items/lang/german": ItemLangGerman,
    "items/lang/spanish": ItemLangSpanish,
    "items/recipes": ItemRecipe,
    "languages": Language,
    "mail": Mail,
    "mail/lang/english": MailLangEnglish,
    "mail/lang/german": MailLangGerman,
    "mail/lang/spanish": MailLangSpanish,
    "map": Map,
    "map/lang/english": MapLangEnglish,
    "map/lang/german": MapLangGerman,
    "map/lang/spanish": MapLangSpanish,
    "music/packs": MusicPack,
    "npcs": Npc,
    "npcs/lang/english": NpcLangEnglish,
    "npcs/lang/german": NpcLangGerman,
    "npcs/lang/spanish": NpcLangSpanish,
    "npcs/shops": NpcShop,
    "rival_marriages": RivalMarriage,
    "tasks": Task,
    "tasks/lang/english": TaskLangEnglish,
    "tasks/lang/german": TaskLangGerman,
    "tasks/lang/spanish": TaskLangSpanish,
    "time": Time,
    "wedding_venues": WeddingVenue,
    "wedding_venues/lang/english": WeddingVenueLangEnglish,
    "wedding_venues/lang/german": WeddingVenueLangGerman,
    "wedding_venues/lang/spanish": WeddingVenueLangSpanish,
    "world_objects": WorldObject,
    "world_objects/lang/english": WorldObjectLangEnglish,
    "world_objects/lang/german": WorldObjectLangGerman,
    "world_objects/lang/spanish": WorldObjectLangSpanish,
}

COLLECTION_REL_PATH_TO_VARIABLE_MAPPING = {
    "buildings": "buildings",
    "buildings/lang/english": "buildings_lang_english",
    "buildings/lang/german": "buildings_lang_german",
    "buildings/lang/spanish": "buildings_lang_spanish",
    "bundles": "bundles",
    "colony_layouts": "colony_layouts",
    "colony_layouts/lang/english": "colony_layouts_lang_english",
    "colony_layouts/lang/german": "colony_layouts_lang_german",
    "colony_layouts/lang/spanish": "colony_layouts_lang_spanish",
    "crafting_stations": "crafting_stations",
    "events": "events",
    "events/lang/english": "events_lang_english",
    "events/lang/german": "events_lang_german",
    "events/lang/spanish": "events_lang_spanish",
    "festivals": "festivals",
    "festivals/lang/english": "festivals_lang_english",
    "festivals/lang/german": "festivals_lang_german",
    "festivals/lang/spanish": "festivals_lang_spanish",
    "furniture": "furniture",
    "furniture/lang/english": "furniture_lang_english",
    "furniture/lang/german": "furniture_lang_german",
    "furniture/lang/spanish": "furniture_lang_spanish",
    "herbs": "herbs",
    "items": "items",
    "items/accessories": "items_accessories",
    "items/lang/english": "items_lang_english",
    "items/lang/german": "items_lang_german",
    "items/lang/spanish": "items_lang_spanish",
    "items/recipes": "items_recipes",
    "languages": "languages",
    "mail": "mail",
    "mail/lang/english": "mail_lang_english",
    "mail/lang/german": "mail_lang_german",
    "mail/lang/spanish": "mail_lang_spanish",
    "map": "map",
    "map/lang/english": "map_lang_english",
    "map/lang/german": "map_lang_german",
    "map/lang/spanish": "map_lang_spanish",
    "music/packs": "music_packs",
    "npcs": "npcs",
    "npcs/lang/english": "npcs_lang_english",
    "npcs/lang/german": "npcs_lang_german",
    "npcs/lang/spanish": "npcs_lang_spanish",
    "npcs/shops": "npcs_shops",
    "rival_marriages": "rival_marriages",
    "tasks": "tasks",
    "tasks/lang/english": "tasks_lang_english",
    "tasks/lang/german": "tasks_lang_german",
    "tasks/lang/spanish": "tasks_lang_spanish",
    "time": "time",
    "wedding_venues": "wedding_venues",
    "wedding_venues/lang/english": "wedding_venues_lang_english",
    "wedding_venues/lang/german": "wedding_venues_lang_german",
    "wedding_venues/lang/spanish": "wedding_venues_lang_spanish",
    "world_objects": "world_objects",
    "world_objects/lang/english": "world_objects_lang_english",
    "world_objects/lang/german": "world_objects_lang_german",
    "world_objects/lang/spanish": "world_objects_lang_spanish",
}


@dataclasses.dataclass
class AllResourceData:
    """All resource data indexed by file stem."""

    buildings: dict[str, Building] = None
    buildings_lang_english: dict[str, BuildingLangEnglish] = None
    buildings_lang_german: dict[str, BuildingLangGerman] = None
    buildings_lang_spanish: dict[str, BuildingLangSpanish] = None
    bundles: dict[str, Bundle] = None
    colony_layouts: dict[str, ColonyLayout] = None
    colony_layouts_lang_english: dict[str, ColonyLayoutLangEnglish] = None
    colony_layouts_lang_german: dict[str, ColonyLayoutLangGerman] = None
    colony_layouts_lang_spanish: dict[str, ColonyLayoutLangSpanish] = None
    crafting_stations: dict[str, CraftingStation] = None
    events: dict[str, Event] = None
    events_lang_english: dict[str, EventLangEnglish] = None
    events_lang_german: dict[str, EventLangGerman] = None
    events_lang_spanish: dict[str, EventLangSpanish] = None
    festivals: dict[str, Festival] = None
    festivals_lang_english: dict[str, FestivalLangEnglish] = None
    festivals_lang_german: dict[str, FestivalLangGerman] = None
    festivals_lang_spanish: dict[str, FestivalLangSpanish] = None
    furniture: dict[str, Furniture] = None
    furniture_lang_english: dict[str, FurnitureLangEnglish] = None
    furniture_lang_german: dict[str, FurnitureLangGerman] = None
    furniture_lang_spanish: dict[str, FurnitureLangSpanish] = None
    herbs: dict[str, Herb] = None
    items: dict[str, Item] = None
    items_accessories: dict[str, ItemAccessory] = None
    items_lang_english: dict[str, ItemLangEnglish] = None
    items_lang_german: dict[str, ItemLangGerman] = None
    items_lang_spanish: dict[str, ItemLangSpanish] = None
    items_recipes: dict[str, ItemRecipe] = None
    languages: dict[str, Language] = None
    mail: dict[str, Mail] = None
    mail_lang_english: dict[str, MailLangEnglish] = None
    mail_lang_german: dict[str, MailLangGerman] = None
    mail_lang_spanish: dict[str, MailLangSpanish] = None
    map: dict[str, Map] = None
    map_lang_english: dict[str, MapLangEnglish] = None
    map_lang_german: dict[str, MapLangGerman] = None
    map_lang_spanish: dict[str, MapLangSpanish] = None
    music_packs: dict[str, MusicPack] = None
    npcs: dict[str, Npc] = None
    npcs_lang_english: dict[str, NpcLangEnglish] = None
    npcs_lang_german: dict[str, NpcLangGerman] = None
    npcs_lang_spanish: dict[str, NpcLangSpanish] = None
    npcs_shops: dict[str, NpcShop] = None
    rival_marriages: dict[str, RivalMarriage] = None
    tasks: dict[str, Task] = None
    tasks_lang_english: dict[str, TaskLangEnglish] = None
    tasks_lang_german: dict[str, TaskLangGerman] = None
    tasks_lang_spanish: dict[str, TaskLangSpanish] = None
    time: dict[str, Time] = None
    wedding_venues: dict[str, WeddingVenue] = None
    wedding_venues_lang_english: dict[str, WeddingVenueLangEnglish] = None
    wedding_venues_lang_german: dict[str, WeddingVenueLangGerman] = None
    wedding_venues_lang_spanish: dict[str, WeddingVenueLangSpanish] = None
    world_objects: dict[str, WorldObject] = None
    world_objects_lang_english: dict[str, WorldObjectLangEnglish] = None
    world_objects_lang_german: dict[str, WorldObjectLangGerman] = None
    world_objects_lang_spanish: dict[str, WorldObjectLangSpanish] = None
