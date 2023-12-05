from rest_framework import generics
from .models import Sucursal
from .serializers import SucursalSerializer

class ListaSucursales(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
