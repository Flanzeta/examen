"""vacunatorio URL Configuration

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
from django.urls import path, include
from django.urls import path
from registro import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.inicio),
    path('ingresar/', v.ingresar),
    path('ingreso_registro/', v.ingreso),
    path('eliminarest/', v.eliminarest),
    path('listarest/', v.listar_vacunatorio),
    path('listar/', v.listar),
    path('eliminar/', v.eliminar),
    path('buscar/', v.buscar),
    path('busqueda/', v.busqueda),
    path('busqueda_establecimiento/', v.busqueda_establecimiento),
]
