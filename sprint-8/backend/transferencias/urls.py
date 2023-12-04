from django.urls import path
from .views import MovimientoListCreateView

urlpatterns = [
    path('movimientos/', MovimientoListCreateView.as_view(), name='movimientos-list-create'),
]