"""
File: main.py
Author: Alexander Lee (https://github.com/alex36540)

Description: Runs the playlist manager.
"""
import pyyoutube
from private import *
import video

api = pyyoutube.Api(api_key=API_KEY)


def main() -> None:
    playlist = api.get_playlist_by_id(playlist_id=PLAYLIST_ID).items[0]
    name = playlist.snippet.title

    videos = video.get_videos(api, PLAYLIST_ID)

    video.write_videos(videos, name)
    print(video.load_videos(name))


if __name__ == '__main__':
    main()
