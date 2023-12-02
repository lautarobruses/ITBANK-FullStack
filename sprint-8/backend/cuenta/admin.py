from django.contrib import admin
from .models import Cuenta, CajaAhorro, CuentaCorriente, TipoMoneda, AuditoriaCuenta, Errores
# Register your models here.

admin.site.register(TipoMoneda)
admin.site.register(Cuenta)
admin.site.register(CuentaCorriente)
admin.site.register(CajaAhorro)
admin.site.register(AuditoriaCuenta)
admin.site.register(Errores)