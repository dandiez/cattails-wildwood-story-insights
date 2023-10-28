import dataclasses

from cws_insights.definitions import Undefined


@dataclasses.dataclass
class Mail:
    """Dataset associated with files in 'gameresources/mail'."""

    attachment: str = Undefined
    attachment_quantity: int = Undefined
    enabled: bool = Undefined
    mail_filters: dict = Undefined
    paper_type: str = Undefined
