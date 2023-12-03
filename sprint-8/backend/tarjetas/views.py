from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Tarjeta
from .serializers import TarjetaSerializer
# Create your views here.

class TarjetasDetailsSelf(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, **kwards):
        tarjetas = Tarjeta.objects.filter(customer=self.request.user.id)
        serializer = TarjetaSerializer(tarjetas, many=True)

        if tarjetas is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ''}, status=status.HTTP_400_BAD_REQUEST)

class TarjetasDetails(APIView):
    def get(self, request, pk, **kwards):
        tarjetas = Tarjeta.objects.filter(customer=pk)
        serializer = TarjetaSerializer(tarjetas, many=True)

        if tarjetas is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ''}, status=status.HTTP_400_BAD_REQUEST)