from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Prestamo
from cuenta.models import Cuenta
from usuario.models import Cliente
from .serializers import PrestamoSerializer
# Create your views here.

class PrestamosList(APIView):
    def get(self, request, pk, **kwards):
        prestamo = Prestamo.objects.filter(branch_id=pk)
        serializer = PrestamoSerializer(prestamo, many=True)

        if prestamo is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ''}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, **kwards):
        user = User.objects.filter(id=pk).first()

        if user is not None:
            cliente_user = Cliente.objects.filter(user=pk).first()
            if cliente_user is not None and cliente_user != []:
                cuenta_user = Cuenta.objects.filter(customer=cliente_user.customer_id).first()
                if cuenta_user is not None:
                    if cuenta_user.balance >= self.request.data.get('loan_total'):
                        prestamo_data = {
                            "loan_type": self.request.data.get('loan_type'),
                            "loan_total": self.request.data.get('loan_total'),
                            "customer": cliente_user.customer_id
                        }

                        serializer = PrestamoSerializer(data=prestamo_data)
                        
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({'error': 'saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'el usuario no tiene una cuenta asociada.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                    return Response({'error': 'el usuario no tiene un cliente asociado.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'el usuario no existe.'}, status=status.HTTP_400_BAD_REQUEST)