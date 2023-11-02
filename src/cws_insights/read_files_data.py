from cws_insights.read_files import AllResourceFiles
from cws_insights.schemas._index import (
    AllResourceData,
    COLLECTION_REL_PATH_TO_VARIABLE_MAPPING,
    COLLECTION_REL_PATH_TO_DATACLASS_MAPPING,
)


def instantiate_all_resource_data(
    all_resource_files: AllResourceFiles,
) -> AllResourceData:
    all_data = AllResourceData()
    for rel_path, files in all_resource_files.items():
        attribute = COLLECTION_REL_PATH_TO_VARIABLE_MAPPING[rel_path]
        class_type = COLLECTION_REL_PATH_TO_DATACLASS_MAPPING[rel_path]
        setattr(
            all_data,
            attribute,
            {f.stem: class_type.from_dict(f.contents) for f in files},
        )
    return all_data
