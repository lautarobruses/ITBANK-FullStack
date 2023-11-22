from django.shortcuts import render, get_object_or_404
from base.models import Cliente, Cuenta
from base.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency
from .forms import TransferForm
from .models import CustomUser

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
        form = TransferForm(request.POST)
        if form.is_valid():
            beneficiario_username = form.cleaned_data['beneficiario']
            monto = form.cleaned_data['monto']

            beneficiario = get_object_or_404(CustomUser, username=beneficiario_username)
            remitente = request.user

            # Realiza la transferencia
            remitente.cuenta.balance -= monto
            beneficiario.cuenta.balance += monto

            remitente.cuenta.save()
            beneficiario.cuenta.save()

            return render(request, 'transferencia_exitosa.html', {'monto': monto, 'beneficiario': beneficiario_username})

    else:
        form = TransferForm()


    return render(request, 'transferencias/transferir.html', {'form': form})