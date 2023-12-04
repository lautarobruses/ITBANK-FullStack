from django.db import models

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    numero_cuenta = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_operacion = models.CharField(max_length=100)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_operacion} en {self.numero_cuenta}: ${self.monto}"
    
    class Meta:
        db_table = 'movimientos'