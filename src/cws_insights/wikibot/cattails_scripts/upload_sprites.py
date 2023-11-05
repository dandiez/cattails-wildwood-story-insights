import os.path
import sys
from os import listdir
from os.path import isfile, join
from pathlib import Path

from pywikibot.specialbots import UploadRobot

THIS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", "..", ".."))
sys.path.insert(0, SRC_DIR)
from cws_insights.common import CI_CD_GAMERESOURCES_DIR


def main():
    items_sprites_dir = os.path.join(CI_CD_GAMERESOURCES_DIR, "items", "sprites")
    onlyfiles = [
        f for f in listdir(items_sprites_dir) if isfile(join(items_sprites_dir, f))
    ]
    only_pngs = [f for f in onlyfiles if Path(f).suffix == ".png"]

    for f in only_pngs:
        stem = Path(f).stem
        full_source_file_path = join(items_sprites_dir, f)
        robot = UploadRobot(
            url=full_source_file_path,
            description=f"Cattails Wildwood Story sprite for uid={stem}",
            filename_prefix="ws_",
            ignore_warning=True,
            always=True,
        )
        robot.run()


if __name__ == "__main__":
    main()