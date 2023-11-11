import os.path
import sys
from os import listdir
from os.path import isfile, join
from pathlib import Path

from PIL import Image
from pywikibot.specialbots import UploadRobot

THIS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", "..", ".."))
sys.path.insert(0, SRC_DIR)
from cws_insights.common import CI_CD_GAMERESOURCES_DIR, WIKI_CONTENTS_DIR, MORE_RESOURCES_PATH


def main():
    items_sprites_dir = os.path.join(CI_CD_GAMERESOURCES_DIR, "items", "sprites")
    output_dir = os.path.join(WIKI_CONTENTS_DIR, "sprites_bigger")
    os.makedirs(output_dir, exist_ok=True)
    make_sprites_bigger(items_sprites_dir, output_dir, factor=3)
    make_sprites_bigger(MORE_RESOURCES_PATH, output_dir, factor=2)


def make_sprites_bigger(items_sprites_dir: str, output_dir: str, factor=3):
    onlyfiles = [
        f for f in listdir(items_sprites_dir) if isfile(join(items_sprites_dir, f))
    ]
    only_pngs = [f for f in onlyfiles if Path(f).suffix == ".png"]
    for f in only_pngs:
        full_source_file_path = join(items_sprites_dir, f)
        image = Image.open(full_source_file_path)
        image = image.crop(image.getbbox())
        width, height = image.size
        new_size = (width*factor, height*factor)
        image = image.resize(new_size, resample=Image.BICUBIC)
        image.save(os.path.join(output_dir, f))



if __name__ == "__main__":
    main()
