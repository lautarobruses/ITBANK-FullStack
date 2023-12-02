from rest_framework import serializers
from .models import Tarjeta

class TarjetaCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = [
            'tarjeta_numero',
            'tarjeta_cvv',
            'tarjeta_fecha_otorgamiento',
            'tarjeta_fecha_expiracion',
            'tarjeta_nombre_propietario',
            'customer',
            'marca_tarjeta'
        ]