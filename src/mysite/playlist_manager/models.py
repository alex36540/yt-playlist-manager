from django.db import models

class Playlist(models.Model):
    id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    # TODO add videos field


class Video(models.Model):
    id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    index = models.IntegerField()
