from django.contrib import admin
from .models import Artist, Song, Gerne, Rating


admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Gerne)
admin.site.register(Rating)