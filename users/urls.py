"""Definiuje wzorce adresów URL dla aplikacji users"""

from django import urls
from django.conf.urls import url
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Dołączenie domyslnych adresów URL uwierzytelniania
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji
    url('register/', views.register, name='register'),
]
