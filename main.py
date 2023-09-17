import json

import pyperclip
import yt_dlp

from argparse_parsing import parse_arguments


def fetch_youtube_playlist_info(args):
    ydl_opts = {
        "extract_flat": True,
        "force_generic_extractor": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(args.url, download=False)

        if args.save_json:
            with open("debug_info.json", "w", encoding="utf-8") as json_file_handle:
                json.dump(info_dict, json_file_handle, indent=4)

        videos_info = info_dict.get("entries", [{}])[
            int(args.video_type)].get("entries", [])

    formatted_output = []
    for video_info in videos_info:
        title = video_info.get("title", "Unknown Title")
        url = video_info.get("id", "Unknown URL")

        if args.video_type == '0':  # For Videos
            duration = int(video_info.get("duration", 0))
            duration_hms = f"{duration // 3600:02d}:{(duration % 3600) // 60:02d}:{duration % 60:02d}"
            formatted_output.append(
                (duration, f"{duration_hms} | [{title}](https://youtu.be/{url})"))
        elif args.video_type == '1':  # For Shorts
            formatted_output.append(
                (None, f"[{title}](https://youtu.be/{url})"))
        else:
            print("No entries found for the given video type.")

    if args.reverse_order:
        formatted_output.reverse()

    if args.sort_by_duration:
        formatted_output.sort(key=lambda x: x[0] if x[0] is not None else 0)

    final_output = "\n".join(x[1] for x in formatted_output)

    if args.save_to_file:
        with open("formatted_output.txt", "w") as f:
            f.write(final_output)

    pyperclip.copy(final_output)

    total_entries = final_output.count('\n') + 1
    print(
        f"Formatted video information has been copied to clipboard. Total entries: {total_entries}")


def main():
    args = parse_arguments()
    fetch_youtube_playlist_info(args)


if __name__ == "__main__":
    main()
