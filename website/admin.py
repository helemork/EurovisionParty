from django.contrib import admin
from .models import *

admin.site.register(Song)
admin.site.register(Vote)
admin.site.register(Party)
admin.site.register(UserParty)
