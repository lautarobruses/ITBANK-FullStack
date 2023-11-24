from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

