from dataclasses import dataclass
from typing import List, Iterable

import feedparser

from model import Fetcher


def get_titles_from_rss(url: str) -> List[str]:
    d = feedparser.parse(url)
    return [entry.title for entry in d.entries]


class RssFetcher(Fetcher):
    def __init__(self, url: str):
        self.url = url

    def fetch_titles(self) -> List[str]:
        titles = get_titles_from_rss(self.url)
        print(f"[RSS] Got {len(titles)} titles")
        return titles
