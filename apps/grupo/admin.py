from django.contrib import admin
from apps.grupo.models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'listaCanciones', 'userDueño')
    search_fields = ('nombre', 'listaCanciones')