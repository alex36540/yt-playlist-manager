from typing import List
from video import Video
import pickle
from os import path
from pyyoutube import Api


class Playlist:
    api: Api
    id: str
    name: str
    videos: List[Video]
    size: int

    def __init__(self, api: Api, pl_id: str):
        self.api = api
        self.id = pl_id
        self.name = self.api.get_playlist_by_id(playlist_id=self.id).items[0].playlist.snippet.title

        self.videos = []
        self.size = 0

    def get_videos(self) -> None:
        """
        Gets all of the videos from a playlist.

        :return: None
        """
        pl_items = self.api.get_playlist_items(playlist_id=self.id, count=None, limit=50)

        for item in pl_items.items:
            self.videos.append(Video(
                item.snippet.resourceId.videoId, item.snippet.title, item.snippet.position  # Create video object
            ))

    def load(self) -> None:
        """
        Loads playlist from a file.

        :return: None
        """
        file_name = "files/" + self.name + ".pkl"

        with open(file_name, "rb") as f:
            while True:
                try:
                    self.videos.append(pickle.load(f))
                    self.size += 1

                except EOFError:
                    break

    def write(self) -> None:
        """
        Writes a playlist to a file. Also checks for new deletions so that the user can be notified of them.

        :return: None
        """
        file_name = "files/" + self.name + ".pkl"
        deleted_videos = set()

        # if the file already exists, check for new video deletions
        if path.exists(file_name):
            for video in self.videos:
                if video.title == "Deleted video":
                    deleted_videos.add(video)

        with open(file_name, "wb") as f:
            for video in self.videos:
                pickle.dump(video, f, pickle.HIGHEST_PROTOCOL)

                if len(deleted_videos) != 0 and video.title == "Deleted video" and video not in deleted_videos:
                    print(self.videos[video.index].title + " has been deleted!")


