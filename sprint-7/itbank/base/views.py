from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Cliente, Cuenta, CajaAhorro, CuentaCorriente

@login_required
def home(request):
    cliente = Cliente.objects.get(user_id=request.user.id)
    
    accountFake = []  # Reemplaza esto con tus datos reales
    cardFake = []  # Reemplaza esto con tus datos reales
    form = ContactForm()

    context = {
        'form': form,
        'nombreCompleto': f'{cliente.customer_name} {cliente.customer_surname}',
        'accountFake': accountFake,
        'cardFake': cardFake
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
