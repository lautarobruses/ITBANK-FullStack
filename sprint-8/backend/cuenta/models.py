from django.db import models
from usuario.models import Cliente

# Create your models here.

class TipoMoneda(models.Model):
    moneda_id = models.AutoField(primary_key=True)
    moneda_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_moneda'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    tipo_moneda = models.ForeignKey(TipoMoneda, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class CuentaCorriente(models.Model):
    account = models.OneToOneField(Cuenta, models.CASCADE, primary_key=True)
    limite = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cuenta_corriente'

class CajaAhorro(models.Model):
    account = models.OneToOneField(Cuenta, models.CASCADE, primary_key=True)
    cargo_mensual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'caja_ahorro'

class AuditoriaCuenta(models.Model):
    id = models.TextField(primary_key=True, blank=True)  # This field type is a guess.
    old_id = models.IntegerField(blank=True, null=True )
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, max_length=128)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    new_balance = models.DecimalField(max_digits=10, decimal_places=5, blank=True, max_length=128)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    old_iban = models.CharField(blank=True, max_length=128)
    new_iban = models.CharField(blank=True, max_length=128)
    old_type = models.CharField(blank=True, max_length=128)
    new_type = models.CharField(blank=True, max_length=128)
    user_action = models.CharField(blank=True, max_length=128)
    created_at = models.TextField(blank=True, max_length=128)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'

class Errores(models.Model):
    error_id = models.AutoField(primary_key=True)
    error_message = models.TextField()
    error_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'errores'