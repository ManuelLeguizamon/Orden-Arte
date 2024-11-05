from django.contrib import admin
from apps.usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'contraseña', 'telefono', 'roll', 'foto_perfil')
    list_filter = ('roll',)
    search_fields = ('nombre', 'roll')