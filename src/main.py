import pyyoutube
import private

API_KEY = private.API_KEY
api = pyyoutube.Api(api_key=API_KEY)


def get_videos():
    videos = []
    pl_id = private.PLAYLIST_ID

    pl_items = api.get_playlist_items(playlist_id=pl_id, count=None, limit=50)

    for item in pl_items.items:
        videos.append({item.snippet.resourceId.videoId: item.snippet.title})  # ID: title

    return videos


def main() -> None:
    print(get_videos())


if __name__ == '__main__':
    main()
