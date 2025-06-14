from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres     = models.CharField(max_length=100)
    apellidos   = models.CharField(max_length=100)
    telefono    = models.CharField(max_length=25)
    email       = models.CharField(max_length=45)
    direccion   = models.CharField(max_length=100)
