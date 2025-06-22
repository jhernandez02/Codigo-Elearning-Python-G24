from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Categoria, Serie, Favorito
from . serializer import CategoriaSerializer, SerieSerializer, FavoritoSerializer

# El ModelViewSet es una clase de vista que proporciona un conjuto de operaciones (CRUD) para un modelo específico
class CategoriaViewSet(viewsets.ModelViewSet):
    # Definimos qué datos del modelo estarán disponibles para ser consultados y modificados
    queryset = Categoria.objects.all().order_by('descripcion')
    # Se especifíca el serializador que se utilizará para transformar los datos en el modelo Categoria y los formatos de respuesta Json
    serializer_class = CategoriaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all().order_by('nombre')
    serializer_class = SerieSerializer

class SeriePorCategoria(APIView):
    # Ejecutamos con el método GET
    def get(self, request, categoria_id):
        # Seleccionamos las series según el valor de categoria_id
        series = Serie.objects.filter(categoria=categoria_id)
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

class FavoritoListView(generics.ListAPIView):
    serializer_class = FavoritoSerializer

    # Implementamos el resultado de la consulta para que devuelva el conjuto de datos (queryset) que se va a listar
    def get_queryset(self):
        # Se obtiene el nombre del usuario del token enviado 
        print(self.request.user)
        # Filtramos solo los dato del usuario que ha solicitado la petición
        return Favorito.objects.filter(usuario=self.request.user)

class FavoritoCreateView(generics.CreateAPIView):
    serializer_class = FavoritoSerializer

    # perform_create se ejecuta justo despues que los datos han sido validados y antes de enviar la respuesta
    # Personalizamos el comportamiento del guardado
    def perform_create(self, serializer):
        # Asignamos el valor del campo usuario
        serializer.save(usuario=self.request.user)

class FavoritoDeleteView(generics.DestroyAPIView):
    serializer_class = FavoritoSerializer

    # Implementamos la consulta para definir de donde se va a buscar el objeto que se quiere eliminar
    def get_queryset(self):
        # Filtramos solo los datos del usuario que ha solicitado la petición
        return Favorito.objects.filter(usuario=self.request.user)