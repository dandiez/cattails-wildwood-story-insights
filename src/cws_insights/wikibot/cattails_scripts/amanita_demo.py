import pywikibot
from pywikibot import pagegenerators

site = pywikibot.Site()
page = pywikibot.Page(site, "Amanita")
current_text = page.text
print(page.text)
to_add = """{{Items|title1=Amanita|image1=Amanita.png|description=A mysterious redcap mushroom that comes in many varieties. Some are safe, some are not. Who knows what eating it will do?|sell_price=12 [[Currency#Mews|Mews]], 0 [[Currency#Mole Cash|Mole Cash]]|rarity=Rare|found=...|can_be_consumed:=Yes}}
"""
new_text = to_add + current_text
page.text = new_text
page.save("Added summary box.")
