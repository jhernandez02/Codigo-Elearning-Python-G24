from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Serie(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    puntaje = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='series_favoritas')
    serie = models.ForeignKey(Serie, on_delete=models.RESTRICT, related_name='usuarios_favoritos')

    class Meta:
        # Valido que un usuario no pueda tener la misma serie más de una vez
        unique_together = ('usuario', 'serie')
    
    def __str__(self):
        return f"{self.usuario.username} - {self.serie.nombre}"
