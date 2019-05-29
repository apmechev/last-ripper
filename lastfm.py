import json
import pylast

def get_config():
    config = None
    with open('lastfm.json') as f:
        config = json.load(f)

    return config

def get_network():
    config = get_config()
    return pylast.LastFMNetwork(api_key=config['api_key'], api_secret=config['api_secret'])

def get_library_tracks(username):
    pass

def get_artist_tracks(artist_name):
    network = get_network()
    artist = pylast.Artist(artist_name, network)

    return artist.get_top_tracks()

def get_top_tracks(user_name, limit=None):
    network = get_network()
    user = pylast.User(user_name, network)
    return user.get_top_tracks(limit=limit)

if __name__ == '__main__':
    print(get_top_tracks('dntbrsnbl', limit=1000))
