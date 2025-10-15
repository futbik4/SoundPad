from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    cover_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.artist}"

SAMPLE_SONGS = [
    {
        'title': 'Bohemian Rhapsody',
        'artist': 'Queen',
        'genre': 'Rock',
        'duration': 354,
        'cover_url': 'https://example.com/queen.jpg'
    },
    {
        'title': 'Blinding Lights',
        'artist': 'The Weeknd',
        'genre': 'Pop',
        'duration': 200,
        'cover_url': 'https://example.com/weeknd.jpg'
    },
    {
        'title': 'Shape of You',
        'artist': 'Ed Sheeran',
        'genre': 'Pop',
        'duration': 233,
        'cover_url': 'https://example.com/edsheeran.jpg'
    },
]

GENRES = ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop', 'Electronic']