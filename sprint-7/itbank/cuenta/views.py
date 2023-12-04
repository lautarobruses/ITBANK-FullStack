from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from base.models import Cliente, Tarjeta, TarjetaDebito, Cuenta, CajaAhorro, Sucursal, TipoMoneda

import random
from faker import Faker #pip install faker
from datetime import datetime

# Create your views here.

def register(request):
    form = RegisterForm

    if(request.method == 'POST'):
        form = form(request.POST)
        if form.is_valid():
            try:
                name = request.POST.get('name_surname', "")

                if name.count(' ') == 1:
                    password = request.POST.get('password', "")
                    confirm_password = request.POST.get('confirm_password', "")

                    if password == confirm_password:
                        mail = request.POST.get('mail', "")
                        phone = request.POST.get('phone', "")
                        dni = request.POST.get('dni', "")
                        first_name, last_name = name.split(" ")

                        username = first_name.lower() + '.' + last_name.lower()
                        branch_id = random.randint( 1, Sucursal.objects.count())

                        user = User(
                            username = username,
                            email = mail,
                        )

                        user.set_password(password)

                        user.save()

                        cliente = Cliente(
                            customer_name = first_name,
                            customer_surname = last_name,
                            customer_dni = dni,
                            telefono = phone,
                            branch = branch_id,
                            user = user.id,
                        )

                        cliente.save()

                        cvv = random.randint(100, 999)

                        fecha_actual = datetime.now()
                        fecha_otorgamiento = fecha_actual.strftime("%Y/%m/%d")
                        fecha_expiracion = (fecha_actual.replace( year = fecha_actual.year + 10 )).strftime("%Y/%m/%d")

                        marca_tarjeta = random.randint(1, 3)

                        tarjeta = Tarjeta(
                            tarjeta_cvv = cvv,
                            tarjeta_fecha_otorgamiento = fecha_otorgamiento,
                            tarjeta_fecha_expiracion = fecha_expiracion,
                            tarjeta_nombre_propietario = first_name.title() + ' ' + last_name.title(),
                            customer_id = cliente.customer_id,
                            marca_tarjeta_id = marca_tarjeta,
                        )
                        
                        tarjeta.save()
                        
                        tipo_moneda = random.randint( 0, TipoMoneda.objects.count() - 1)

                        fake = Faker()

                        while True:
                            iban = fake.iban()
                            if not Cuenta.objects.filter(iban=iban).exists():
                                break
                        
                        cuenta = Cuenta(
                            balance = 0,
                            iban = iban,
                            customer_id = cliente.customer_id,
                            tipo_moneda_id = tipo_moneda,
                        )

                        cuenta.save()
                        
                        caja_ahorro = CajaAhorro(
                            account_id = cuenta.account_id,
                            cargo_mensual = 0,
                        )

                        caja_ahorro.save()

                        tarjeta_debito = TarjetaDebito(
                            tarjeta_numero = tarjeta,
                            account_id = cuenta.account_id,
                        )

                        tarjeta_debito.save()

                        return redirect('../login', {'form': form})
                    else:
                        return render(request, 'cuenta/register.html', {'form': form, 'error': "Las contraseñas no coinciden. Inténtalo de nuevo."})
                else:
                    return render(request, 'cuenta/register.html', {'form': form, 'errorName': "Escribe tu nombre y apellido separado con un espacio."})
            except:
                return render(request, 'cuenta/register.html', {'form': form, 'errorName': "El nombre de usuario ya existe."})
        else:
            print("no soy valido")

    return render(request, 'cuenta/register.html', {'form': form})