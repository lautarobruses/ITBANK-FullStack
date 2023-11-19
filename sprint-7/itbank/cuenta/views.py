from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'cuenta/login.html', {'form': LoginForm})

def register(request):
    if(request.method == 'GET'):
        return render(request, 'cuenta/register.html', {'form': RegisterForm})
    else:
        try:
            user = User.objects.create_user(
                username = request.POST['']
            )
        except:
            print("hola")