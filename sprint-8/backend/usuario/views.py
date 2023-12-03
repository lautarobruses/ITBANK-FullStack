from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from cuenta.models import Cuenta

from prestamos.models import Prestamo

from .serializers import UserSerializer, ClienteSerializer, UserLoginSerializer
from .models import Cliente


# Create your views here.

class UserList(APIView):
    def post(self, request, **kwards):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
class UserDetailsSelf(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwards):
        user = User.objects.filter(id=self.request.user.id).first()
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