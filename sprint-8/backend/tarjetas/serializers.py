from rest_framework import serializers
from .models import Tarjeta, TarjetaDebito

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = [
            'tarjeta_numero',
            'tarjeta_cvv',
            'tarjeta_fecha_otorgamiento',
            'tarjeta_fecha_expiracion',
            'tarjeta_nombre_propietario',
            'customer',                         #es el user_id
            'marca_tarjeta'
        ]

class TarjetaDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaDebito
        fields = [
            'tarjeta_numero',
            'account'
        ]