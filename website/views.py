from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
import django.contrib.auth
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html', {
        'form': UserCreationForm()
    })

@login_required
def songs(request):
    songs = Song.objects.all()
    return render(request,'songs.html',{
    'songs':songs,
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
