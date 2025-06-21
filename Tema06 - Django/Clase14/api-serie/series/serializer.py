from rest_framework import serializers
from . models import Categoria, Serie, Favorito

# Los serializers se encargan de convertir datos complejos (modelos)
# en formato Json, y también toman datos enviados en formato Json
# para convertirlos en objetos de Python

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields=('id','descripcion')

class SerieSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(source='categoria.descripcion', read_only=True)

    class Meta:
        model=Serie
        fields=('__all__')

class FavoritoSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(source='usuario.username', read_only=True)
    nombre_serie = serializers.CharField(source='serie.nombre', read_only=True)
    nombre_categoria = serializers.CharField(source='serie.categoria.descripcion', read_only=True)
    
    class Meta:
        model=Favorito
        fields=('__all__')
        # El usuario no puede enviar o modificar el campo usuario
        read_only_fields = ['usuario']
    
    def validate(self, data):
        # Obtenemos el usuario que solicita la petición por medio del token
        user = self.context['request'].user
        # Obtenemos el id de la seria enviada por el body de la petición
        serie = data['serie']
        if Favorito.objects.filter(usuario=user,serie=serie).exists():
            raise serializers.ValidationError("Esta serie ya se guardó como favorita.")
        return data

