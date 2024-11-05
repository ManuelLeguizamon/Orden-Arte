from django.contrib import admin
from apps.grupo.models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'listaCanciones', 'foto_grupo')
    list_filter = ('usuarios',)
    search_fields = ('nombre', 'listaCanciones')