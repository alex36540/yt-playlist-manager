from django.urls import path
from . import views


app_name = 'playlist_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('playlist/<str:playlist_id>/', views.playlist, name='playlist')
]
