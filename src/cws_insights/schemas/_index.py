import dataclasses

from cws_insights.schemas.buildings import Buildings
from cws_insights.schemas.buildings_lang_english import BuildingsLangEnglish
from cws_insights.schemas.buildings_lang_german import BuildingsLangGerman
from cws_insights.schemas.buildings_lang_spanish import BuildingsLangSpanish
from cws_insights.schemas.bundles import Bundles
from cws_insights.schemas.colony_layouts import ColonyLayouts
from cws_insights.schemas.colony_layouts_lang_english import ColonyLayoutsLangEnglish
from cws_insights.schemas.colony_layouts_lang_german import ColonyLayoutsLangGerman
from cws_insights.schemas.colony_layouts_lang_spanish import ColonyLayoutsLangSpanish
from cws_insights.schemas.crafting_stations import CraftingStations
from cws_insights.schemas.events import Events
from cws_insights.schemas.events_lang_english import EventsLangEnglish
from cws_insights.schemas.events_lang_german import EventsLangGerman
from cws_insights.schemas.events_lang_spanish import EventsLangSpanish
from cws_insights.schemas.festivals import Festivals
from cws_insights.schemas.festivals_lang_english import FestivalsLangEnglish
from cws_insights.schemas.festivals_lang_german import FestivalsLangGerman
from cws_insights.schemas.festivals_lang_spanish import FestivalsLangSpanish
from cws_insights.schemas.furniture import Furniture
from cws_insights.schemas.furniture_lang_english import FurnitureLangEnglish
from cws_insights.schemas.furniture_lang_german import FurnitureLangGerman
from cws_insights.schemas.furniture_lang_spanish import FurnitureLangSpanish
from cws_insights.schemas.herbs import Herbs
from cws_insights.schemas.items import Items
from cws_insights.schemas.items_accessories import ItemsAccessories
from cws_insights.schemas.items_lang_english import ItemsLangEnglish
from cws_insights.schemas.items_lang_german import ItemsLangGerman
from cws_insights.schemas.items_lang_spanish import ItemsLangSpanish
from cws_insights.schemas.items_recipes import ItemsRecipes
from cws_insights.schemas.languages import Languages
from cws_insights.schemas.mail import Mail
from cws_insights.schemas.mail_lang_english import MailLangEnglish
from cws_insights.schemas.mail_lang_german import MailLangGerman
from cws_insights.schemas.mail_lang_spanish import MailLangSpanish
from cws_insights.schemas.map import Map
from cws_insights.schemas.map_lang_english import MapLangEnglish
from cws_insights.schemas.map_lang_german import MapLangGerman
from cws_insights.schemas.map_lang_spanish import MapLangSpanish
from cws_insights.schemas.music_packs import MusicPacks
from cws_insights.schemas.npcs import Npcs
from cws_insights.schemas.npcs_lang_english import NpcsLangEnglish
from cws_insights.schemas.npcs_lang_german import NpcsLangGerman
from cws_insights.schemas.npcs_lang_spanish import NpcsLangSpanish
from cws_insights.schemas.npcs_shops import NpcsShops
from cws_insights.schemas.rival_marriages import RivalMarriages
from cws_insights.schemas.tasks import Tasks
from cws_insights.schemas.tasks_lang_english import TasksLangEnglish
from cws_insights.schemas.tasks_lang_german import TasksLangGerman
from cws_insights.schemas.tasks_lang_spanish import TasksLangSpanish
from cws_insights.schemas.time import Time
from cws_insights.schemas.wedding_venues import WeddingVenues
from cws_insights.schemas.wedding_venues_lang_english import WeddingVenuesLangEnglish
from cws_insights.schemas.wedding_venues_lang_german import WeddingVenuesLangGerman
from cws_insights.schemas.wedding_venues_lang_spanish import WeddingVenuesLangSpanish
from cws_insights.schemas.world_objects import WorldObjects
from cws_insights.schemas.world_objects_lang_english import WorldObjectsLangEnglish
from cws_insights.schemas.world_objects_lang_german import WorldObjectsLangGerman
from cws_insights.schemas.world_objects_lang_spanish import WorldObjectsLangSpanish

