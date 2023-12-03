from django.urls import path, include
from usuario import views

urlpatterns = [
    path('register/', views.UserList.as_view()), #registra al usuario con el metodo POST
    path('login/', views.UserDetails.as_view()), #logea al usuario si este existe con el metodo POST
    path('self/', views.UserDetailsSelf.as_view())  #devuelve los datos del usuario logeado con el metodo GET
]