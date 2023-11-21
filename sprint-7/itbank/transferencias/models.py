from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Transferencia(models.Model):
    dni_destinatario = models.DecimalField(max_digits=8, decimal_places=0)
    customer_name_destinatario = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
