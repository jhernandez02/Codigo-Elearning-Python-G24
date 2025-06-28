from django.urls import path
from . import views

urlpatterns = [
    path('v1/ventas/producto/<int:producto_id>', views.get_producto_precio),
]