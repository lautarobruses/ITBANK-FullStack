# Generated by Django 4.2.7 on 2023-11-19 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_remove_userprofile_apellido_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
