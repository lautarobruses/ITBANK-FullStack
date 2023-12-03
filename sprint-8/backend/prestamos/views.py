from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Prestamo
from .serializers import PrestamoSerializer
# Create your views here.

class PrestamosList(APIView):
    def get(self, request, pk, **kwards):
        tarjetas = Prestamo.objects.filter(branch_id=pk)
        serializer = PrestamoSerializer(tarjetas, many=True)

        if tarjetas is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': ''}, status=status.HTTP_400_BAD_REQUEST)