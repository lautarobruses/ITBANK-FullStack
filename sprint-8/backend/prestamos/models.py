from django.db import models
from usuario.models import Cliente
# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prestamo'