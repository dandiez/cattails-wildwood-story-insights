import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ItemLangSpanishLang:
    item_uid_do_not_translate: str
    lang_item_definite_article: str
    lang_item_demonstrative_article: str
    lang_item_description: str
    lang_item_indefinite_article: str
    lang_item_name: str
