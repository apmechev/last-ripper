from find_youtube_urls import youtube_url_for_track
from lastfm import get_top_tracks
from youtube_downloader import download_video

def download_tracks(user_name, limit, output_folder):
    print(output_folder)
    tracks = get_top_tracks(user_name, limit=limit)

    for track in tracks:
        youtube_url = youtube_url_for_track(track.item)

        if not youtube_url:
            print("Couldn't parse url for", track.item.name)
            continue

        download_video(youtube_url)

if __name__ == '__main__':
    download_tracks('dntbrsnbl')