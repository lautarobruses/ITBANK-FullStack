from django.db import models

class PagoServicio(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"{self.servicio} - ${self.monto} (Vencimiento: {self.fecha_vencimiento})"
    
    class Meta:
        db_table = 'pagos_servicio'
