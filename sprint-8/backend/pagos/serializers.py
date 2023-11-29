from rest_framework import serializers
from .models import Servicio

class ServicioSerializer0(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    usuario_origen = serializers.CharField(max_length=200)
    usuario_destino = serializers.CharField(max_length=200)
    monto = serializers.DecimalField(max_digits=10, decimal_places=2)
    fecha = serializers.DateTimeField(read_only = True)

class ServicioSerializer(serializers.ModelSerializer):
    model = Servicio

    fields = '__all__'
    read_only_fields = ('id', 'fecha')