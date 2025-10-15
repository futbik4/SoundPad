from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_playlist, name='create_playlist'),
    path('success/', views.success, name='success'),
    path('clear-cookies/', views.clear_cookies, name='clear_cookies'),
    path('settings/', views.settings_page, name='settings'),
    path('my-playlists/', views.my_playlists, name='my_playlists'),
]