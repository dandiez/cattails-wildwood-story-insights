import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class ItemLangGerman:
    """Dataset associated with files in 'gameresources/items/lang/german'."""

    _special_mappings: ClassVar[dict] = {}
    item_uid_do_not_translate: str = Undefined
    lang_item_definite_article: str = Undefined
    lang_item_demonstrative_article: str = Undefined
    lang_item_description: str = Undefined
    lang_item_indefinite_article: str = Undefined
    lang_item_name: str = Undefined
