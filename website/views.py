from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
import django.contrib.auth


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        print('post')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('valid')
            django.contrib.auth.login(request, form.get_user())
            return redirect('index')
        print('invalid')
    else:
        print('no post')
        form = AuthenticationForm()

    return render(request, 'login.html', {
        'form': form
    })

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