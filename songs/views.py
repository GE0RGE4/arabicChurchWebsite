from django.shortcuts import render, get_object_or_404
from .models import Song
from django.db.models import Q
import re

# Welcome page
def welcome(request):
    return render(request, 'songs/welcome.html')

# Song list with search
def song_list(request):
    keyword_q = request.GET.get('keywords', '').strip()
    lyrics_q = request.GET.get('lyrics', '').strip()

    songs = Song.objects.all()

    if keyword_q:
        songs = songs.filter(
            Q(anthropological_keywords__icontains=keyword_q) |
            Q(theological_keywords__icontains=keyword_q)
        )

    if lyrics_q:
        songs = songs.filter(lyrics__icontains=lyrics_q)

    return render(request, 'songs/song_list.html', {
        'songs': songs,
        'keyword_q': keyword_q,
        'lyrics_q': lyrics_q,
    })

# Song detail page
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    search_term = request.GET.get('lyrics', '').strip()

    lyrics = song.lyrics
    if search_term:
        pattern = re.escape(search_term)
        lyrics = re.sub(pattern, r'<mark>\g<0></mark>', lyrics, flags=re.IGNORECASE)

    return render(request, 'songs/song_detail.html', {
        'song': song,
        'lyrics': lyrics,
        'search_term': search_term,
    })
