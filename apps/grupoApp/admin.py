from django.contrib import admin
from apps.grupoApp.models import GrupoModel

@admin.register(GrupoModel)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'listaCanciones', 'foto_grupo')
    list_filter = ('usuarios',)
    search_fields = ('nombre', 'listaCanciones')