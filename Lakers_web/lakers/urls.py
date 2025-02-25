from django.urls import path, include
from django.contrib import admin 
from . import views
#Aqui voy a ir poniendo las urls que va a ir teniendo la app

urlpatterns = [
    path('equipo/', views.equipo_detalle, name='equipodetalle'),
    path('jugador/', views.jugador_detalle, name='jugadordetalle'),
]

