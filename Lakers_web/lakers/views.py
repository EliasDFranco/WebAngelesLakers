from django.shortcuts import render, get_list_or_404
from .models import Equipo, Jugador

def index(request):
    return render(request, 'index.html' )

def equipoDetalle(request):
    equipo = get_list_or_404(Equipo, nombre="Los Ángeles Lakers")
    jugadores = equipo[0].jugadores.all()
    return render(request, 'equipoDetalle.html', {'equipo': equipo[0], 'jugadores': jugadores})

def jugadorDetalle(request, jugador_id):
    jugador = get_list_or_404(Jugador, jugador_id=id)
    return render(request, 'jugadorDetalle.html', { 'jugador': jugador})
    
