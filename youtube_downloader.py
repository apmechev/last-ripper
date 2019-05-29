import youtube_dl

def download_video(youtube_url, output_folder):
    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
        {'key': 'FFmpegMetadata'}]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=aCrrsm0U4t0', 'output')