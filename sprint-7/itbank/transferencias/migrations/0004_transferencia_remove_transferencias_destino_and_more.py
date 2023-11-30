# Generated by Django 4.2.7 on 2023-11-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferencias', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_destinatario', models.DecimalField(decimal_places=0, max_digits=8)),
                ('customer_name_destinatario', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='transferencias',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='transferencias',
            name='origen',
        ),
        migrations.DeleteModel(
            name='CuentaBancaria',
        ),
        migrations.DeleteModel(
            name='Transferencias',
        ),
    ]