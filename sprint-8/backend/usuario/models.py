from django.db import models
from django.contrib.auth.models import User
from sucursal.models import Sucursal
from sucursal.models import Empleado

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    telefono = models.TextField(max_length=15)
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Sucursal, models.DO_NOTHING)
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteBlack(models.Model):
    customer = models.OneToOneField(Cliente, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente_black'


class ClienteClassic(models.Model):
    customer = models.OneToOneField(Cliente, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente_classic'


class ClienteGold(models.Model):
    customer = models.OneToOneField(Cliente, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente_gold'

class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion_completa = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'