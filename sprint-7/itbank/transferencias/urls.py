from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.transferencias, name='transferencias'),
    path('transferir/', views.accion_transferir, name='AccionTransferir'),
]