from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = [
            'loan_id',
            'loan_type',
            'loan_date',
            'loan_total',
            'customer',
            'branch_id'
        ]