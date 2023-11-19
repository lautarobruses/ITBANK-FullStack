from django.shortcuts import render

# Create your views here.

def transferencias(request):

    return render(request, 'transferencias/transferencias.html')