COLLECTION_REL_PATH_TO_DATACLASS_MAPPING = {
    "buildings": Buildings,
    "buildings/lang/english": BuildingsLangEnglish,
    "buildings/lang/german": BuildingsLangGerman,
    "buildings/lang/spanish": BuildingsLangSpanish,
    "bundles": Bundles,
    "colony_layouts": ColonyLayouts,
    "colony_layouts/lang/english": ColonyLayoutsLangEnglish,
    "colony_layouts/lang/german": ColonyLayoutsLangGerman,
    "colony_layouts/lang/spanish": ColonyLayoutsLangSpanish,
    "crafting_stations": CraftingStations,
    "events": Events,
    "events/lang/english": EventsLangEnglish,
    "events/lang/german": EventsLangGerman,
    "events/lang/spanish": EventsLangSpanish,
    "festivals": Festivals,
    "festivals/lang/english": FestivalsLangEnglish,
    "festivals/lang/german": FestivalsLangGerman,
    "festivals/lang/spanish": FestivalsLangSpanish,
    "furniture": Furniture,
    "furniture/lang/english": FurnitureLangEnglish,
    "furniture/lang/german": FurnitureLangGerman,
    "furniture/lang/spanish": FurnitureLangSpanish,
    "herbs": Herbs,
    "items": Items,
    "items/accessories": ItemsAccessories,
    "items/lang/english": ItemsLangEnglish,
    "items/lang/german": ItemsLangGerman,
    "items/lang/spanish": ItemsLangSpanish,
    "items/recipes": ItemsRecipes,
    "languages": Languages,
    "mail": Mail,
    "mail/lang/english": MailLangEnglish,
    "mail/lang/german": MailLangGerman,
    "mail/lang/spanish": MailLangSpanish,
    "map": Map,
    "map/lang/english": MapLangEnglish,
    "map/lang/german": MapLangGerman,
    "map/lang/spanish": MapLangSpanish,
    "music/packs": MusicPacks,
    "npcs": Npcs,
    "npcs/lang/english": NpcsLangEnglish,
    "npcs/lang/german": NpcsLangGerman,
    "npcs/lang/spanish": NpcsLangSpanish,
    "npcs/shops": NpcsShops,
    "rival_marriages": RivalMarriages,
    "tasks": Tasks,
    "tasks/lang/english": TasksLangEnglish,
    "tasks/lang/german": TasksLangGerman,
    "tasks/lang/spanish": TasksLangSpanish,
    "time": Time,
    "wedding_venues": WeddingVenues,
    "wedding_venues/lang/english": WeddingVenuesLangEnglish,
    "wedding_venues/lang/german": WeddingVenuesLangGerman,
    "wedding_venues/lang/spanish": WeddingVenuesLangSpanish,
    "world_objects": WorldObjects,
    "world_objects/lang/english": WorldObjectsLangEnglish,
    "world_objects/lang/german": WorldObjectsLangGerman,
    "world_objects/lang/spanish": WorldObjectsLangSpanish,
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

    buildings: dict[str, Buildings]
    buildings_lang_english: dict[str, BuildingsLangEnglish]
    buildings_lang_german: dict[str, BuildingsLangGerman]
    buildings_lang_spanish: dict[str, BuildingsLangSpanish]
    bundles: dict[str, Bundles]
    colony_layouts: dict[str, ColonyLayouts]
    colony_layouts_lang_english: dict[str, ColonyLayoutsLangEnglish]
    colony_layouts_lang_german: dict[str, ColonyLayoutsLangGerman]
    colony_layouts_lang_spanish: dict[str, ColonyLayoutsLangSpanish]
    crafting_stations: dict[str, CraftingStations]
    events: dict[str, Events]
    events_lang_english: dict[str, EventsLangEnglish]
    events_lang_german: dict[str, EventsLangGerman]
    events_lang_spanish: dict[str, EventsLangSpanish]
    festivals: dict[str, Festivals]
    festivals_lang_english: dict[str, FestivalsLangEnglish]
    festivals_lang_german: dict[str, FestivalsLangGerman]
    festivals_lang_spanish: dict[str, FestivalsLangSpanish]
    furniture: dict[str, Furniture]
    furniture_lang_english: dict[str, FurnitureLangEnglish]
    furniture_lang_german: dict[str, FurnitureLangGerman]
    furniture_lang_spanish: dict[str, FurnitureLangSpanish]
    herbs: dict[str, Herbs]
    items: dict[str, Items]
    items_accessories: dict[str, ItemsAccessories]
    items_lang_english: dict[str, ItemsLangEnglish]
    items_lang_german: dict[str, ItemsLangGerman]
    items_lang_spanish: dict[str, ItemsLangSpanish]
    items_recipes: dict[str, ItemsRecipes]
    languages: dict[str, Languages]
    mail: dict[str, Mail]
    mail_lang_english: dict[str, MailLangEnglish]
    mail_lang_german: dict[str, MailLangGerman]
    mail_lang_spanish: dict[str, MailLangSpanish]
    map: dict[str, Map]
    map_lang_english: dict[str, MapLangEnglish]
    map_lang_german: dict[str, MapLangGerman]
    map_lang_spanish: dict[str, MapLangSpanish]
    music_packs: dict[str, MusicPacks]
    npcs: dict[str, Npcs]
    npcs_lang_english: dict[str, NpcsLangEnglish]
    npcs_lang_german: dict[str, NpcsLangGerman]
    npcs_lang_spanish: dict[str, NpcsLangSpanish]
    npcs_shops: dict[str, NpcsShops]
    rival_marriages: dict[str, RivalMarriages]
    tasks: dict[str, Tasks]
    tasks_lang_english: dict[str, TasksLangEnglish]
    tasks_lang_german: dict[str, TasksLangGerman]
    tasks_lang_spanish: dict[str, TasksLangSpanish]
    time: dict[str, Time]
    wedding_venues: dict[str, WeddingVenues]
    wedding_venues_lang_english: dict[str, WeddingVenuesLangEnglish]
    wedding_venues_lang_german: dict[str, WeddingVenuesLangGerman]
    wedding_venues_lang_spanish: dict[str, WeddingVenuesLangSpanish]
    world_objects: dict[str, WorldObjects]
    world_objects_lang_english: dict[str, WorldObjectsLangEnglish]
    world_objects_lang_german: dict[str, WorldObjectsLangGerman]
    world_objects_lang_spanish: dict[str, WorldObjectsLangSpanish]
