from django.shortcuts import render, redirect
from .forms import ServicioForm
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

@login_required
def pagos(request):
    form = ServicioForm()
    servicios = []

    if 'servicios' in request.session:
        servicios = request.session['servicios']

    context = {
        "form": form,
        "servicios": servicios
    }

    return render(request, 'pagos/pagos.html', context)

@login_required
def servicios(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            request.session['servicios'] = form.cleaned_data
            return redirect('pagos')
    else:
        form = ServicioForm()

    context = {
        "form": form
    }

    return render(request, 'pagos/servicios.html', context)