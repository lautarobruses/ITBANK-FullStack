from django.shortcuts import render,redirect
from .forms import FormularioCalculadoraPrestamos

def calculadora_prestamos(request):
    pago_mensual = None

    if request.method == 'POST':
        formulario = FormularioCalculadoraPrestamos(request.POST)
        if formulario.is_valid():
            monto = formulario.cleaned_data['monto']
            tasa_interes = formulario.cleaned_data['tasa_interes'] / 100 / 12
            meses = formulario.cleaned_data['meses']
            # Fórmula para calcular el pago mensual de un préstamo
            pago_mensual = "{:.2f}".format(monto * tasa_interes * (1 + tasa_interes) ** meses / ((1 + tasa_interes) ** meses - 1))
            return redirect('prestamos')
    else:
        formulario = FormularioCalculadoraPrestamos()
    formulario = FormularioCalculadoraPrestamos() # Siempre devuelve un nuevo formulario para solicitudes GET
    return render(request, 'prestamos\prestamos.html', {'formulario': formulario, 'pago_mensual': pago_mensual})
