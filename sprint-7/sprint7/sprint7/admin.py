from django.contrib import admin
from .models import (
    AuditoriaCuenta, CajaAhorro, Cliente, ClienteBlack, ClienteClassic, ClienteGold,
    Cuenta, CuentaCorriente, Direccion, Empleado, Errores, MarcaTarjeta,
    Movimientos, Prestamo, Sucursal, Tarjeta, TarjetaCredito, TarjetaDebito,
    TipoMoneda
)

admin.site.register(AuditoriaCuenta)
admin.site.register(CajaAhorro)
admin.site.register(Cliente)
admin.site.register(ClienteBlack)
admin.site.register(ClienteClassic)
admin.site.register(ClienteGold)
admin.site.register(Cuenta)
admin.site.register(CuentaCorriente)
admin.site.register(Direccion)
admin.site.register(Empleado)
admin.site.register(Errores)
admin.site.register(MarcaTarjeta)
admin.site.register(Movimientos)
admin.site.register(Prestamo)
admin.site.register(Sucursal)
admin.site.register(Tarjeta)
admin.site.register(TarjetaCredito)
admin.site.register(TarjetaDebito)
admin.site.register(TipoMoneda)
