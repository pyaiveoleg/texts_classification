import sys
from config import sources, output_folder, browser
from dataset_manipulation import gather_dataset
from model import Source

sys.path.append('.')
sys.path.append('..')


def main():
    if len(sys.argv) >= 2:
        source_id = int(sys.argv[1])
        source = sources[source_id]
        print(f"Selected 1 source: {source.name}")
        fake_sources = [Source("NONE", [], True)] * source_id + [source]
        gather_dataset(fake_sources, output_folder)
        print(f"Finished")
    else:
        print(f"Gathering dataset from {len(sources)} sources and dumping to '{output_folder}'")
        gather_dataset(sources, output_folder)
        print(f"Finished")
    browser.close()


if __name__ == '__main__':
    main()
