from dataclasses import dataclass
from typing import Protocol, List


class Fetcher(Protocol):
    def fetch_titles(self) -> List[str]: ...


@dataclass
class Source:
    name: str
    fetchers: List[Fetcher]

    def fetch_articles(self) -> 'FetchedArticles':
        titles = set()
        for fetcher in self.fetchers:
            for title in fetcher.fetch_titles():
                titles.add(title)
        print(f"Fetched {len(titles)} articles from '{self.name}'")
        return FetchedArticles(source_name=self.name, titles=list(titles))


@dataclass
class FetchedArticles:
    source_name: str
    titles: List[str]


Dataset = List[FetchedArticles]
