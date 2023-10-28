import dataclasses
from typing import ClassVar

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Mail:
    """Dataset associated with files in 'gameresources/mail'."""

    _special_mappings: ClassVar[dict] = {}
    attachment: str = Undefined
    attachment_quantity: int = Undefined
    enabled: bool = Undefined
    mail_filters: dict = Undefined
    paper_type: str = Undefined
