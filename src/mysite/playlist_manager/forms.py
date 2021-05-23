from django import forms


class PlaylistForm(forms.Form):
    pl_id = forms.CharField(label='Playlist ID:', max_length=100)
