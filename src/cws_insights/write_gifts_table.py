import os.path
import cws_insights

if __name__=="__main__":
    text = """
# Gifts / Items

|item|Alabaster|
|-|-|
|frog|❤️|
|bad_stuff|👿|
"""
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, "..", "..", "_site_src", "gifts.md"), "w", encoding="utf8") as f:
        f.write(text)

