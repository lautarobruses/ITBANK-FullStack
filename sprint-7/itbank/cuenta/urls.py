from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.cuenta, name='cuenta'),
    path('login/', views.cuenta, name='login'),
    path('register/', views.cuenta, name='register'),
]