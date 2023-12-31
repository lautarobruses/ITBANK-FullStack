# Generated by Django 4.2.7 on 2023-12-02 20:08

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
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cuenta.cuenta')),
                ('cargo_mensual', models.FloatField()),
            ],
            options={
                'db_table': 'caja_ahorro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CuentaCorriente',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cuenta.cuenta')),
                ('limite', models.FloatField()),
            ],
            options={
                'db_table': 'cuenta_corriente',
                'managed': False,
            },
        ),
    ]
