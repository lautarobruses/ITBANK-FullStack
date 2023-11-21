from django.shortcuts import render
from base.forms import ContactForm

def pagos(request):
    form = ContactForm()

    context = {
        "form": form
    }

    return render(request, 'pagos/pagos.html', context)

def servicios(request):
    
    return render(request, 'pagos/servicios.html')