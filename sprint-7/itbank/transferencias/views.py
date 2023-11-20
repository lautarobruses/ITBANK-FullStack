from django.shortcuts import render, redirect
from .models import CuentaBancaria, Transferencias


# Create your views here.

# @login_required
def transferencias(request):
    
    transferencia = Transferencias.objects.filter(origen__usuario=request.user)

    return render(request, 'transferencias/transferencias.html', {'transferencias' : transferencia})

# @login_required
def accion_transferir(request):
    # if request.method == 'POST':
    # cuenta_origen_id = request.POST.get('cuenta_origen')
    # cuenta_destino_id = request.POST.get('cuenta_destino')
    # monto = request.POST.get('monto')

    # cuenta_origen = CuentaBancaria.objects.get(id=cuenta_origen_id)
    # cuenta_destino = CuentaBancaria.objects.get(id=cuenta_destino_id)

        # return redirect('transferencias/transferencias.html')
    
    # cuentas = CuentaBancaria.objects.filter(usuario=request.user)

    return render(request, 'transferencias/transferir.html')

