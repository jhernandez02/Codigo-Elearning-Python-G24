from rest_framework import serializers
from . models import Categoria, Serie

# Los serializers se encargan de convertir datos complejos (modelos)
# en formato Json, y también toman datos enviados en formato Json
# para convertirlos en objetos de Python

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields=('id','descripcion')

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Serie
        fields=('__all__')