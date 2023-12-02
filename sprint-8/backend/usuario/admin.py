from django.contrib import admin
from .models import Cliente, ClienteBlack, ClienteClassic, ClienteGold, Direccion

# Register your models here.

admin.site.register(Cliente)
admin.site.register(ClienteBlack)
admin.site.register(ClienteClassic)
admin.site.register(ClienteGold)
admin.site.register(Direccion)