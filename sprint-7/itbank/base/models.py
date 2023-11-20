# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'

class CajaAhorro(models.Model):
    account = models.OneToOneField('Cuenta', models.DO_NOTHING, primary_key=True)
    cargo_mensual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'caja_ahorro'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    telefono = models.TextField(max_length=15)
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.CASCADE, blank=True, null=True)

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


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    tipo_moneda = models.ForeignKey('TipoMoneda', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class CuentaCorriente(models.Model):
    account = models.OneToOneField(Cuenta, models.DO_NOTHING, primary_key=True)
    limite = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cuenta_corriente'


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion_completa = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Errores(models.Model):
    error_id = models.AutoField(primary_key=True)
    error_message = models.TextField()
    error_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'errores'


class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca_tarjeta_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True, blank=True)
    numero_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='numero_cuenta', to_field=None, blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    tipo_operacion = models.CharField(blank=True, null=True, max_length=50)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


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


class TipoMoneda(models.Model):
    moneda_id = models.AutoField(primary_key=True)
    moneda_nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_moneda'
