from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from cuenta.models import Cuenta, TipoMoneda
from sucursal.models import Sucursal
from prestamos.models import Prestamo
from cuenta.serializers import CuentaSerializer, CuentaCorrienteSerializer
from tarjetas.serializers import TarjetaSerializer, TarjetaDebitoSerializer

from .serializers import UserSerializer, ClienteSerializer, UserLoginSerializer
from .models import Cliente

import random
from faker import Faker #pip install faker
from datetime import datetime
# Create your views here.

class UserList(APIView):
    def post(self, request, **kwards):
        if self.request.data.get('name_surname').count(' ') == 1:
            if(self.request.data.get('password') == self.request.data.get('confirm_password')):
                first_name, last_name = self.request.data.get('name_surname').split(" ")
                # username = first_name.lower() + '.' + last_name.lower()

                user_data = {
                    "username": self.request.data.get('mail'),
                    "email": self.request.data.get('mail'),
                    "password": self.request.data.get('password'),
                }

                serializer_user = UserSerializer(data=user_data)

                if serializer_user.is_valid():
                    user = serializer_user.save()

                    cliente_data = {
                        "customer_name": first_name,
                        "customer_surname": last_name,
                        "customer_dni": self.request.data.get('dni'),
                        "telefono": self.request.data.get('phone'),
                        "branch": random.randint( 1, Sucursal.objects.count()),
                        "user": user.id,
                    }

                    serializer_cliente = ClienteSerializer(data=cliente_data)

                    if serializer_cliente.is_valid():
                        cliente = serializer_cliente.save()

                        cvv = random.randint(100, 999)
                        fecha_actual = datetime.now()
                        fecha_otorgamiento = fecha_actual.strftime("%Y/%m/%d")
                        fecha_expiracion = (fecha_actual.replace( year = fecha_actual.year + 10 )).strftime("%Y/%m/%d")
                        marca_tarjeta = random.randint(1, 3)

                        tarjeta_data = {
                            "tarjeta_cvv": cvv,
                            "tarjeta_fecha_otorgamiento": fecha_otorgamiento,
                            "tarjeta_fecha_expiracion": fecha_expiracion,
                            "tarjeta_nombre_propietario": first_name.title() + ' ' + last_name.title(),
                            "customer": cliente.customer_id,
                            "marca_tarjeta": marca_tarjeta,
                        }

                        serializer_tarjeta = TarjetaSerializer(data=tarjeta_data)

                        serializer_tarjeta.is_valid()
                        tarjeta = serializer_tarjeta.save()
                    
                        fake = Faker()
                        tipo_moneda = random.randint( 0, TipoMoneda.objects.count() - 1)

                        while True:
                            iban = fake.iban()
                            if not Cuenta.objects.filter(iban=iban).exists():
                                break
                        
                        cuenta_data = {
                            "balance": 0,
                            "iban": iban,
                            "customer": cliente.customer_id,
                            "tipo_moneda": tipo_moneda,
                        }

                        serializer_cuenta = CuentaSerializer(data=cuenta_data)

                        serializer_cuenta.is_valid()
                        cuenta = serializer_cuenta.save()

                        cuenta_corriente_data = {
                            "account": cuenta.account_id,
                            "limite": 0,
                        }

                        serializer_cuenta_corriente = CuentaCorrienteSerializer(data=cuenta_corriente_data)

                        serializer_cuenta_corriente.is_valid()
                        serializer_cuenta_corriente.save()

                        tarjeta_debito_data = {
                            "tarjeta_numero": tarjeta.tarjeta_numero,
                            "account": cuenta.account_id,
                        }

                        serializer_tarjeta_debito = TarjetaDebitoSerializer(data=tarjeta_debito_data)
                        
                        serializer_tarjeta_debito.is_valid()
                        serializer_tarjeta_debito.save()

                        return Response(serializer_user.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Las contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Escribe tu nombre y apellido separado por un espacio.'}, status=status.HTTP_400_BAD_REQUEST)

    
class UserDetails(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # El usuario no es válido
                return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Datos de inicio de sesión no válidos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Api para que un usuario obtenga sus propios datos (primera api de la segunda problematica)
class ClienteDetailsSelf(APIView):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwards):
        user = User.objects.get(id=self.request.user.id)

        if user is not None:
            cliente = Cliente.objects.get(user_id=user.id)
            serializer = ClienteSerializer(cliente)

            if cliente is not None:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'el usuario no esta asociado a ningun cliente'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'el usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)

#Api para que un usuario obtenga sus propios datos (primera api de la segunda problematica)
class UserDetailsSelf(APIView):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwards):
        user = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(user)

        if user is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'usuario sin logear'}, status=status.HTTP_400_BAD_REQUEST)

# Api para OBTENER SALDO DE CUENTA DE UN CLIENTE

class ObtenerSaldo(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        try:
            cliente = Cliente.objects.get(user=self.request.user)
            cuenta = Cuenta.objects.get(customer=cliente)

            data = {
                'balance': cuenta.balance,
                'iban': cuenta.iban,
                'tipo_moneda': cuenta.tipo_moneda.moneda_nombre, 
            }

            return Response(data, status=status.HTTP_200_OK)
        except Cuenta.DoesNotExist:
            return Response({'error': 'El cliente no tiene una cuenta asociada.'}, status=status.HTTP_400_BAD_REQUEST)
        
# Api para OBTENER MONTO DE PRESTAMOS DE UN CLIENTE

class ObtenerMontoPrestamos(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        try:
            cliente = Cliente.objects.get(user=self.request.user)
            prestamos = Prestamo.objects.filter(customer=cliente)

            data = {
                'prestamos': [{'loan_type': p.loan_type, 'loan_date': p.loan_date, 'loan_total': p.loan_total} for p in prestamos],
            }

            return Response(data, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({'error': 'El cliente no existe en la base de datos.'}, status=status.HTTP_400_BAD_REQUEST)
        except Prestamo.DoesNotExist:
            return Response({'error': 'El cliente no tiene préstamos asociados.'}, status=status.HTTP_400_BAD_REQUEST)