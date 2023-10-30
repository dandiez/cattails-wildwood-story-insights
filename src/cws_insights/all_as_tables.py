import os
from dataclasses import asdict

import pandas as pd

from cws_insights.common import CI_CD_GAMERESOURCES_DIR, SITE_SRC_DIR
from cws_insights.read_files import read_all_resource_files


def main(gameresources_dir, site_src_dir):
    """Dump the raw data into csv tables."""

    extensions_to_consider = (".meta", ".lang")
    all_raw_files = read_all_resource_files(
        gameresources_dir, file_suffixes=extensions_to_consider
    )
    links = []
    for rel_path, data in all_raw_files.items():
        file_name = rel_path.replace("/", "_") + ".csv"
        file_path = os.path.join(site_src_dir, "tables", file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df = pd.DataFrame(
            [
                {
                    **{"file": d.stem, "extension": d.extension, "path": d.rel_path},
                    **d.contents,
                }
                for d in data
            ]
        )
        df.to_csv(file_path, index=False)
        links.append(f"[{file_name}](tables/{file_name})")
    with open(os.path.join(site_src_dir, "raw_tables.md"), "w") as f:
        f.write("\n\n".join(links))


if __name__ == "__main__":
    gameresources_dir = CI_CD_GAMERESOURCES_DIR
    site_src_dir = SITE_SRC_DIR
    main(gameresources_dir, site_src_dir)
