import os.path
import cws_insights
from cws_insights.read_files import read_all

if __name__=="__main__":
    this_dir = os.path.dirname(__file__)
    extensions_to_consider = (".meta", ".lang")
    gameresources_dir = os.path.abspath(os.path.join(this_dir, "..", "..", "cattails-wildwood-story-gameresources", "gameresources"))
    print(f"gameresources dir is '{gameresources_dir}'")
    all_data = read_all(gameresources_dir, file_suffixes=extensions_to_consider)
    footer = "\n\n".join([f"Found '{len(v)}' files in '{k}'" for k, v in all_data.items()])
    text = f"""
# Gifts / Items

|item|Alabaster|
|-|-|
|frog|❤️|
|bad_stuff|👿|

{footer}
"""
    with open(os.path.join(this_dir, "..", "..", "_site_src", "gifts.md"), "w", encoding="utf8") as f:
        f.write(text)

