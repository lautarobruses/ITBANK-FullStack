from django.shortcuts import render, redirect, get_object_or_404
from base.models import Cliente, Cuenta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency
from django.db import transaction
# Create your views here. 

@login_required
def transferencias(request):


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
        cuenta_origen_id = request.POST.get('cuenta_origen')
        cuenta_destino_id = request.POST.get('cuenta_destino')
        monto = float(request.POST.get('monto'))

        try:
            with transaction.atomic():
                cuenta_origen = Cuenta.objects.select_for_update().get(id=cuenta_origen_id)
                cuenta_destino = Cuenta.objects.select_for_update().get(id=cuenta_destino_id)

                if cuenta_origen.balance >= monto:
                    cuenta_origen.balance -= monto
                    cuenta_destino.balance += monto

                    cuenta_origen.save()
                    cuenta_destino.save()

                    messages.success(request, 'Transferencia realizada con éxito')
                else:
                    messages.error(request, 'No tienes fondos suficientes para realizar la transferencia')
        except Cuenta.DoesNotExist:
            messages.error(request, 'Las cuentas seleccionadas no existen.')

    cliente = get_object_or_404(Cliente, user=request.user.id)  # Usar request.user.id en lugar de request.user
    cuentas = Cuenta.objects.filter(customer=cliente)
    context = {
        'nombreUser': f'{cliente.customer_name}',
        'cuentas': cuentas,
    }

    return render(request, 'transferencias/transferir.html', context)
