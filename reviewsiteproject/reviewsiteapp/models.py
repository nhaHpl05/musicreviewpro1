from django.db import models
from django.contrib.auth.models import User
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation


class Artist(models.Model):
    artist_name = models.CharField(max_length=255)

    def _str_(self):
        return self.artist_name


class Gerne(models.Model):
    gerne = models.CharField(max_length = 250)  
    
    def _str_(self):
        return self.gerne      


class Rating(models.Model):
    bar = models.CharField(max_length=100)
    ratings = GenericRelation(Rating, related_query_name='rating')
Rating.objects.filter(ratings__isnull=False).order_by('ratings__average')


class Song(models.Model):
    song_title = models.CharField(max_length = 250)
    date_release = models.DateField()
    artist = models.ForeignKey(Artist, on_delete = models.DO_NOTHING)
    gerne_type = models.ForeignKey(Gerne, on_delete = models.DO_NOTHING)
    
    def __str__(self):
        return self.song_title
    
    class Meta:
        db_table='song'
        verbose_name_plural='songs'

 
 
        
