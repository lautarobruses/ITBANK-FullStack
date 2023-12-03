from django.urls import path, include
from tarjetas import views

urlpatterns = [
    path('<int:pk>/', views.TarjetasList.as_view()),
]