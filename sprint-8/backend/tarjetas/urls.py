from django.urls import path, include
from . import views

urlpatterns = [
    path('self/', views.TarjetasDetailsSelf.as_view()), #Devuelve las tarjetas del usuario logeado con el metodo GET
    path('<int:pk>/', views.TarjetasDetails.as_view()), #Devuelve las tarjetas del usuario dado su id en el pk con el metodo GET
]