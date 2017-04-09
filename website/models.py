from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    order = models.PositiveIntegerField()
    country = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


    def __str__(self):
       return self.country

class Vote(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(User)
    show = models.IntegerField()
    lightshow = models.IntegerField()
    outfit = models.IntegerField()
    melody = models.IntegerField()
    voice = models.IntegerField()
    esc_factor = models.IntegerField()
    sexyness = models.IntegerField()
    douchebag = models.IntegerField()
    modulation = models.IntegerField()
    dress_change = models.IntegerField()
    language = models.IntegerField()

    def __str__(self):
       return self.song
