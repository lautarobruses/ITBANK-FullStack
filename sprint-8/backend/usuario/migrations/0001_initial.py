# Generated by Django 4.2.7 on 2023-12-02 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='ClienteBlack',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuario.cliente')),
            ],
            options={
                'db_table': 'cliente_black',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteClassic',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuario.cliente')),
            ],
            options={
                'db_table': 'cliente_classic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteGold',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='usuario.cliente')),
            ],
            options={
                'db_table': 'cliente_gold',
                'managed': False,
            },
        ),
    ]
