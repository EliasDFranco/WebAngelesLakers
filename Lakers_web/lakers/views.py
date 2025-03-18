from django.shortcuts import render, get_list_or_404
from .models import Equipo, Jugador
from django.http import JsonResponse
from .utils import get_nba_data

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html' )

def equipoDetalle(request):
    equipo = get_list_or_404(Equipo, nombre="Los Ángeles Lakers")
    jugadores = equipo[0].jugador_set.all()
    return render(request, 'equipoDetalle.html', {'equipo': equipo, 'jugadores': jugadores})

def jugadorDetalle(request, jugador_id):
    jugador = get_list_or_404(Jugador, id=jugador_id)
    return render(request, 'jugadorDetalle.html', { 'jugador': jugador})
 

        
    
