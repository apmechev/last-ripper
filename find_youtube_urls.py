import itertools
import pylast
import requests
import re

from lastfm import get_top_tracks

youtube_url_finder = re.compile('watch\\?\\=', re.M)

def youtube_url_for_track(track):
    page_url = f'https://www.last.fm/music/{track.artist.name}/_/{track.title}'
    response = requests.get(page_url)
    html = response.content.decode('utf8')

    match = youtube_url_finder.search(html)

    try:
        start = html.index('https://www.youtube.com/watch?v=')
        end = html.index('"', start)

        url = html[start:end]
        return url
    except:
        return None