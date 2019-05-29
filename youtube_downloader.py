import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

def download_video(youtube_url):
    print(youtube_url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == '__main__':
    download_video(['https://www.youtube.com/watch?v=aCrrsm0U4t0'])