from django.shortcuts import render
from .models import Song, Artist

def index (request):
    return render (request, 'reviewsiteapp/index.html')

def getSong(request):
    song_list = Song.objects.all()
    return render(request, 'reviewsiteapp/songs.html', {'song_list': song_list})


  