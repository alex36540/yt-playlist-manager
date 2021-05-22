from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Video


def index(request):
    return HttpResponse("Eyyyy waddup jit")


def playlist(request):
    return HttpResponse("Playlisttt")
