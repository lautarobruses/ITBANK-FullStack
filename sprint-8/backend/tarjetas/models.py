from django.db import models
from usuario.models import Cliente
from cuenta.models import Cuenta

# Create your models here.

class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca_tarjeta_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    tarjeta_numero = models.AutoField(primary_key=True)
    tarjeta_cvv = models.IntegerField(db_column='tarjeta_CVV')  # Field name made lowercase.
    tarjeta_fecha_otorgamiento = models.TextField()
    tarjeta_fecha_expiracion = models.TextField()
    tarjeta_nombre_propietario = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    marca_tarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TarjetaCredito(models.Model):
    tarjeta_numero = models.OneToOneField(Tarjeta, models.DO_NOTHING, db_column='tarjeta_numero', primary_key=True)
    cantidad_extensiones = models.IntegerField()
    limite_en_un_pago = models.FloatField()
    limite_en_cuotas = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tarjeta_credito'


class TarjetaDebito(models.Model):
    tarjeta_numero = models.OneToOneField(Tarjeta, models.DO_NOTHING, db_column='tarjeta_numero', primary_key=True)
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta_debito'

class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True, blank=True)
    numero_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='numero_cuenta', to_field=None, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipo_operacion = models.CharField(blank=True, null=True, max_length=50)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'