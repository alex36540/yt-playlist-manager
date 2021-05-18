"""
File: main.py
Author: Alexander Lee (https://github.com/alex36540)

Description: Runs the playlist manager.
"""
from pyyoutube import Api

from private import *
from playlist import Playlist

api = Api(api_key=API_KEY)


def main() -> None:
    playlist = Playlist(api, PLAYLIST_ID)


if __name__ == '__main__':
    main()
