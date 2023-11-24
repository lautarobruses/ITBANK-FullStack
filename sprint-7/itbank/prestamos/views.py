from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from base.models import Cliente, ClienteClassic, ClienteGold, ClienteBlack, Prestamo
from base.forms import ContactForm

from .forms import FormularioCalculadoraPrestamos, SolicitudPrestamoForm

@login_required
def prestamos(request):
    form = ContactForm()

    pago_mensual = None

    if request.method == 'POST':
        formulario = FormularioCalculadoraPrestamos(request.POST)
        if formulario.is_valid():
            monto = formulario.cleaned_data['monto']
            tasa_interes = formulario.cleaned_data['tasa_interes'] / 100 / 12
            meses = formulario.cleaned_data['meses']
            # Fórmula para calcular el pago mensual de un préstamo
            pago_mensual = "{:.2f}".format(monto * tasa_interes * (1 + tasa_interes) ** meses / ((1 + tasa_interes) ** meses - 1))
    else:
        formulario = FormularioCalculadoraPrestamos()
    formulario = FormularioCalculadoraPrestamos()

    return render(request, 'prestamos\prestamos.html', {'form': form, 'formulario': formulario, 'pago_mensual': pago_mensual})

@login_required
def solicitar_prestamo(request):
    cliente = Cliente.objects.get(user_id=request.user.id)

    if ClienteClassic.objects.filter(customer_id=cliente.customer_id).exists():
        max_loan_amount = 100000
    elif ClienteGold.objects.filter(customer_id=cliente.customer_id).exists():
        max_loan_amount = 300000
    elif ClienteBlack.objects.filter(customer_id=cliente.customer_id).exists():
        max_loan_amount = 500000
    else:
        max_loan_amount = 0

    if request.method == 'POST':
        form2 = SolicitudPrestamoForm(request.POST)
        if form2.is_valid():
            loan = Prestamo()
            loan.customer_id = cliente.customer_id
            loan.loan_type = form2.cleaned_data['tipo_prestamo']
            loan.loan_date = form2.cleaned_data['fecha_prestamo']
            loan.loan_total = min(form2.cleaned_data['monto_solicitado'], max_loan_amount)
            loan.save()
            return render(request, 'prestamos\prestamos.html', {'form2': form2, 'message': 'Tu solicitud de préstamo ha sido enviada.'})
    else:
        form2 = SolicitudPrestamoForm()

    return render(request, 'prestamos\prestamos.html', {'form2': form2, 'max_loan_amount': max_loan_amount})