from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.PrestamosList.as_view()), #Devuelve los prestamos de una sucursal dada su branch_id en el pk con el metodo GET
]