from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Cliente, Cuenta, CajaAhorro, CuentaCorriente, Tarjeta, TarjetaDebito, TarjetaCredito, MarcaTarjeta
                    
@login_required
def home(request):
    cliente = Cliente.objects.get(user_id=request.user.id)
    
    cuentas = Cuenta.objects.filter(customer_id=cliente.customer_id)
    cuentaParser(cuentas)
    tarjetas = Tarjeta.objects.filter(customer_id=cliente.customer_id)
    form = ContactForm()

    context = {
        'form': form,
        'nombreCompleto': f'{cliente.customer_name} {cliente.customer_surname}',
        'cuentas': cuentas,
        'tarjetas': tarjetas,
    }

    return render(request, 'base/home.html', context)

def comingSoon(request):
    return render(request, 'base/comingSoon.html')

@login_required
def sendMessage(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre", "")
            from_email = form.cleaned_data.get("email", "")
            mensaje = form.cleaned_data.get("mensaje", "")

            # Envía el correo electrónico
            subject = f'Nuevo mensaje de contacto de {nombre}'
            message = f'Nombre: {nombre}\nCorreo Electrónico: {from_email}\nMensaje: {mensaje}'
            to_email = 'contacto@nexusbank.com'

            send_mail(subject, message, from_email, [to_email])

            return redirect(reverse('home') + '?ok')

    return render(request, 'base/home.html', {'form': form})


def cuentaParser(cuentas):
    for cuenta in cuentas:
        caja_ahorro = CajaAhorro.objects.get(account=cuenta.account_id)
        if caja_ahorro:
            # Modifica los atributos de la Caja de Ahorro según sea necesario
            cuenta.title = 'Caja de ahorro'
            cuenta.cargo_mensual = caja_ahorro.cargo_mensual
        else:
            # Verifica si existe una Cuenta Corriente asociada a la cuenta
            cuenta_corriente = CuentaCorriente.objects.get(account=cuenta.account_id)
            if cuenta_corriente:
                cuenta.title = 'Cuenta corriente'
                cuenta.limite = cuenta_corriente.limite

        # Guarda los cambios en la base de datos
        cuenta.save()
