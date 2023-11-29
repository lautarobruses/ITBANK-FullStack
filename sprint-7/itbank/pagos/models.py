from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_origen = models.CharField(max_length=200)
    usuario_destino = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
