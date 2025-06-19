from django.db import models

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
