from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #r'^/*$'
    url(r'^$', views.index, name='index'),
    ]
