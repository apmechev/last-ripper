#!python3
import sys
from options import parser
from download_tracks import download_tracks

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])

    download_tracks(args.username, args.limit)
