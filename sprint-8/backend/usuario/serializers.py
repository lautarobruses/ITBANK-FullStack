from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

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