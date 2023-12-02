from django.contrib import admin
from .models import Tarjeta, TarjetaDebito, TarjetaCredito, MarcaTarjeta, Movimientos

# Register your models here.

admin.site.register(Tarjeta)
admin.site.register(TarjetaCredito)
admin.site.register(TarjetaDebito)
admin.site.register(MarcaTarjeta)
admin.site.register(Movimientos)