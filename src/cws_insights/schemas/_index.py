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
