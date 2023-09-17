import json

import pyperclip
import yt_dlp

from argparse_parsing import parse_arguments


def fetch_youtube_playlist_info(playlist_url):
    ydl_opts = {
        "extract_flat": True,
        "force_generic_extractor": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)

        # Write the debug information to a JSON file
        with open("debug_info.json", "w", encoding="utf-8") as json_file_handle:
            json.dump(info_dict, json_file_handle, indent=4)

        # Directly access the entries under "Videos", which is assumed to be the first entry
        videos_info = info_dict.get("entries", [{}])[0].get("entries", [])

    formatted_output = []
    for video_info in videos_info:
        title = video_info.get("title", "Unknown Title")
        url = video_info.get("id", "Unknown URL")
        duration = int(video_info.get("duration", 0))
        duration_hms = (
            f"{duration // 3600:02d}:{(duration % 3600) // 60:02d}:{duration % 60:02d}"
        )
        formatted_output.append(
            f"[{title}](https://youtu.be/{url}) | {duration_hms}")

    return "\n".join(formatted_output)


def main():
    args = parse_arguments()
    formatted_info = fetch_youtube_playlist_info(args.url)
    print("Formatted Video Information:")
    print(formatted_info)
    pyperclip.copy(formatted_info)
    print("Formatted video information has been copied to clipboard.")


if __name__ == "__main__":
    main()
