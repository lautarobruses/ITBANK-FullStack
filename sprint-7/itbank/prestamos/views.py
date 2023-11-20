from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from base.models import ClienteClassic, ClienteGold, ClienteBlack, Prestamo
from .forms import FormularioCalculadoraPrestamos, SolicitudPrestamoForm
# @login_required
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


# def solicitar_prestamo(request):
#     user = request.user
#     if ClienteClassic.objects.filter(customer_id=user.id).exists():
#         max_loan_amount = 100000
#     elif ClienteGold.objects.filter(customer_id=user.id).exists():
#         max_loan_amount = 300000
#     elif ClienteBlack.objects.filter(customer_id=user.id).exists():
#         max_loan_amount = 500000
#     else:
#         max_loan_amount = 0  # o cualquier valor predeterminado

#     if request.method == 'POST':
#         form = SolicitudPrestamoForm(request.POST)
#         if form.is_valid():
#             loan = Prestamo()
#             loan.user = user
#             loan.loan_type = form.cleaned_data['tipo_prestamo']
#             loan.loan_date = form.cleaned_data['fecha_prestamo']
#             loan.loan_total = min(form.cleaned_data['monto_solicitado'], max_loan_amount)
#             loan.save()
#     else:
#         form = SolicitudPrestamoForm()

#     return render(request, 'prestamos\prestamos.html', {'form': form})
