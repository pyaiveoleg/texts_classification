from abc import abstractmethod
from datetime import date
from typing import List

from mining.fetchers.browser_utils import Browser
from mining.model import Fetcher
from mining.util import daterange, format_day_month


class SimpleDateBasedFetcher(Fetcher):
    def __init__(self, from_date: date, until_date: date, css_selector: str, browser: Browser):
        self.from_date = from_date
        self.until_date = until_date
        self.browser = browser
        self.css_selector = css_selector

    @abstractmethod
    def get_url(self, year: str, month: str, day: str) -> str:
        ...

    def fetch_titles(self) -> List[str]:
        titles = set()
        for cur_date in daterange(self.from_date, self.until_date):
            url = self.get_url(str(cur_date.year), format_day_month(cur_date.month), format_day_month(cur_date.day))
            for title in self.browser.get_text_elements(url, self.css_selector):
                titles.add(title)
        return list(titles)


class VedomostiArchiveFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".article-preview-item__title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.vedomosti.ru/archive/{year}/{month}/{day}"


class KommersantArchiveFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".uho__link.uho__link--overlay", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.kommersant.ru/archive/list/77/day/{year}-{month}-{day}?cal_open=1"
