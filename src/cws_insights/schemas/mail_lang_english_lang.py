import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class MailLangEnglishLang:
    lang_mail_content_body: str
    lang_mail_content_header: str
    lang_mail_content_signature: str
    lang_mail_subject: str
