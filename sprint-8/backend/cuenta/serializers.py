from rest_framework import serializers
from tarjetas.models import Tarjeta, TarjetaCredito, TarjetaDebito
from .models import Cliente, Cuenta, CajaAhorro, CuentaCorriente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class CajaAhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CajaAhorro
        fields = '__all__'

class CuentaCorrienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaCorriente
        fields = '__all__'
        
class TarjetaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaCredito
        fields = '__all__'

class TarjetaDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaDebito
        fields = '__all__'

class TarjetaSerializer(serializers.ModelSerializer):
    tarjetacredito = TarjetaCreditoSerializer(source='tarjetacredito_set', many=True, read_only=True)
    tarjetadebito = TarjetaDebitoSerializer(source='tarjetadebito_set', many=True, read_only=True)

    class Meta:
        model = Tarjeta
        fields = '__all__'
