from django.shortcuts import render

# Create your views here.
def home(request):
    accountFake = []  # Reemplaza esto con tus datos reales
    cardFake = []  # Reemplaza esto con tus datos reales

    return render(request, 'base/home.html', {'accountFake': accountFake, 'cardFake': cardFake})