from nba_api.stats.static import teams 
from nba_api.stats.endpoints import commonteamroster
from .models import Equipo, Jugador

def actualizar_datos_lakers(request): 
    lakers_id = 1610612747 #Este es el id de los Lakers usando la NBA API
    
    #Obtener info del equipo
    lakers_data = [team for team in teams.get_teams() if team['id'] == lakers_id ]
    
    equipo, created = Equipo.objects.update_or_create(
        nombre = lakers_data['full_name'], 
        defaults={
            "ciudad": lakers_data['city'],
            "abreviatura": lakers_data['abbreviation'],
            "fundacion": lakers_data['year_founded'],
            "campeonatos":17,
            "estadio": 'Crypto.com Arena',
        }
    )
    
    #Obtenemos el roster
    
    roster = commonteamroster.CommonTeamRoster(team_id=lakers_id).get_data_frames()[0]
    
    for _, row in roster.iterrows():
        Jugador.objects.update_or_create(
            nombre=row['PLAYER'],
            defaults={
                "posicion": row['POSITION'],
                "altura":row['HEIGHT'],
                "peso": row['WEIGHT'],
                "equipo": equipo
            }
        )
        