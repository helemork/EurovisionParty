from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request, 'registration.html', {
        'form': UserCreationForm()
    })