# Generated by Django 4.2.7 on 2023-11-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('new_id', models.IntegerField(blank=True, null=True)),
                ('old_balance', models.DecimalField(blank=True, decimal_places=5, max_digits=10, max_length=128)),
                ('new_balance', models.DecimalField(blank=True, decimal_places=5, max_digits=10, max_length=128)),
                ('old_iban', models.CharField(blank=True, max_length=128)),
                ('new_iban', models.CharField(blank=True, max_length=128)),
                ('old_type', models.CharField(blank=True, max_length=128)),
                ('new_type', models.CharField(blank=True, max_length=128)),
                ('user_action', models.CharField(blank=True, max_length=128)),
                ('created_at', models.TextField(blank=True, max_length=128)),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI', unique=True)),
                ('telefono', models.TextField(max_length=15)),
                ('dob', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_completa', models.TextField()),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Errores',
            fields=[
                ('error_id', models.AutoField(primary_key=True, serialize=False)),
                ('error_message', models.TextField()),
                ('error_date', models.TextField()),
            ],
            options={
                'db_table': 'errores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MarcaTarjeta',
            fields=[
                ('marca_tarjeta_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca_tarjeta_nombre', models.TextField()),
            ],
            options={
                'db_table': 'marca_tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('tipo_operacion', models.CharField(blank=True, max_length=50, null=True)),
                ('hora', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('tarjeta_numero', models.AutoField(primary_key=True, serialize=False)),
                ('tarjeta_cvv', models.IntegerField(db_column='tarjeta_CVV')),
                ('tarjeta_fecha_otorgamiento', models.TextField()),
                ('tarjeta_fecha_expiracion', models.TextField()),
                ('tarjeta_nombre_propietario', models.TextField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoMoneda',
            fields=[
                ('moneda_id', models.AutoField(primary_key=True, serialize=False)),
                ('moneda_nombre', models.TextField()),
            ],
            options={
                'db_table': 'tipo_moneda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CajaAhorro',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.cuenta')),
                ('cargo_mensual', models.FloatField()),
            ],
            options={
                'db_table': 'caja_ahorro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteBlack',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.cliente')),
            ],
            options={
                'db_table': 'cliente_black',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteClassic',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.cliente')),
            ],
            options={
                'db_table': 'cliente_classic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteGold',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.cliente')),
            ],
            options={
                'db_table': 'cliente_gold',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CuentaCorriente',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.cuenta')),
                ('limite', models.FloatField()),
            ],
            options={
                'db_table': 'cuenta_corriente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TarjetaCredito',
            fields=[
                ('tarjeta_numero', models.OneToOneField(db_column='tarjeta_numero', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.tarjeta')),
                ('cantidad_extensiones', models.IntegerField()),
                ('limite_en_un_pago', models.FloatField()),
                ('limite_en_cuotas', models.FloatField()),
            ],
            options={
                'db_table': 'tarjeta_credito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TarjetaDebito',
            fields=[
                ('tarjeta_numero', models.OneToOneField(db_column='tarjeta_numero', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='base.tarjeta')),
            ],
            options={
                'db_table': 'tarjeta_debito',
                'managed': False,
            },
        ),
    ]
