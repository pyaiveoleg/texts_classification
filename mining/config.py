from datetime import date

from fetchers.rss_fetcher import RssFetcher
from mining.fetchers.browser_utils import Browser
from mining.fetchers.date_browser_fetchers import VedomostiArchiveFetcher, KommersantArchiveFetcher
from model import Source

output_folder = "output"

browser = Browser()

sources = [
    Source(
        name="Ведомости",
        fetchers=[
            RssFetcher("https://www.vedomosti.ru/rss/news"),
            RssFetcher("https://www.vedomosti.ru/rss/articles"),
            VedomostiArchiveFetcher(from_date=date(2021, 11, 1), until_date=date(2021, 11, 3), browser=browser),
        ]
    ),
    Source(
        name="Коммерсантъ",
        fetchers=[
            RssFetcher("https://www.kommersant.ru/RSS/corp.xml"),
            RssFetcher("https://www.kommersant.ru/RSS/news.xml"),
            KommersantArchiveFetcher(from_date=date(2021, 11, 1), until_date=date(2021, 11, 3), browser=browser)
        ]
    ),
    Source(
        name="Российская Газета",
        fetchers=[
            RssFetcher("https://rg.ru/tema/rss.xml")
        ]
    ),
    Source(
        name="РИА Новости",
        fetchers=[
            RssFetcher("https://ria.ru/export/rss2/archive/index.xml")
        ]
    ),
    Source(
        name="LentaRU",
        fetchers=[
            RssFetcher("https://lenta.ru/rss/news"),
            RssFetcher("https://lenta.ru/rss/articles"),
            RssFetcher("https://lenta.ru/rss/top7"),
            RssFetcher("https://lenta.ru/rss/last24")
        ]
    ),
    Source(
        name="Голос Америки",
        fetchers=[
            RssFetcher("https://www.golosameriki.com/api/zkivremjvq"),
            RssFetcher("https://www.golosameriki.com/api/zkroqremuoqq")
        ]
    ),
    Source(
        name="РБК",
        fetchers=[
            RssFetcher("https://rssexport.rbc.ru/rbcnews/news/30/full.rss"),
            RssFetcher("http://static.feed.rbc.ru/rbc/logical/footer/news.rss")
        ]
    )

]