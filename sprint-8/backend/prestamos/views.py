from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions

from cuenta.models import Cuenta
from usuario.models import Cliente
from .permissions import IsEmploye
from .models import Prestamo
from .serializers import PrestamoSerializer
# Create your views here.

class PrestamosList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsEmploye]

    def get(self, request, pk, **kwards):
        prestamo = Prestamo.objects.filter(branch_id=pk)
        serializer = PrestamoSerializer(prestamo, many=True)

        if prestamo is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ''}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk, **kwards):
        user = User.objects.get(id=pk)

        if user is not None:
            cliente_user = Cliente.objects.get(user=pk)
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


    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Prestamo, pk=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
