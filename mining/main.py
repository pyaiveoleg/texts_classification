from config import sources, output_folder, browser
from dataset_manipulation import dump_dataset, gather_dataset


def main():
    print(f"Gathering dataset from {len(sources)} sources")
    dataset = gather_dataset(sources)
    print(f"Dumping dataset to '{output_folder}'")
    dump_dataset(dataset, output_folder)
    browser.close()


if __name__ == '__main__':
    main()
