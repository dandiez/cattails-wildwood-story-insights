import dataclasses
from pathlib import Path


@dataclasses.dataclass
class Units:
    """Way to write different units."""

    mews: str
    mole_cash: str
    task_token: str
    festival_token: str
    prey: str
    herb: str
    treasure: str
    wood: str
    stone: str
    sand: str

    def from_shop_currency_type(self, currency_type: str):
        match currency_type:
            case "mews":
                return self.mews
            case "festival tokens":
                return self.festival_token
            case "task tokens":
                return self.task_token
            case "mole cash":
                return self.mole_cash


UNITS_FANDOM = Units(
    mews="{{WSMew}}",
    mole_cash="{{WSMolecash}}",
    task_token="{{WSTasktoken}}",
    festival_token="{{WSFesttoken}}",
    prey="{{Stpile|Prey}}",
    herb="{{Stpile|Herb}}",
    treasure="{{Stpile|Treasure}}",
    wood="{{Stpile|Wood}}",
    stone="{{Stpile|Stone}}",
    sand="{{Stpile|Sand}}",
)


NPC_PAGE_LINK_NEEDS_ATTACHMENT = {
    "Coco",
    "Elli",
    "Ember",
    "Forest Guardian",
    "Jag",
    "Krampy",
}


def get_npc_page_link(npc_uid: str):
    if npc_uid in NPC_PAGE_LINK_NEEDS_ATTACHMENT:
        page = f"{npc_uid}/Wildwood Story|{npc_uid}"
    else:
        page = npc_uid
    return f"[[{page}]]"


def get_region_locations_file_name_from_image_name(image_png: str):
    return Path(image_png).stem + "_locations.png"
