import sys
from collections import defaultdict
from enum import Enum, IntEnum, StrEnum
from pathlib import Path


import os

import mwparserfromhell
import pandas as pd

THIS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(THIS_DIR, "..", "..", ".."))
sys.path.insert(0, SRC_DIR)


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


def get_wildwood_page_name(page_name: str) -> str:
    return page_name + "/Wildwood Story"


@dataclasses.dataclass
class PageNameInfo:
    base_page_name: str
    base_page_exists: bool
    base_page_has_category_cattails: bool
    base_page_has_category_wildwood: bool
    base_page_is_redirect: bool

    wildwood_page_name: str
    wildwood_page_exists: bool
    wildwood_page_has_category_cattails: bool
    wildwood_page_has_category_wildwood: bool
    wildwood_page_is_redirect: bool



TEMPLATE_NAME = "WSItem"


def has_new_template(page: Page):
    text = page.text
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates(recursive=False)
    if any(t.name.matches(TEMPLATE_NAME) for t in templates):
        return True
    return False


def is_tbd(cwpage):
    text = cwpage.page.text.strip().lower()
    if text in ("tbd", "tba"):
        return True
    return False


def fetch_info():
    site = pywikibot.Site()
    cattails_1 = pywikibot.Category(site, "Cattails")
    ct1_pages = {p.title() for p in cattails_1.articles()}
    cattails_2 = pywikibot.Category(site, "Wildwood_Story")
    ct2_pages = {p.title() for p in cattails_2.articles()}
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
    for root, dirs, files in os.walk(item_pages_dir):
        for f in files:
            page_name = Path(f).stem
            page_exists = page_name in page_by_name
            page_name_wildwood = get_wildwood_page_name(page_name)
            page_wildwood_exists = page_name_wildwood in page_by_name
            yield PageNameInfo(
                base_page_name=page_name,
                base_page_exists=page_exists,
                base_page_has_category_cattails=page_name in ct1_pages,
                base_page_has_category_wildwood=page_name in ct2_pages,
                base_page_is_redirect=page_by_name[page_name].is_redir
                if page_exists
                else None,

                wildwood_page_name=page_name_wildwood,
                wildwood_page_exists=page_wildwood_exists,
                wildwood_page_has_category_cattails=page_name_wildwood in ct1_pages,
                wildwood_page_has_category_wildwood=page_name_wildwood in ct2_pages,
                wildwood_page_is_redirect=page_by_name[page_name_wildwood].is_redir
                if page_wildwood_exists
                else None,

            )


class AuditCode(StrEnum):
    NEEDS_MANUAL_FIX = "NEEDS_MANUAL_FIX"
    BASE_PAGE_MISSING = "BASE_PAGE_MISSING"
    BAD_CATEGORY = "BAD_CATEGORY"
    MISSING_CATEGORY_WILDWOOD_ON_BASE_PAGE = "MISSING_CATEGORY_WILDWOOD_ON_BASE_PAGE"
    OK_BOTH_GAMES_HAVE_ITEM = "OK_BOTH_GAMES_HAVE_ITEM"
    OK_ONLY_WILDWOOD_HAS_ITEM = "OK_ONLY_WILDWOOD_HAS_ITEM"
    WILDWOOD_PAGE_MISSING = "WILDWOOD_PAGE_MISSING"
    MISSING_WILDWOOD_REDIRECT_PAGE = "MISSING_WILDWOOD_REDIRECT_PAGE"
    MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE = (
        "MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE"
    )


def run_audit(i: PageNameInfo) -> AuditCode:
    print = lambda x: x
    if i.base_page_is_redirect:
        print("Bad page")
        return AuditCode.NEEDS_MANUAL_FIX
    if not i.base_page_exists:
        print("Missing page")
        return AuditCode.BASE_PAGE_MISSING
    if i.base_page_has_category_cattails:
        if i.base_page_has_category_wildwood:
            print("Bad categories")
            return AuditCode.BAD_CATEGORY
        if i.wildwood_page_exists:
            if i.wildwood_page_is_redirect:
                print("unexpected redirect")
                return AuditCode.NEEDS_MANUAL_FIX
            if not i.wildwood_page_has_category_wildwood:
                print("missing category wildwood")
                return AuditCode.MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE
            print("ok page - same item in two games, both categorised.")
            return AuditCode.OK_BOTH_GAMES_HAVE_ITEM
        print("need to create wildwood page for item")
        return AuditCode.WILDWOOD_PAGE_MISSING
    if not i.base_page_has_category_wildwood:
        print("missing category")
        return AuditCode.MISSING_CATEGORY_WILDWOOD_ON_BASE_PAGE
    if not i.wildwood_page_exists:
        print("missing redirect page for only wildwood item")
        return AuditCode.MISSING_WILDWOOD_REDIRECT_PAGE
    if i.wildwood_page_is_redirect:
        print("ok page redirect (assuming it redirects to base page...)")
        return AuditCode.OK_ONLY_WILDWOOD_HAS_ITEM
    if not i.wildwood_page_has_category_wildwood:
        print("missing category wildwood")
        return AuditCode.MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE
    print("unexpected page same item in two games both categorised wildwood")
    return AuditCode.NEEDS_MANUAL_FIX


def main():
    info = list(fetch_info())
    # df = pd.DataFrame(fetch_info())
    # df.to_csv("page_audit.csv", index=False)
    check_summary = defaultdict(list)
    for i in info:
        audit_code = run_audit(i)
        check_summary[audit_code].append(i)

    for k, v in check_summary.items():
        print(k, len(v))  # , [x.base_page_name for x in v])
    if AuditCode.MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE in check_summary:
        for p in check_summary[AuditCode.MISSING_CATEGORY_WILDWOOD_ON_WILDWOOD_PAGE]:
            print(p.wildwood_page_name)

if __name__ == "__main__":
    main()
