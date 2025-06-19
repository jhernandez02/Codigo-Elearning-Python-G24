from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'series', views.SerieViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]