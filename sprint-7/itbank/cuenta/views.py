from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
# from base.models import Cliente

# Create your views here.

def register(request):
    form = RegisterForm

    if(request.method == 'POST'):
        form = form(request.POST)
        if form.is_valid():
            try:
                username = request.POST.get('name_surname', "")

                if username.count(' ') == 1:
                    password = request.POST.get('password', "")
                    confirm_password = request.POST.get('confirm_password', "")

                    if password == confirm_password:
                        mail = request.POST.get('mail', "")

                        first_name, last_name = username.split(" ")
                        username = first_name.lower() + '.' + last_name.lower()

                        user = User( username=username, email=mail, )

                        user.set_password(password)

                        user.save()

                        return redirect('../login', {'form': form})
                    else:
                        return render(request, 'cuenta/register.html', {'form': form, 'error': "Las contraseñas no coinciden. Inténtalo de nuevo."})
                else:
                    return render(request, 'cuenta/register.html', {'form': form, 'errorName': "Escribe tu nombre y apellido separado con un espacio."})
            except:
                return render(request, 'cuenta/register.html', {'form': form, 'errorName': "El nombre de usuario ya existe."})
        else:
            print("no soy valido")

    return render(request, 'cuenta/register.html', {'form': form})