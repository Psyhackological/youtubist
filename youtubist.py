import yt_dlp
import argparse

parser = argparse.ArgumentParser(prog="Youtubist")
parser.add_argument(nargs='?', type=str, help="Playlist/channel URL. (str)", dest="url")
parser.add_argument('-r', "--reverse", action="store_true", help="Downloads from oldest videos to the newest.")
parser.add_argument('-d', "--duration", action="store_true", help="Adds duration entry to output file.")
parser.add_argument('-q', "--quiet", action="store_true", help="Silence printing out.")
args = parser.parse_args()


def seconds_to_time(seconds):
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    hours = seconds // 3600

    if minutes < 10:  # FORCING MINUTES TO BE 2 CHARACTERS
        minutes = f'0{minutes}'
    if seconds < 10:  # FORCING SECONDS TO BE 2 CHARACTERS
        seconds = f'0{seconds}'

    if hours == 0:  # DO NOT WRITE HOURS
        return f'[{title}]({url}) | __{minutes}:{seconds}__\n'
    else:  # DO WRITE HOURS
        return f'[{title}]({url}) | __{hours}:{minutes}:{seconds}__\n'


ydl_opts = {  # YT-DLP OPTIONS
    'simulate': True,  # DO NOT DOWNLOAD VIDEOS OR AUDIO TO THE DISK
    'quiet': args.quiet,  # DO NOT PRINT ANYTHING BE QUIET
    'playlistreverse': args.reverse  # FROM LAST TO 1ST ITEM IF TRUE
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # SPECIAL YT-DLP OBJECT WITH YDL_OPTS (OPTIONS)

    try:
        result = ydl.extract_info(args.url, download=False)  # WE WANT INFO WITHOUT DOWNLOADING THE VIDEO
    except yt_dlp.utils.DownloadError:  # SILLY YOU, THAT IS NOT A VALID
        quit()

    file_name = f"{result['uploader'].replace(' ', '_')}.txt"
    with open(file_name, 'w+t', encoding='utf-8') as file:  # CREATE A NEW FILE AND MAKE SURE HE IS CLEAN
        file.seek(0)
        file.truncate()

    if 'entries' in result:  # CAN BE A PLAYLIST OR A LIST OF VIDEOS
        playlist = result['entries']  # GET ENTRIES FROM VIDEO

        for i, item in enumerate(playlist):  # LOOPS ENTRIES TO GRAB EACH VIDEO URL
            single_video = result['entries'][i]  # SINGLE VIDEO FROM ENUMERATE NUMBER
            title = single_video['title']  # TITLE
            url = f'https://youtu.be/{single_video["id"]}'  # SHORTEN LINK

            if args.duration:
                duration = single_video['duration']  # DURATION IS AN INT TYPE IN THE SECONDS
                entry_name = seconds_to_time(duration)
                with open(file_name, 'a+t', encoding='utf-8') as file:
                    file.write(entry_name)
            else:
                todoist = f'[{title}]({url})\n'  # SPECIAL FORMAT IN TODOIST
                with open(file_name, 'a+t', encoding='utf-8') as file:  # OPEN FILE AND APPEND
                    file.write(todoist)  # WRITE EACH LINE
    else:
        print("Not a playlist.")
        quit()
