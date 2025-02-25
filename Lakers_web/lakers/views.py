from django.shortcuts import render, get_list_or_404
from .models import Equipo, Jugador



def equipo_detalle(request):
    equipo = get_list_or_404(Equipo, nombre="Los Ángeles Lakers")
    jugadores = Equipo.jugadores.all()
    return render(request, 'equipo_detalle.html', {'equipo': equipo, 'jugadores': jugadores})

def jugador_detalle(request, jugador_id):
    jugador = get_list_or_404(Jugador, jugador_id=id)
    return render(request, 'jugador:detalle.html', { 'jugador: jugador'})
    
