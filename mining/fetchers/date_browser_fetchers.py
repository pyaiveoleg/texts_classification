from abc import abstractmethod
from datetime import date
from typing import List

from fetchers.browser_utils import Browser
from model import Fetcher
from util import daterange, format_day_month


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
            try:
                url = self.get_url(str(cur_date.year), format_day_month(cur_date.month), format_day_month(cur_date.day))
                for title in self.browser.get_text_elements(url, self.css_selector):
                    titles.add(title)
            except Exception as e:
                print(f"Exception while fetching titles for {cur_date}: {e}")
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


class RgFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".b-link.b-link_title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://rg.ru/search/?from={day}.{month}.{year}&to={day}.{month}.{year}"


class LentaRuFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, "h3.card-title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://lenta.ru/{year}/{month}/{day}/"


class RiaFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, "a.list-item__title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://ria.ru/{year}{month}{day}/"


class RbkFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".search-item__title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.rbc.ru/search/?query=%D0%A0%D0%91%D0%9A&dateFrom={day}.{month}.{year}&dateTo={day}.{month}.{year}"


class GolosAmerikiFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".media-block__title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.golosameriki.com/novosti/{year}/{month}/{day}"


class PopcornNewsFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_date: date, until_date: date, browser: Browser):
        super().__init__(from_date, until_date, ".articles-archive_articles-title", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.popcornnews.ru/archive/{year}/{month}/{day}"


class E1SexFetcher(SimpleDateBasedFetcher):
    def __init__(self, from_data: date, until_date: date, browser: Browser):
        super().__init__(from_data, until_date, "h2.GZjx", browser)

    def get_url(self, year: str, month: str, day: str) -> str:
        return f"https://www.e1.ru/text/tags/%D1%81%D0%B5%D0%BA%D1%81/?dateFrom={day}.{month}.{year}&dateTo={day}.{month}.{year}"
