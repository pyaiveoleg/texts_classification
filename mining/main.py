from config import sources, output_folder, browser
from dataset_manipulation import gather_dataset


def main():
    print(f"Gathering dataset from {len(sources)} sources and dumping to '{output_folder}'")
    gather_dataset(sources, output_folder)
    print(f"Finished")
    browser.close()


if __name__ == '__main__':
    main()
