from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PlaylistForm, SettingsForm
from .models import SAMPLE_SONGS, GENRES
import json
from datetime import datetime, timedelta
from .translations import TRANSLATIONS

def create_playlist(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')
    
    song_choices = [(i, song['title']) for i, song in enumerate(SAMPLE_SONGS)]
    
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        form.fields['songs'].choices = song_choices
        
        if form.is_valid():
            playlist_data = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
                'is_public': form.cleaned_data['is_public'],
                'songs': form.cleaned_data['songs'],
                'created_at': str(datetime.now())
            }

            response = redirect('success')
            playlists = request.COOKIES.get('playlists', '[]')
            playlists_list = json.loads(playlists)
            playlists_list.append(playlist_data)
            response.set_cookie('playlists', json.dumps(playlists_list), max_age=365*24*60*60)
            
            return response
    else:
        form = PlaylistForm()
        form.fields['songs'].choices = song_choices
    
    context = {
        'form': form,
        'songs': SAMPLE_SONGS,
        'current_theme': theme,
        'current_language': language,
        't': TRANSLATIONS[language],
    }
    return render(request, 'playlists/create_playlist.html', context)

def success(request):
    theme = request.COOKIES.get('theme', 'light')
    visit_history = request.COOKIES.get('visit_history', '[]')
    history_list = json.loads(visit_history)
    language = request.COOKIES.get('language', 'en')

    context = {
        'current_theme': theme,
        'visit_history': history_list,
        't': TRANSLATIONS[language],
    }
    return render(request, 'playlists/success.html', context)

def clear_cookies(request):
    response = redirect('create_playlist')
    response.delete_cookie('theme')
    response.delete_cookie('language')
    response.delete_cookie('last_visited')
    response.delete_cookie('visit_history')
    response.delete_cookie('playlists')
    return response

def settings_page(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')
    
    if request.method == 'POST':
        form = SettingsForm(request.POST)  
        if form.is_valid():
            response = redirect('settings')
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=365*24*60*60)
            response.set_cookie('language', form.cleaned_data['language'], max_age=365*24*60*60)
            return response
    else:
        initial_data = {'theme': theme, 'language': language}
        form = SettingsForm(initial=initial_data) 
    
    context = {
        'form': form,
        'current_theme': theme,
        'current_language': language,
        't': TRANSLATIONS[language],  
    }
    return render(request, 'playlists/settings.html', context)

def my_playlists(request):
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'en')
    
    playlists_json = request.COOKIES.get('playlists', '[]')
    playlists = json.loads(playlists_json)
    
    context = {
        'playlists': playlists,
        'current_theme': theme,
        'current_language': language,
        't': TRANSLATIONS[language],
    }
    return render(request, 'playlists/my_playlists.html', context)