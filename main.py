import pyperclip
import yt_dlp

from argparse_parsing import parse_arguments


def fetch_youtube_playlist_info(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        entries = info_dict.get('entries', [])

    formatted_output = []
    for video_info in entries:
        title = video_info.get("title", "Unknown Title")
        url = video_info.get("url", "Unknown URL")
        duration = video_info.get("duration", "Unknown Duration")

        duration_hms = f"{int(duration // 3600):02d}:{int((duration % 3600) // 60):02d}:{int(duration % 60):02d}"

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
