import argparse

parser = argparse.ArgumentParser(description="Download tracks from lastfm")
parser.add_argument('--username', help='The last fm user to get top tracks for')
parser.add_argument('--limit', type=int, default=10, help='The maximum number of tracks to get')
parser.add_argument('--output-folder', default="output")