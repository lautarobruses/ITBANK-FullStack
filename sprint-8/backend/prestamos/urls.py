from django.urls import path, include
from tarjetas import views

urlpatterns = [
    path('<int:pk>/', views.TarjetasDetails.as_view()), #Devuelve los prestamos de una sucursal dada su branch_id en el pk con el metodo GET
]