from rest_framework import generics
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

# Create your views here.

class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer