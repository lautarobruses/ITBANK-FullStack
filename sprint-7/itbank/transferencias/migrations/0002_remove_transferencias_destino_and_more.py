# Generated by Django 4.2.7 on 2023-11-20 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transferencias', '0001_initial'),
    ]

    operations = [
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
