import contextlib
import dataclasses
import os.path

from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from PIL import ImageDraw

from cws_insights.common import (
    CI_CD_GAMERESOURCES_DIR,
    WIKI_CONTENTS_DIR,
    MORE_RESOURCES_PATH,
)
from cws_insights.merged_data.items import (
    get_merged_item_data,
    AllItemPlus,
    get_stem_from_uid,
)
from cws_insights.page_writers.items_fandom import get_all_ws_items, AllWsItem
from cws_insights.read_files import read_all_resource_files
from cws_insights.read_files_data import instantiate_all_resource_data
from cws_insights.schemas._index import AllResourceData


@dataclasses.dataclass
class MapObject:
    x: int
    y: int
    image_path: str


@dataclasses.dataclass
class BackgroundObject:
    xmax: int
    ymax: int
    image_path: str
    _bitmap: Image = None
    _grid_size: int = None

    @property
    def bitmap(self):
        return self._bitmap

    def __post_init__(self):
        self._bitmap = Image.open(self.image_path)

    def adjust_color(self, color_f: float = 0.6, contrast_f=0.2, brightness=1.7):
        converter = ImageEnhance.Color(self._bitmap)
        self._bitmap = converter.enhance(color_f)
        converter = ImageEnhance.Contrast(self._bitmap)
        self._bitmap = converter.enhance(contrast_f)
        converter = ImageEnhance.Brightness(self._bitmap)
        self._bitmap = converter.enhance(brightness)

    def scale_to_fit_maxcoords(self):
        ...

    def add_grid(self, delta: int, color: str, width: int):
        self._grid_size = delta
        middle = self.xmax // 2
        for n in range(self.xmax // delta + 1):
            for k in (1, -1):
                c = middle + k * (delta // 2 + n * delta)
                if not (0 <= c <= self.xmax):
                    continue
                shape = [(c, 0), (c, self.ymax)]
                img1 = ImageDraw.Draw(self._bitmap)
                img1.line(shape, fill=color, width=width)
                shape = [(0, c), (self.ymax, c)]
                img1 = ImageDraw.Draw(self._bitmap)
                img1.line(shape, fill=color, width=width)

    def paste_image(self, image: Image, center_coords: tuple[int, int]):
        shrink_factor = 0.75
        image = image.crop(image.getbbox())
        image = ImageOps.contain(
            image,
            (
                round(self._grid_size * shrink_factor),
                round(self._grid_size * shrink_factor),
            ),
        )
        # image = ImageOps.expand(image, border=(
        #    1,1,1,1
        # ), fill="black")
        cx, cy = center_coords
        px = cx - image.size[0] // 2
        py = cy - image.size[1] // 2
        try:
            self._bitmap.paste(image, (px, py), image)
        except ValueError:
            self._bitmap.paste(image, (px, py))


def create_map(
    background_image_path: str,
    xmax: int,
    ymax: int,
    all_coords: set[list[int]],
    thumb_image: Image,
) -> Image:
    m = BackgroundObject(xmax=xmax, ymax=ymax, image_path=background_image_path)
    m.add_grid(60, "red", 2)
    m.adjust_color()
    for x, y in all_coords:
        m.paste_image(thumb_image, (x, y))
    return m.bitmap


def create_all_maps(
    *,
    all_resource_data: AllResourceData,
    ws_items: AllWsItem,
    all_item_plus: AllItemPlus,
    world_map_png_path: str,
    wiki_contents_dir: str,
    item_sprites_dir: str,
):
    output_dir = os.path.join(wiki_contents_dir, "location_maps")
    os.makedirs(output_dir, exist_ok=True)
    coords_from_region_name = {
        uid: r.region_data.world_map_portrait_coordinate
        for uid, r in all_resource_data.map_region.items()
    }
    for uid, ws_item in ws_items.items():
        if not ws_item.region_locations_image:
            continue
        regions = all_item_plus[uid].from_map
        all_regions = set(
            regions.spawners
            + regions.world_objects
            + regions.herb_list
            + regions.prey_list
        )
        all_item_coords = {tuple(coords_from_region_name[r]) for r in all_regions}
        thumb_sprite = get_item_sprite_path(item_sprites_dir, uid)
        img = create_map(
            world_map_png_path, 500, 500, all_item_coords, Image.open(thumb_sprite)
        )
        save_loc = os.path.join(output_dir, ws_item.region_locations_image)
        img.save(save_loc)


def get_item_sprite_path(item_sprites_dir, uid):
    filename = get_stem_from_uid(uid) + ".png"
    loc = os.path.join(item_sprites_dir, filename)
    if not os.path.isfile(loc):
        loc = os.path.join(MORE_RESOURCES_PATH, filename)
    if not os.path.isfile(loc):
        raise ValueError(f"Cannot find sprite for {uid}")
    return loc


def main(gameresources_dir: str, wiki_contents_dir: str):
    all_raw_files = read_all_resource_files(gameresources_dir)
    all_resource_data = instantiate_all_resource_data(all_raw_files)
    all_item_plus = get_merged_item_data(all_resource_data)
    world_map_png_path = os.path.join(gameresources_dir, "map", "worldmap.png")
    item_sprites_dir = os.path.join(gameresources_dir, "items", "sprites")
    item_merged = get_merged_item_data(all_resource_data)
    ws_items = get_all_ws_items(item_merged, all_resource_data)
    create_all_maps(
        all_resource_data=all_resource_data,
        ws_items=ws_items,
        all_item_plus=all_item_plus,
        world_map_png_path=world_map_png_path,
        wiki_contents_dir=wiki_contents_dir,
        item_sprites_dir=item_sprites_dir,
    )


if __name__ == "__main__":
    gameresources_dir = CI_CD_GAMERESOURCES_DIR
    wiki_contents_dir = WIKI_CONTENTS_DIR
    main(gameresources_dir, wiki_contents_dir)
