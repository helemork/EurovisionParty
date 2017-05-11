from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, reverse
import django.contrib.auth
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html', {})


@login_required
def songs(request):
    songs = Song.objects.filter(hidden=False).order_by('order')
    last_with_vote = -1
    counter = 0
    for song in songs:
        song.vote = None
        try:
            song.vote = Vote.objects.get(song = song, user = request.user)
            song.total = song.vote.get_score()
            last_with_vote = counter
        except:
            pass
        counter += 1

    # Show warning for skipped songs
    for i in range(last_with_vote):
        song = songs[i]
        if song.vote is None:
            song.warning = True

    return render(request,'songs.html',{
        'active': 'songs',
        'songs':songs,
    })


@login_required
def vote(request, song_id):
    song = Song.objects.get(id=song_id)

    vote = None
    # If vote already exists, get it!
    try:
        vote = Vote.objects.get(user=request.user, song=song)
    except Vote.DoesNotExist:
        pass

    if request.method == 'POST':
        if vote == None:
            form = VoteForm(request.POST)
        else:
            form = VoteForm(instance=vote, data=request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.song = song
            vote.user = request.user
            vote.save()
            return redirect(reverse('songs') + '#song_' + str(song.id))
        else:
            print('ERROR: Vote form not valid')
            print(form.errors)

    return render(request, 'vote.html', {
        'song': song,
        'vote': vote,
        'scores': [20, 15, '---', 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, '---', -5, -10, -20],
        'bonus_scores': [0, 5, 10, 15, 20, 25, 30],
        'minus_scores': [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -12, '---', -15, -20, -25, -30],
    })


@login_required
def scoreboard_page(request):
    return render(request, 'scoreboard_page.html', {
        'active': 'scoreboard',
    })


@login_required
def scoreboard(request):
    # Get all songs
    songs = Song.objects.filter(hidden=False)

    # For each song; get all votes and calculate score
    for song in songs:
        # Get votes for this song
        votes = Vote.objects.filter(song=song)
        song.has_votes = False
        total_score = 0
        if votes.count() > 0:
            song.has_votes = True
            highest_score = None
            lowest_score = None
            for vote in votes:
                score = vote.get_score()
                total_score += score
                if highest_score is None or score > highest_score :
                    highest_score = score
                    highest_name = vote.user.username
                if lowest_score is None or score < lowest_score :
                    lowest_score = score
                    lowest_name = vote.user.username

        song.score = total_score
        song.lowest_score = lowest_score
        song.highest_score = highest_score
        song.lowest_name = lowest_name
        song.highest_name = highest_name

    # Sort by score
    def song_to_key(song):
        return -song.score

    sorted_songs = sorted(songs, key=song_to_key)

    return render(request, 'scoreboard.html', {
        'songs': sorted_songs,
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
