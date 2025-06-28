from django.urls import path
from almacen import views

urlpatterns = [
    path('v1/categorias', views.CategoriaListView.as_view()),
    path('v1/productos', views.ProductoListView.as_view()),
    path('v1/productos/<int:pk>', views.ProductoDetailView.as_view()),
]