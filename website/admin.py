from django.contrib import admin
from .models import *

class SongAdmin(admin.ModelAdmin):
    list_display = ('country', 'title', 'order', 'contest')
    list_filter = ('contest',)
    list_editable = ('order', )

admin.site.register(Song, SongAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'year')
    list_filter = ('user', 'song')

    def year(self, obj):
        return obj.song.contest.year

admin.site.register(Vote, VoteAdmin)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contest')
    list_filter = ('contest',)

admin.site.register(Party, PartyAdmin)

admin.site.register(UserParty)
admin.site.register(Contest)
