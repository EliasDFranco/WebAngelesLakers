from django.contrib import admin
from .models import Equipo, Jugador

# Register your models here.
#Registrando nuestros modelos Equipo y Jugador
admin.site.register(Equipo)
admin.site.register(Jugador)
