import yt_dlp

url = input("Playlist/channel URL: ")
reverse = input("From newest to oldest? (Y/n): ")
quiet = input("Waste time printing out? (Y/n): ")
wants_duration = input("Do you want duration entry? (y/N): ")

reverse = True if 'n' in reverse.lower() else False
quiet = True if 'n' in quiet.lower() else False
wants_duration = True if 'y' in wants_duration.lower() else False

ydl_opts = {  # YT-DLP OPTIONS
    'simulate': True,  # DO NOT DOWNLOAD VIDEOS OR AUDIO TO THE DISK
    'quiet': quiet,  # DO NOT PRINT ANYTHING BE QUIET
    'playlistreverse': reverse  # FROM LAST TO 1ST ITEM IF TRUE
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # SPECIAL YT-DLP OBJECT WITH YDL_OPTS (OPTIONS)

    try:
        result = ydl.extract_info(url, download=False)  # WE WANT INFO WITHOUT DOWNLOADING THE VIDEO
    except yt_dlp.utils.DownloadError:  # SILLY YOU, THAT IS NOT A VALID
        quit()

    with open('todoist.txt', 'w+t', encoding='utf-8') as f:  # CREATE A NEW FILE AND MAKE SURE HE IS CLEAN
        f.seek(0)
        f.truncate()

    if 'entries' in result:  # CAN BE A PLAYLIST OR A LIST OF VIDEOS
        video = result['entries']  # GET ENTRIES FROM VIDEO

        for i, item in enumerate(video):  # LOOPS ENTIRES TO GRAB EACH VIDEO URL
            video = result['entries'][i]  # SINGLE VIDEO FROM ENUMARATE NUMBER
            title = video['title']  # TITLE
            url = f'https://youtu.be/{video["id"]}'  # SHORTEN LINK

            if wants_duration:
                duration = video['duration']  # DURATION IS AN INT TYPE IN THE SECONDS
                minutes = (duration // 60) % 60
                seconds = duration % 60
                hours = duration // 3600

                if minutes < 10:  # FORCING MINUTES TO BE 2 CHARACTERS
                    minutes = f'0{minutes}'
                if seconds < 10:  # FORCING SECONDS TO BE 2 CHARACTERS
                    seconds = f'0{seconds}'

                with open('youtubist.txt', 'a+t', encoding='utf-8') as d:
                    if hours == 0:  # DO NOT WRITE HOURS
                        d.write(f'[{title}]({url}) | __{minutes}:{seconds}__\n')
                    else:  # DO WRITE HOURS
                        d.write(f'[{title}]({url}) | __{hours}:{minutes}:{seconds}__\n')

            else:
                todoist = f'[{title}]({url})'  # SPECIAL FORMAT IN TODOIST
                with open('todoist.txt', 'a+t', encoding='utf-8') as t:  # OPEN FILE AND APPEND
                    t.write(todoist + "\n")  # WRITE EACH LINE
    else:
        print("Not a playlist")
        quit()
