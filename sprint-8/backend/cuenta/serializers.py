from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cuenta, CuentaCorriente

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = [
            'account_id',
            'balance',
            'iban',
            'customer',
            'tipo_moneda',
        ]

class CuentaCorrienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaCorriente
        fields = [
            'account',
            'limite',
        ]

