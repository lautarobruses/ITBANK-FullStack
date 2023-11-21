from django.shortcuts import render
from base.forms import ContactForm

def pagos(request):
    form = ContactForm()
    return render(request, 'pagos/pagos.html', form)

def servicios(request):
    
    return render(request, 'pagos/servicios.html')