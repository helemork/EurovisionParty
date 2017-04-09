from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {
        'form': form
    })

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # This will login the user
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {
        'form': form
    })