import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MailMeta_MailFilters:
    filter_autumn: bool = None
    filter_birthday_champ: bool = None
    filter_curios: int = None
    filter_dating_alabaster: int = None
    filter_dating_fliss: int = None
    filter_dating_spark: int = None
    filter_day: int = None
    filter_friendship_alabaster: int = None
    filter_friendship_bob: int = None
    filter_friendship_buttercup: int = None
    filter_friendship_champ: int = None
    filter_friendship_charlotte: int = None
    filter_friendship_coco: int = None
    filter_friendship_elli: int = None
    filter_friendship_ember: int = None
    filter_friendship_fliss: int = None
    filter_friendship_garlic: int = None
    filter_friendship_glimmer: int = None
    filter_friendship_jag: int = None
    filter_friendship_krampy: int = None
    filter_friendship_lainey: int = None
    filter_friendship_max_champ: int = None
    filter_friendship_max_charlotte: int = None
    filter_friendship_phantom: int = None
    filter_friendship_rosemary: int = None
    filter_friendship_spark: int = None
    filter_friendship_talon: int = None
    filter_friendship_zephyr: int = None
    filter_has_changed_name: bool = None
    filter_has_kittens: bool = None
    filter_has_met_alabaster: bool = None
    filter_has_met_bob: bool = None
    filter_has_met_buttercup: bool = None
    filter_has_met_champ: bool = None
    filter_has_met_charlotte: bool = None
    filter_has_met_coco: bool = None
    filter_has_met_elli: bool = None
    filter_has_met_ember: bool = None
    filter_has_met_fliss: bool = None
    filter_has_met_garlic: bool = None
    filter_has_met_glimmer: bool = None
    filter_has_met_jag: bool = None
    filter_has_met_krampy: bool = None
    filter_has_met_lainey: bool = None
    filter_has_met_phantom: bool = None
    filter_has_met_rosemary: bool = None
    filter_has_met_spark: bool = None
    filter_has_met_talon: bool = None
    filter_has_met_zephyr: bool = None
    filter_has_used_healing_services: bool = None
    filter_kitten_age: int = None
    filter_kitten_age_max: int = None
    filter_mine_level: int = None
    filter_player_birthday: bool = None
    filter_player_is_dating: bool = None
    filter_player_is_dating_buttercup: bool = None
    filter_player_is_dating_champ: bool = None
    filter_player_is_dating_coco: bool = None
    filter_player_is_dating_elli: bool = None
    filter_player_is_dating_ember: bool = None
    filter_player_is_dating_glimmer: bool = None
    filter_player_is_dating_jag: bool = None
    filter_player_is_dating_krampy: bool = None
    filter_player_is_dating_lainey: bool = None
    filter_player_is_dating_phantom: bool = None
    filter_player_is_dating_spark: bool = None
    filter_player_is_dating_talon: bool = None
    filter_player_is_dating_zephyr: bool = None
    filter_player_is_married: bool = None
    filter_player_is_married_to_alabaster: bool = None
    filter_player_is_married_to_bob: bool = None
    filter_player_is_married_to_buttercup: bool = None
    filter_player_is_married_to_champ: bool = None
    filter_player_is_married_to_charlotte: bool = None
    filter_player_is_married_to_coco: bool = None
    filter_player_is_married_to_elli: bool = None
    filter_player_is_married_to_ember: bool = None
    filter_player_is_married_to_fliss: bool = None
    filter_player_is_married_to_garlic: bool = None
    filter_player_is_married_to_glimmer: bool = None
    filter_player_is_married_to_jag: bool = None
    filter_player_is_married_to_krampy: bool = None
    filter_player_is_married_to_phantom: bool = None
    filter_player_is_married_to_rosemary: bool = None
    filter_player_is_married_to_spark: bool = None
    filter_player_is_married_to_talon: bool = None
    filter_player_is_married_to_zephyr: bool = None
    filter_player_recently_married: bool = None
    filter_rival_marriage_completed_alabasterandfliss: bool = None
    filter_rival_marriage_completed_bobandbuttercup: bool = None
    filter_rival_marriage_completed_elliandchamp: bool = None
    filter_rival_marriage_completed_krampyandtalon: bool = None
    filter_rival_marriage_completed_sparkandlainey: bool = None
    filter_season_day: int = None
    filter_season_day_max: int = None
    filter_spring: bool = None
    filter_summer: bool = None
    filter_wc_fate: int = None
    filter_winter: bool = None
    filter_year: int = None
    filter_year_max: int = None


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MailMeta:
    attachment: str
    attachment_quantity: int
    enabled: bool
    mail_filters: MailMeta_MailFilters
    paper_type: str
