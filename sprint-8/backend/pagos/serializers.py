from rest_framework import serializers
from .models import Servicio

class ServicioSerializer0(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    servicio = serializers.CharField(max_length=200)
    monto = serializers.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = serializers.DateTimeField()

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio

        fields = '__all__'
        read_only_fields = ('id',)