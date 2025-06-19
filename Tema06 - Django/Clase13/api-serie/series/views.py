from rest_framework import viewsets
from rest_framework.response import Response
from . models import Categoria, Serie
from . serializer import CategoriaSerializer, SerieSerializer

# El ModelViewSet es una clase de vista que proporciona
# un conjuto de operaciones (CRUD) para un modelo específico
class CategoriaViewSet(viewsets.ModelViewSet):
    # Definimos qué datos del modelo estarán disponibles
    # para ser consultados y modificados
    queryset = Categoria.objects.all().order_by('descripcion')
    # Se especifíca el serializador que se utilizará
    # para transformar los datos en el modelo Categoria
    # y los formatos de respuesta Json
    serializer_class = CategoriaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all().order_by('nombre')
    serializer_class = SerieSerializer
