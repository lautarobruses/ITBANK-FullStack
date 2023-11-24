from django.contrib import admin
from django.urls import path
from .views import prestamos, solicitar_prestamo

urlpatterns = [
    path('', prestamos, name='prestamos'),
    path('solicitar/', solicitar_prestamo, name='solicitar_prestamo'),
]