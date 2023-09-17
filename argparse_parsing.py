import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube playlist or channel video information.")
    parser.add_argument("url", help="URL of the YouTube playlist or channel.")
    parser.add_argument("--save-json", help="Save raw JSON data to disk.",
                        action='store_true', default=False)
    args = parser.parse_args()
    return args
