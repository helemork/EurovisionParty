from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
import django.contrib.auth
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html', {})


@login_required
def songs(request):
    songs = Song.objects.all()
    return render(request,'songs.html',{
    'songs':songs,
    })


@login_required
def vote(request, song_id):
    song = Song.objects.get(id=song_id)

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.song = song
            form.user = request.user
            form.save()
            return redirect('songs')
        else:
            print('ERROR: Vote form not valid')
    else:
        # If vote already exists, get it!
        try:
            vote = Vote.objects.get(user=request.user, song=song)
        except Vote.DoesNotExist:
            vote = None

    return render(request, 'vote.html', {
        'song': song,
        'vote': vote,
    })


@login_required
def scoreboard(request):
    return render(request, 'scoreboard.html', {

    })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            django.contrib.auth.login(request, form.get_user())
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {
        'form': form
    })


def logout(request):
    django.contrib.auth.logout(request)
    return redirect('index')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            django.contrib.auth.login(request, user) # This will login the user
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {
        'form': form
    })
