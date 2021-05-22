from django.db import models


class Playlist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    # to get all videos, method is <Playlist>.video_set.all(), or video_set.create( VIDEO FIELDS )
    # this is also where you add methods

    def __str__(self):
        return self.name


class Video(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    index = models.IntegerField()

    def __str__(self):
        return str(self.index) + " " + str(self.title)
