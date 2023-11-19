from django.urls import path
from .views import home, sendMessage

urlpatterns = [
    path('', home, name='home'),
    path('contact/', sendMessage, name='sendMessage'),
]
