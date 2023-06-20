"""
URL configuration for djangoApp project.

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
from django.urls import path
from persona import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.layouts, name='layouts'),
    path('acerca/', views.acerca, name='acerca'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('layouts/', views.layouts, name='layouts'),
    path('index/', views.index, name='index'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('crearestudiante/', views.crearestudiante, name='crearestudiante'),
    path('crearrol/', views.crearrol, name='crearrol'),
    path('indexestudiante/', views.indexestudiante, name='indexestudiante'),
    path('indexrol/', views.indexrol, name='indexrol'),
    path('editarestudiante/<int:id>', views.editarestudiante, name='editarestudiante'),
    path('editarrol/<int:id>', views.editarrol, name='editarrol'),
    path('eliminarestudiante/<int:id>/', views.eliminarestudiante, name='eliminarestudiante'),
    path('eliminarrol/<int:id>/', views.eliminarrol, name='eliminarrol'),


]
