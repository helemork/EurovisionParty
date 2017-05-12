from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^vote/([0-9]+)/$', views.vote, name='vote'),
    url(r'^userscoreboard/$', views.userscoreboard, name='userscoreboard'),
    url(r'^scoreboard/$', views.scoreboard_page, name='scoreboard'),
    url(r'^global_scoreboard/$', views.global_scoreboard_page, name='global_scoreboard'),
    url(r'^scoreboard/get/$', views.scoreboard, name='scoreboard_get'),

    url(r'^join_party/$', views.join_party, name='join_party'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
