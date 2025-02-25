from django.shortcuts import render, get_list_or_404
from .models import Equipo, Jugador



def equipoDetalle(request):
    equipo = get_list_or_404(Equipo, nombre="Los Ángeles Lakers")
    jugadores = Equipo.jugadores.all()
    return render(request, 'equipoDetalle.html', {'equipo': equipo, 'jugadores': jugadores})

def jugador_detalle(request, jugador_id):
    jugador = get_list_or_404(Jugador, jugador_id=id)
    return render(request, 'jugadorDetalle.html', { 'jugador: jugador'})
    
