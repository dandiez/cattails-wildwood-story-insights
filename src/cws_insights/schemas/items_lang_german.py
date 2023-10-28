import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemsLangGerman:
    """Dataset associated with files in 'gameresources/items/lang/german'."""

    item_uid_do_not_translate: str = Undefined
    lang_item_definite_article: str = Undefined
    lang_item_demonstrative_article: str = Undefined
    lang_item_description: str = Undefined
    lang_item_indefinite_article: str = Undefined
    lang_item_name: str = Undefined
