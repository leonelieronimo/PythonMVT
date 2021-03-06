"""PythonMVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from PythonMVT.views import saludo
from PythonMVT.views import diaHoy
from PythonMVT.views import nombre
from PythonMVT.views import saludoTemplate
from PythonMVT.views import saludoParametros
from PythonMVT.views import saludoFamilia
from PythonMVT.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('diaHoy/', diaHoy),
    path('nombre/<str:nombre>', nombre),
    path('saludoTemplate/', saludoTemplate),
    path('saludoParametros/', saludoParametros),
    path('saludoFamilia/<str:nombreFamiliar>/<int:edad>/', saludoFamilia),
    path('home/', home),
]
