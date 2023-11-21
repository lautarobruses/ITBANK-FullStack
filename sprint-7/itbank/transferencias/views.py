from django.shortcuts import render, redirect, get_object_or_404
from base.models import Cliente, Cuenta
from .models import Transferencia
from base.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency
from django.db import transaction

@login_required
def transferencias(request):
    form = ContactForm()
    # Obtener el cliente asociado al usuario actual
    cliente = Cliente.objects.get(user_id=request.user.id)
    saldo = Cuenta.objects.get(account_id=request.user.id)
    balance = saldo.balance
    codigo_moneda = '$'

    saldo_formateado = format_currency(balance / 100, codigo_moneda, locale='es_AR')
    if balance > 0:
        mensaje = f'Saldo: {saldo_formateado}'
    else:
        messages.error(request, 'Saldo insuficiente para realizar transferencias. ')
        mensaje = f'Saldo: {saldo_formateado} hay que ponerse las pilas con las cuentas'
    
    context = {
        'form': form,
        'nombreUser': cliente.customer_name,
        'saldo': f'{mensaje}',
        'balance': balance,
    }

    return render(request, 'transferencias/transferencias.html', context)

    

@login_required
# def accion_transferir(request):
#     # if request.method == 'POST':
#     # cuenta_origen_id = request.POST.get('cuenta_origen')
#     # cuenta_destino_id = request.POST.get('cuenta_destino')
#     # monto = request.POST.get('monto')

#     # cuenta_origen = CuentaBancaria.objects.get(id=cuenta_origen_id)
#     # cuenta_destino = CuentaBancaria.objects.get(id=cuenta_destino_id)

#         # return redirect('transferencias/transferencias.html')
    
#     # cuentas = CuentaBancaria.objects.filter(usuario=request.user)
#     cliente = Cliente.objects.get(user_id=request.user.id)
#     context = {
#         'nombreUser': f'{cliente.customer_name}',
#     }


#     return render(request, 'transferencias/transferir.html', context)


def accion_transferir(request):
    if request.method == 'POST':
        dni_destinatario = request.POST.get('dni')
        customer_name_destinatario = request.POST.get('customer_name')
        monto = float(request.POST.get('monto'))

        try:
            with transaction.atomic():
                destinatario = Cuenta.objects.select_for_update().get(dni=dni_destinatario, customer_name=customer_name_destinatario)
                cuenta_origen_id = request.POST.get('cuenta_origen_id')
                cuenta_origen = Cuenta.objects.select_for_update().get(id=cuenta_origen_id)

                if cuenta_origen.balance >= monto:
                    # Realizar la transferencia
                    cuenta_origen.balance -= monto
                    destinatario.balance += monto

                    cuenta_origen.save()
                    destinatario.save()

                    # Guardar la información de la transferencia en la base de datos
                    Transferencia.objects.create(
                        dni_destinatario=dni_destinatario,
                        customer_name_destinatario=customer_name_destinatario,
                        monto=monto
                    )

                    messages.success(request, 'Transferencia realizada con éxito')
                    return render(request, 'transferencias/success.html')  # Redirigir a la página de éxito
                else:
                    messages.error(request, 'No tienes fondos suficientes para realizar la transferencia')
                    return render(request, 'transferencias/error.html')  # Redirigir a la página de error
        except Cuenta.DoesNotExist:
            messages.error(request, 'El destinatario no existe.')
            return render(request, 'transferencias/error.html')  # Redirigir a la página de error

    cliente = get_object_or_404(Cliente, user=request.user.id)
    cuentas = Cuenta.objects.filter(customer=cliente)
    context = {
        'nombreUser': f'{cliente.customer_name}',
        'cuentas': cuentas,
    }

    return render(request, 'transferencias/transferir.html', context)