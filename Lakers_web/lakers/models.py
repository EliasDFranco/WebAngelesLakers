from django.db import models

# Modelo de Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=150, default="Los Ángeles Lakers")
    fundacion = models.IntegerField()
    ciudad = models.CharField(max_length=150, default="Los Ángeles, California")
    campeonatos = models.IntegerField(default=15)
    estadio = models.CharField(max_length=200, default="Crypto.com Arena")
    logo_lakers = models.ImageField(upload_to="equipos/", blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
# Modelo de Jugador
class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE, related_name="jugador")
    nombre = models.CharField(max_length=150)
    posicion = models.CharField(max_length=100, default="")
    numero_remera = models.IntegerField()
    foto_jugador = models.ImageField(upload_to="jugador/", blank=True, null=True )
    
    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"
