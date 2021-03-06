from dataclasses import dataclass
from typing import Protocol, List, Optional


class Fetcher(Protocol):
    def fetch_titles(self) -> List[str]: ...


@dataclass
class Source:
    name: str
    fetchers: List[Fetcher]
    skip: bool = False

    def fetch_titles(self) -> List[str]:
        titles = set()
        for fetcher in self.fetchers:
            try:
                fetched_titles = fetcher.fetch_titles()
            except Exception as e:
                print(f"Fetcher failed with an exception: {e}")
                continue
            for title in fetched_titles:
                titles.add(title)
        print(f"Fetched {len(titles)} articles from '{self.name}'")
        return list(titles)
