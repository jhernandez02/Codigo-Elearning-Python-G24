from django.shortcuts import render
from .models import Persona

# Create your views here.

def index(request):
    # Obtenemos lista de todas las personas
    lista_personas = Persona.objects.all()
    # Preparamos los datos
    context = {
        'personas': lista_personas
    }
    # Pasamos los valores de context a la plantilla index.html
    return render(request, 'personas/index.html', context)

def detalle(request, persona_id):
    # Busco una persona por el valor de su id
    persona = Persona.objects.get(pk=persona_id)
    # Preparamos los datos
    context = {
        'persona': persona
    }
    # Pasamos los valores de context a la plantilla detalle.html
    return render(request, 'personas/detalle.html', context)
