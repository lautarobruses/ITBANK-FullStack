from django.shortcuts import render

# Create your views here.

def pagos(request):

    return render(request, 'pagos/pagos.html')

def servicios(request):
    
    return render(request, 'pagos/servicios.html')