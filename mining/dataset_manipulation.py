import os
from pathlib import Path
import json
from typing import List

from model import Source
from util import sanitize


def gather_dataset(sources: List[Source], output_folder: str):
    folder = Path(output_folder)
    os.makedirs(folder, exist_ok=True)
    # dump sources.json
    with open(folder / 'sources.json', "w") as sources_file:
        sources_dict = dict()
        for source_id, source in enumerate(sources):
            sources_dict[source_id] = source.name
        sources_file.write(json.dumps(sources_dict, ensure_ascii=False))
    # dump articles.txt for each source
    with open(folder / 'articles.txt', "w") as articles_file:
        for source_id, source in enumerate(sources):
            if source.skip:
                print(f"Skipping source {source.name}")
                continue
            for title in source.fetch_titles():
                articles_file.write(f"__label_{source_id} {sanitize(title)}\n")
