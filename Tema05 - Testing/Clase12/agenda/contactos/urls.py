from django.urls import path
from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:persona_id>', views.detalle, name='detalle')
]