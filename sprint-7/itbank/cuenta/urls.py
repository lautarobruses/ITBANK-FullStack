from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from base.views import home #cambiar

from . import views

urlpatterns = [
    path('', home, name='cuenta'),
    path('auth/', include('django.contrib.auth.urls'), name='auth'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]