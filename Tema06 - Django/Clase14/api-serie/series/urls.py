from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'series', views.SerieViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/categorias/<int:categoria_id>/series/', views.SeriePorCategoria.as_view()),
    path('v1/favoritos/', views.FavoritoListView.as_view()),
    path('v1/favoritos/crear/', views.FavoritoCreateView.as_view()),
    path('v1/favoritos/<int:pk>/eliminar/', views.FavoritoDeleteView.as_view()),
]