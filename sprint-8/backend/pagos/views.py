from rest_framework import generics
from .models import PagoServicio
from .serializers import PagoServicioSerializer

class PagoServicioListCreateView(generics.ListCreateAPIView):
    queryset = PagoServicio.objects.all()
    serializer_class = PagoServicioSerializer