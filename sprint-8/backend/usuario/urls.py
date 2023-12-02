from django.urls import path, include
from usuario import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetails.as_view())
]