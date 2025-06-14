from django.contrib import admin
from .models import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombres','apellidos','email')
    search_fields = ('nombres','apellidos','email')

# Register your models here.
admin.site.register(Persona, PersonaAdmin)