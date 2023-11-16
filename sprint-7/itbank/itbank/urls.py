"""
URL configuration for itbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('coming-soon/', views.comingSoon, name='coming-soon'),
    path('cuenta/', include('cuenta.urls'), name='cuenta'),
    path('pagos/', views.home, name='pagos'),
    path('prestamos/', views.home, name='prestamos'),
    path('transferencias/', views.home, name='transferencias'),
]
