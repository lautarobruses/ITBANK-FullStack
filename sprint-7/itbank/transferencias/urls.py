from django.contrib import admin
from django.urls import path
from .views import transferencias, accion_transferir

urlpatterns = [
    path('', transferencias, name='transferencias'),
    path('transferir/', accion_transferir, name='accion_transferir'),
]