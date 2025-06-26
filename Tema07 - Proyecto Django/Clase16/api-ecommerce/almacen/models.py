from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField(default=0)
    imagen = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre