from django.urls import path, include
from django.contrib import admin 
from . import views
#Aqui voy a ir poniendo las urls que va a ir teniendo la app

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('equipo/', views.equipoDetalle, name="equipoDetalle"),
    path('jugador/<int:jugador_id>/', views.jugadorDetalle, name="jugadorDetalle"),
    path('nba/teams', views.get_teams),
]