from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_field = ('id',)

admin.site.register(Servicio, ServicioAdmin)