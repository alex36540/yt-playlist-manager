"""
File: video.py
Author: Alexander Lee (https://github.com/alex36540)

Description: Contains representation of a video as well as operations on a playlist pertaining
             to videos.
"""
from dataclasses import dataclass
from typing import List
import pickle
from os import path


@dataclass(unsafe_hash=True)
class Video:
    """Class that represents a video"""
    id: str
    title: str
    index: int


def get_videos(api, playlist_id: str) -> List[Video]:
    """
    Gets all of the videos from a playlist.

    :param api: The api object to use
    :param playlist_id: The id of the playlist
    :return: An array containing video objects of every video on the playlist
    """
    videos = []
    pl_id = playlist_id

    pl_items = api.get_playlist_items(playlist_id=pl_id, count=None, limit=50)

    for item in pl_items.items:
        videos.append(Video(
            item.snippet.resourceId.videoId, item.snippet.title, item.snippet.position  # Create video object
        ))

    return videos


def write_videos(pl_videos: List[Video], pl_name: str) -> None:
    """
    Writes a list of videos to a file. Also checks for new deletions so that the user can be notified of them.

    :param pl_videos: List of videos to be converted into a file
    :param pl_name: Name of the playlist (also serves as the file name)
    :return: None
    """
    file_name = "files/" + pl_name + ".pkl"
    deleted_videos = set()

    # if the file already exists, check for new video deletions
    if path.exists(file_name):
        loaded_videos = load_videos(pl_name)

        for video in loaded_videos:
            if video.title == "Deleted video":
                deleted_videos.add(video)

    with open(file_name, "wb") as f:
        for video in pl_videos:
            pickle.dump(video, f, pickle.HIGHEST_PROTOCOL)

            if len(deleted_videos) != 0 and video.title == "Deleted video" and video not in deleted_videos:
                print(pl_videos[video.index].title + " has been deleted!")


def load_videos(pl_name: str) -> List[Video]:
    """
    Loads videos from a file.

    :param pl_name: The name of the playlist to load videos from
    :return: A list of all of the videos from the file
    """
    video_list = []
    file_name = "files/" + pl_name + ".pkl"

    with open(file_name, "rb") as f:
        while True:
            try:
                video_list.append(pickle.load(f))

            except EOFError:
                break

    return video_list
