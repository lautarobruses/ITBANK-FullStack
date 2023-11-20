from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagos, name='pagos'),
    path('servicios/', views.servicios, name='servicios'),
]