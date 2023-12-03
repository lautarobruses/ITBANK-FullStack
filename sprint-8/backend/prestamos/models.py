from django.db import models
from usuario.models import Cliente
from sucursal.models import Sucursal
# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.DateTimeField(auto_now_add=True)
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    branch = models.ForeignKey(Sucursal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prestamo'