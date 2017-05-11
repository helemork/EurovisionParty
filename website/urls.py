from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^vote/([0-9]+)/$', views.vote, name='vote'),
    url(r'^userscoreboard/$', views.userscoreboard, name='userscoreboard'),
    url(r'^scoreboard/$', views.scoreboard_page, name='scoreboard'),
    url(r'^scoreboard/get/$', views.scoreboard, name='scoreboard_get'),

    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
