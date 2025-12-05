from django.contrib import admin
from .models import Vacuna

@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ['id_vacuna', 'nombre', 'tipo', 'fecha_aplicacion', 'mascota']
