import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube playlist or channel video information.")
    parser.add_argument("url", help="URL of the YouTube playlist or channel.")
    parser.add_argument("-j", "--save-json", help="Save raw JSON data to disk.",
                        action='store_true', default=False)
    parser.add_argument("-r", "--reverse-order",
                        help="Reverse the order of video entries (oldest to newest).", action='store_true', default=False)
    parser.add_argument("-d", "--sort-by-duration",
                        help="Sort video entries by duration (shortest to longest).", action='store_true', default=False)
    parser.add_argument("-f", "--save-to-file",
                        help="Save formatted output to a text file.", action='store_true', default=False)
    parser.add_argument(
        "-t", "--video-type", help="Type of videos to fetch. '0' for Videos, '1' for Shorts.", choices=['0', '1'], default='0')
    args = parser.parse_args()
    return args
