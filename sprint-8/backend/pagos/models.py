from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    class Meta: 
        ordering = ['fecha_vencimiento']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):

        return f'Servicio: {self.servicio}, Monto: {self.monto}, Vencimiento: {self.fecha_vencimiento}'

