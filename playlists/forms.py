from django import forms

class PlaylistForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='',  
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        required=False,
        label='',  
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    is_public = forms.BooleanField(
        required=False,
        label='',  
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    songs = forms.MultipleChoiceField(
        required=False,
        label='',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'song-checkbox'}),
        choices=[]  
    )
class SettingsForm(forms.Form):
    PLAYLIST_THEMES = [
        ('light', 'Светлая тема'),
        ('dark', 'Темная тема'),
    ]
    
    LANGUAGES = [
        ('en', 'English'),
        ('ru', 'Русский'),
    ]
    
    theme = forms.ChoiceField(
        choices=PLAYLIST_THEMES,
        label='Тема оформления',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    language = forms.ChoiceField(
        choices=LANGUAGES,
        label='Язык интерфейса',
        widget=forms.Select(attrs={'class': 'form-control'})
    )