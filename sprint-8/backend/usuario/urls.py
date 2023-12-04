from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserList.as_view()), #registra al usuario con el metodo POST
    path('login/', views.UserDetails.as_view()), #logea al usuario si este existe con el metodo POST
    path('self/', views.UserDetailsSelf.as_view()),  #devuelve los datos del usuario logeado con el metodo GET
    path('self/cliente/', views.ClienteDetailsSelf.as_view()),  #devuelve los datos del cliente logeado con el metodo GET
    path('obtener_saldo/', views.ObtenerSaldo.as_view(), name='obtener_saldo'),
    path('obtener_monto_prestamos/', views.ObtenerMontoPrestamos.as_view(), name='obtener_monto_prestamos'), 
]