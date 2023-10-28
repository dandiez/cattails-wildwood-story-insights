import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class MailLangSpanish:
    """Dataset associated with files in 'gameresources/mail/lang/spanish'."""

    _special_mappings: ClassVar[dict] = {}
    lang_mail_content_body: str = Undefined
    lang_mail_content_header: str = Undefined
    lang_mail_content_signature: str = Undefined
    lang_mail_subject: str = Undefined
