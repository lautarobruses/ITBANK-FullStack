from rest_framework import viewsets
from tarjetas.models import Tarjeta, TarjetaCredito, TarjetaDebito
from .models import Cliente,Cuenta,CajaAhorro,CuentaCorriente
from .serializers import ClienteSerializer, CuentaSerializer, CajaAhorroSerializer, CuentaCorrienteSerializer, TarjetaSerializer, TarjetaCreditoSerializer, TarjetaDebitoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    lookup_field = 'customer_id'

class CajaAhorroViewSet(viewsets.ModelViewSet):
    queryset = CajaAhorro.objects.all()
    serializer_class = CajaAhorroSerializer

class CuentaCorrienteViewSet(viewsets.ModelViewSet):
    queryset = CuentaCorriente.objects.all()
    serializer_class = CuentaCorrienteSerializer

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    lookup_field = 'customer_id'

class TarjetaCreditoViewSet(viewsets.ModelViewSet):
    queryset = TarjetaCredito.objects.all()
    serializer_class = TarjetaCreditoSerializer

class TarjetaDebitoViewSet(viewsets.ModelViewSet):
    queryset = TarjetaDebito.objects.all()
    serializer_class = TarjetaDebitoSerializer
