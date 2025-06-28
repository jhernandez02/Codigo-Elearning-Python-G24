from django.urls import path
from . import views

urlpatterns = [
    path('v1/ventas/', views.listar_pedido),
    path('v1/ventas/crear/', views.crear_pedido),
    path('v1/ventas/producto/<int:producto_id>', views.get_producto_precio),
    path('v1/ventas/boleta/generar', views.generar_boleta),
]