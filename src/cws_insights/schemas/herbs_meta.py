import dataclasses
import dataclasses_json


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class HerbMeta:
    autumn: list[str] = dataclasses.field(default_factory=list)
    bush_herbs: list[str] = dataclasses.field(default_factory=list)
    night_herbs: list[str] = dataclasses.field(default_factory=list)
    ranked_herbs: list[str] = dataclasses.field(default_factory=list)
    spring: list[str] = dataclasses.field(default_factory=list)
    summer: list[str] = dataclasses.field(default_factory=list)
    winter: list[str] = dataclasses.field(default_factory=list)
