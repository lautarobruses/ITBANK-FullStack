# Generated by Django 4.2.7 on 2023-11-20 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_authuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
