from django.contrib import admin
from apps.usuarioApp.models import UsuarioModel

@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'contraseña', 'telefono', 'roll', 'foto_perfil')
    list_filter = ('roll',)
    search_fields = ('nombre', 'roll')