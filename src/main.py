import pyyoutube
import private
import videos

API_KEY = private.API_KEY
api = pyyoutube.Api(api_key=API_KEY)


def main() -> None:
    print(videos.get_videos(api))


if __name__ == '__main__':
    main()
