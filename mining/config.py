from datetime import date

from fetchers.rss_fetcher import RssFetcher
from fetchers.browser_utils import Browser
from fetchers.date_browser_fetchers import VedomostiArchiveFetcher, KommersantArchiveFetcher, RgFetcher, \
    LentaRuFetcher, RiaFetcher, RbkFetcher, GolosAmerikiFetcher, PopcornNewsFetcher, E1SexFetcher
from model import Source

output_folder = "output"

browser = Browser()

from_date = date(2010, 11, 1)
until_date = date(2021, 11, 3)

sources = [
    Source(
        name="Ведомости",
        fetchers=[
            RssFetcher("https://www.vedomosti.ru/rss/news"),
            RssFetcher("https://www.vedomosti.ru/rss/articles"),
            VedomostiArchiveFetcher(from_date, until_date, browser),
        ]
    ),
    Source(
        name="Коммерсантъ",
        fetchers=[
            RssFetcher("https://www.kommersant.ru/RSS/corp.xml"),
            RssFetcher("https://www.kommersant.ru/RSS/news.xml"),
            KommersantArchiveFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="Российская Газета",
        fetchers=[
            RssFetcher("https://rg.ru/tema/rss.xml"),
            # RgFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="РИА Новости",
        fetchers=[
            RssFetcher("https://ria.ru/export/rss2/archive/index.xml"),
            RiaFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="LentaRU",
        fetchers=[
            RssFetcher("https://lenta.ru/rss/news"),
            RssFetcher("https://lenta.ru/rss/articles"),
            RssFetcher("https://lenta.ru/rss/top7"),
            RssFetcher("https://lenta.ru/rss/last24"),
            LentaRuFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="Голос Америки",
        fetchers=[
            RssFetcher("https://www.golosameriki.com/api/zkivremjvq"),
            RssFetcher("https://www.golosameriki.com/api/zkroqremuoqq"),
            GolosAmerikiFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="РБК",
        fetchers=[
            RssFetcher("https://rssexport.rbc.ru/rbcnews/news/30/full.rss"),
            RssFetcher("http://static.feed.rbc.ru/rbc/logical/footer/news.rss"),
            RbkFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="PopcornNews",
        fetchers=[
            PopcornNewsFetcher(from_date, until_date, browser)
        ]
    ),
    Source(
        name="E1",
        fetchers=[
            E1SexFetcher(from_date, until_date, browser)
        ]
    )
]
