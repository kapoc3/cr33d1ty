"""
credyty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from test import views as testview

urlpatterns = [
     path('', testview.index, name='index'),   
     path('ejercicio1/', testview.ejercicio1, name='ejercicio1'),
     path('ejercicio2/', testview.ejercicio2, name='ejercicio2'),
     path('ejercicio3/', testview.ejercicio3, name='ejercicio3'),
     path('ejercicio4/', testview.ejercicio4, name='ejercicio4'),
     path('ejercicio5/', testview.ejercicio5, name='ejercicio5'),
]
