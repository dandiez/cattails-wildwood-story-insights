import sys
from pathlib import Path

import mwparserfromhell
import os

THIS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", "..", ".."))
sys.path.insert(0, SRC_DIR)

from cws_insights.wikibot.cattails_scripts.audit_pages import (
    fetch_info,
    run_audit,
    AuditCode,
    get_wildwood_page_name,
    TEMPLATE_NAME,
    has_new_template,
    is_tbd,
)

import dataclasses

import pywikibot
from pywikibot import Page

from cws_insights.common import WIKI_CONTENTS_DIR


@dataclasses.dataclass
class CWPage:
    page: Page
    title: str
    id: int
    is_redir: bool


def replace_whole_page_with_template(cwpage: CWPage, contents: str):
    page = cwpage.page
    page.text = contents
    page.save("Automatic update from files.")


def update_template(cwpage: CWPage, new_template: str):
    page = cwpage.page
    text = page.text
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates(recursive=False)
    for t in templates:
        if t.name.matches(TEMPLATE_NAME):
            wikicode.replace(t, new_template)
            break
    new_text = str(wikicode)
    if new_text == text:
        # print(f"Page did not change: {cwpage.title}")
        return
    page.text = new_text
    page.save("Automatic update from files.")
    print(f"Page updated: {cwpage.title}")


def add_page(site, page_title: str, contents: str):
    new_page = Page(site, page_title)
    new_page.text = contents
    new_page.save("Page created automatically based on game files.")


def create_wildwood_redirect_page(page_name, wildwood_page_name, site):
    new_page = Page(site, wildwood_page_name)
    new_page.text = f"#REDIRECT [[{page_name}]]"
    new_page.save("Add redirect for Wildwood exclusive item")
    print(f"Created redirect {wildwood_page_name} --> {page_name}")


def main():
    site = pywikibot.Site()
    all_pages = []
    for page in site.allpages():
        page_info = CWPage(
            page=page,
            title=page.title(),
            id=page._pageid,
            is_redir=page.isRedirectPage(),
        )
        all_pages.append(page_info)
    print(len(all_pages))
    page_by_name = {p.title: p for p in all_pages}

    item_pages_dir = os.path.join(WIKI_CONTENTS_DIR, "fandom_items")
    info_per_page = {i.base_page_name: run_audit(i) for i in fetch_info()}
    for root, dirs, files in os.walk(item_pages_dir):
        for f in files:
            item_name = Path(f).stem
            full_file_path = os.path.join(root, f)
            with open(full_file_path) as wikifile:
                contents = wikifile.read()

            info = info_per_page[item_name]
            if info in {
                AuditCode.WILDWOOD_PAGE_MISSING,
                AuditCode.MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE,
                AuditCode.OK_BOTH_GAMES_HAVE_ITEM,
            }:
                page_name = get_wildwood_page_name(item_name)
            elif info == AuditCode.MISSING_WILDWOOD_REDIRECT_PAGE:
                create_wildwood_redirect_page(
                    item_name, get_wildwood_page_name(item_name), site
                )
                continue
            elif info in {
                AuditCode.OK_ONLY_WILDWOOD_HAS_ITEM, AuditCode
            }:
                page_name = item_name
            else:
                continue
            create_or_update_page(page_name, contents, page_by_name, site)


def create_or_update_page(page_name, contents, page_by_name, site):
    page_exists = page_name in page_by_name
    if page_exists:
        cwpage = page_by_name[page_name]
        if has_new_template(cwpage.page):
            update_template(cwpage, contents)
        elif is_tbd(cwpage):
            print(f"Page {page_name} is tbd. Will get updated.")
            replace_whole_page_with_template(cwpage, contents)
        else:
            print(f"Page {page_name} exists already with content.")
    else:
        print(f"***Page {page_name} does not exist.")
        add_page(site, page_name, contents)


if __name__ == "__main__":
    main()
