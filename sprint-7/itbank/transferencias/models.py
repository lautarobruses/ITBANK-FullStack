from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cuenta = models.OneToOneField('Cuenta', on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


class Cuenta(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)