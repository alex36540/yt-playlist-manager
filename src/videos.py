from dataclasses import dataclass
import private


@dataclass(unsafe_hash=True)
class Video:
    """Class that represents a video"""
    id: str
    name: str


def get_videos(api):
    videos = []
    pl_id = private.PLAYLIST_ID

    pl_items = api.get_playlist_items(playlist_id=pl_id, count=None, limit=50)

    for item in pl_items.items:
        videos.append(Video(
            item.snippet.resourceId.videoId, item.snippet.title # Create video object
        ))

    return videos
