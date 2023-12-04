from rest_framework import serializers
from .models import PagoServicio

class PagoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoServicio
        fields = '__all__'