from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from tarjetas.models import Tarjeta, TarjetaCredito, TarjetaDebito
from .models import Cliente, Cuenta, CajaAhorro, CuentaCorriente
from .serializers import ClienteSerializer, CuentaSerializer, CajaAhorroSerializer, CuentaCorrienteSerializer, TarjetaSerializer, TarjetaCreditoSerializer, TarjetaDebitoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    lookup_field = 'customer_id'

    def retrieve(self, request, *args, **kwargs):
        # Si se proporciona un account_id, realiza la búsqueda por ese ID
        try:
            cuenta = Cuenta.objects.filter(customer_id=kwargs.get('customer_id'))
            serializer = self.get_serializer(cuenta, many=True)
            return Response(serializer.data)
        except Cuenta.DoesNotExist:
            return Response({'error': 'La cuenta no existe'}, status=status.HTTP_404_NOT_FOUND)

class CajaAhorroViewSet(viewsets.ModelViewSet):
    queryset = CajaAhorro.objects.all()
    serializer_class = CajaAhorroSerializer
    lookup_field = 'account_id'

    def retrieve(self, request, *args, **kwargs):
        # Si se proporciona un account_id, realiza la búsqueda por ese ID
        try:
            print(kwargs)
            cuenta = CajaAhorro.objects.filter(account_id=kwargs.get('account_id'))
            serializer = self.get_serializer(cuenta, many=True)
            return Response(serializer.data)
        except CajaAhorro.DoesNotExist:
            return Response({'error': 'La cuenta no existe'}, status=status.HTTP_404_NOT_FOUND)

class CuentaCorrienteViewSet(viewsets.ModelViewSet):
    queryset = CuentaCorriente.objects.all()
    serializer_class = CuentaCorrienteSerializer
    lookup_field = 'account_id'

    def retrieve(self, request, *args, **kwargs):
        # Si se proporciona un account_id, realiza la búsqueda por ese ID
        try:
            print(kwargs)
            cuenta = CuentaCorriente.objects.filter(account_id=kwargs.get('account_id'))
            serializer = self.get_serializer(cuenta, many=True)
            return Response(serializer.data)
        except CuentaCorriente.DoesNotExist:
            return Response({'error': 'La cuenta no existe'}, status=status.HTTP_404_NOT_FOUND)

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
