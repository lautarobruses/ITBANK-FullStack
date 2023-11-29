from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'fecha')

admin.site.register(Servicio, ServicioAdmin)