from django.shortcuts import render, redirect
from base.models import Cliente, Cuenta
from base.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency


# Create your views here. 

@login_required
def transferencias(request):
<<<<<<< HEAD
    form = ContactForm()
=======


>>>>>>> e46ce97a5fc439b8064be73118ba296314937e17
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
def accion_transferir(request):
    # if request.method == 'POST':
    # cuenta_origen_id = request.POST.get('cuenta_origen')
    # cuenta_destino_id = request.POST.get('cuenta_destino')
    # monto = request.POST.get('monto')

    # cuenta_origen = CuentaBancaria.objects.get(id=cuenta_origen_id)
    # cuenta_destino = CuentaBancaria.objects.get(id=cuenta_destino_id)

        # return redirect('transferencias/transferencias.html')
    
    # cuentas = CuentaBancaria.objects.filter(usuario=request.user)
    cliente = Cliente.objects.get(user_id=request.user.id)
    context = {
        'nombreUser': f'{cliente.customer_name}',
    }


    return render(request, 'transferencias/transferir.html', context)

