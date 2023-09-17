import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube playlist or channel video information.")
    parser.add_argument("url", help="URL of the YouTube playlist or channel.")
    args = parser.parse_args()
    return args
