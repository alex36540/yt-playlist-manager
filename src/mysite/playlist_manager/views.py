from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Video
from django.urls import reverse

import os
from dotenv import load_dotenv
import pyyoutube

load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
api = pyyoutube.Api(api_key=API_KEY)


def index(request):
    context = {}
    return render(request, 'playlist_manager/index.html', context)


def playlist(request, playlist_id):
    # if playlist already exists in database
    try:
        pl = Playlist.objects.get(id=playlist_id)

    except Playlist.DoesNotExist:
        # TODO raise 404 if playlist isn't found
        pl_title = api.get_playlist_by_id(playlist_id=playlist_id).items[0].snippet.title
        pl = Playlist(id=playlist_id, title=pl_title)
        pl.save()

        # get videos
        pl_items = api.get_playlist_items(playlist_id=playlist_id, count=None, limit=50)

        for item in pl_items.items:
            pl.video_set.create(
                id=item.snippet.resourceId.videoId,
                title=item.snippet.title,
                index=item.snippet.position
            )

    context = {
        'playlist': pl,
        'video_list': list(pl.video_set.order_by('index'))
    }

    return render(request, 'playlist_manager/playlist.html', context)
