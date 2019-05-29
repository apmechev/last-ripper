import itertools
import pylast

def get_last_fm_tracks(username):
    pass

def youtube_url_for_track(track_id):
    pass

def find_youtube_urls(username, limit=10):
    tracks = get_last_fm_tracks(username)
    for track in itertools.islice(tracks, limit):
        youtube_url = youtube_url_for_track(track)
        print(youtube_url)

find_youtube_urls('dntbrsnbl')