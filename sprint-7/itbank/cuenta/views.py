from django.shortcuts import render
from .forms import LoginForm, RegisterForm

# Create your views here.

def login(request):
    return render(request, 'cuenta/login.html', {'form': LoginForm})

def register(request):
    return render(request, 'cuenta/register.html', {'form': RegisterForm})