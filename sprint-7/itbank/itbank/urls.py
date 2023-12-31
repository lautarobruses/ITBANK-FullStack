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

from base.views import home, comingSoon
from transferencias.views import transferencias
from pagos.views import pagos, servicios
from prestamos.views import prestamos, solicitar_prestamo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('', include('base.urls'), name='home'),
    path('coming-soon/', comingSoon, name='coming-soon'),
    path('accounts/', include('cuenta.urls'), name='cuenta'),
    path('pagos/', include('pagos.urls'), name='pagos'),
    path('prestamos/', include('prestamos.urls'), name='prestamos'),
    path('transferencias/', include('transferencias.urls'), name='transferencias'),
]
