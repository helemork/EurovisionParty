from django.db import models
from django.contrib.auth.models import User

class Contest(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return str(self.year) + ' - ' + self.country

class Party(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    contest = models.ForeignKey(Contest)

    def __str__(self):
        return self.name

class UserParty(models.Model):
    user = models.ForeignKey(User)
    party = models.ForeignKey(Party)

    def get_user_party(user):
        try:
            return UserParty.objects.get(user=user).party
        except:
            return None


class Song(models.Model):
    order = models.PositiveIntegerField()
    hidden = models.BooleanField(default=False)
    country = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    contest = models.ForeignKey(Contest)

    def get_score(self):
        return 'you'

    def __str__(self):
       return self.country + ' - ' + self.title


class Vote(models.Model):
    song = models.ForeignKey(Song)
    user = models.ForeignKey(User)
    show = models.IntegerField()
    lightshow = models.IntegerField()
    outfit = models.IntegerField()
    dress = models.IntegerField()
    melody = models.IntegerField()
    voice = models.IntegerField()
    esc_factor = models.IntegerField()
    sexyness = models.IntegerField()
    douchebag = models.IntegerField()
    plagiarism = models.IntegerField()
    modulation = models.IntegerField()
    artbreak = models.IntegerField()
    dress_change = models.IntegerField()
    language = models.IntegerField()

    def __str__(self):
       return self.song.country + " vote by " + self.user.username

    def get_score(self):
        return self.show + self.lightshow + self.outfit + self.melody + \
                self.voice + self.esc_factor + self.sexyness + self.douchebag + self.modulation + \
                self.dress_change + self.language + self.artbreak + self.dress + self.plagiarism
