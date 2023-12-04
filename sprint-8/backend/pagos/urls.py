from django.urls import path
from .views import PagoServicioListCreateView

urlpatterns = [
    path('pagos-servicio/', PagoServicioListCreateView.as_view(), name='pagos-servicio-list-create'),
]