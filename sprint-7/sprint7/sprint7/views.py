from django.shortcuts import render

def home(request):
    accountFake = []  # Reemplaza esto con tus datos reales
    cardFake = []  # Reemplaza esto con tus datos reales

    return render(request, 'sprint7/home.html', {'accountFake': accountFake, 'cardFake': cardFake})
