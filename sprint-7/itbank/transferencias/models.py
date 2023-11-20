from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class CuentaBancaria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        
        return f'{self.usuario.username} cuenta bancaria'
    
class Transferencias(models.Model):
    origen = models.ForeignKey(CuentaBancaria, related_name='cuenta_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(CuentaBancaria, related_name='cuenta_destino', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'Transferencia de {self.origen.usuario.username} a {self.destino.usuario.username}'
    
    class Meta:
        ordering = ['-fecha']