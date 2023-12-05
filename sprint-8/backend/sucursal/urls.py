from django.urls import path
from .views import ListaSucursales

urlpatterns = [
    path('listar_sucursales/', ListaSucursales.as_view(), name='listar_sucursales'),
]