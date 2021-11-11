import os
from pathlib import Path
import json
from typing import List

from model import Dataset, Source
from util import sanitize


def gather_dataset(sources: List[Source]) -> Dataset:
    return [source.fetch_articles() for source in sources]


def dump_dataset(dataset: Dataset, folder: str):
    folder = Path(folder)
    os.makedirs(folder, exist_ok=True)

    with open(folder / 'sources.json', "w") as sources_file:
        sources_dict = dict()
        for source_id, fetched_articles in enumerate(dataset):
            sources_dict[source_id] = fetched_articles.source_name
        sources_file.write(json.dumps(sources_dict, ensure_ascii=False))

    with open(folder / 'articles.txt', "w") as articles_file:
        for source_id, fetched_articles in enumerate(dataset):
            for title in fetched_articles.titles:
                articles_file.write(f"__label_{source_id} {sanitize(title)}\n")
