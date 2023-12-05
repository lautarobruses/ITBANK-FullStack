from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Direccion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'customer_id',
            'customer_name',
            'customer_surname',
            'customer_dni',
            'telefono',
            'dob',
            'branch',
            'user'
        ]
        

class ModificarDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['direccion_completa']