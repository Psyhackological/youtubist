import yt_dlp
import argparse

parser = argparse.ArgumentParser(prog="Youtubist")
parser.add_argument(nargs='?', type=str, help="Playlist/channel URL. (str)", dest="url")
parser.add_argument('-r', "--reverse", action="store_true", help="Downloads from oldest videos to the newest.")
parser.add_argument('-d', "--duration", action="store_true", help="Adds duration entry to output file.")
parser.add_argument('-q', "--quiet", action="store_true", help="Silence printing out.")
args = parser.parse_args()


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
    with open(file_name, 'w+t', encoding='utf-8') as f:  # CREATE A NEW FILE AND MAKE SURE HE IS CLEAN
        f.seek(0)
        f.truncate()

    if 'entries' in result:  # CAN BE A PLAYLIST OR A LIST OF VIDEOS
        playlist = result['entries']  # GET ENTRIES FROM VIDEO

        for i, item in enumerate(playlist):  # LOOPS ENTRIES TO GRAB EACH VIDEO URL
            single_video = result['entries'][i]  # SINGLE VIDEO FROM ENUMERATE NUMBER
            title = single_video['title']  # TITLE
            url = f'https://youtu.be/{single_video["id"]}'  # SHORTEN LINK

            if args.duration:
                duration = single_video['duration']  # DURATION IS AN INT TYPE IN THE SECONDS
                minutes = (duration // 60) % 60
                seconds = duration % 60
                hours = duration // 3600

                if minutes < 10:  # FORCING MINUTES TO BE 2 CHARACTERS
                    minutes = f'0{minutes}'
                if seconds < 10:  # FORCING SECONDS TO BE 2 CHARACTERS
                    seconds = f'0{seconds}'

                with open(file_name, 'a+t', encoding='utf-8') as d:
                    if hours == 0:  # DO NOT WRITE HOURS
                        d.write(f'[{title}]({url}) | __{minutes}:{seconds}__\n')
                    else:  # DO WRITE HOURS
                        d.write(f'[{title}]({url}) | __{hours}:{minutes}:{seconds}__\n')

            else:
                todoist = f'[{title}]({url})'  # SPECIAL FORMAT IN TODOIST
                with open(file_name, 'a+t', encoding='utf-8') as t:  # OPEN FILE AND APPEND
                    t.write(todoist + "\n")  # WRITE EACH LINE
    else:
        print("Not a playlist.")
        quit()
