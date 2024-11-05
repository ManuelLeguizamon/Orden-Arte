from django.contrib import admin
from apps.evento.models import Evento, Vestimenta, Horario, Localidad, EventoTipo

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('pais', 'ciudad', 'direccion')
    list_filter = ('pais', 'ciudad', 'direccion')
    search_fields = ('pais', 'ciudad', 'direccion')

@admin.register(EventoTipo)
class EventoTipoAdmin(admin.ModelAdmin):
    list_display = ('eventoTipo',)
    list_filter = ('eventoTipo',)
    search_fields = ('eventoTipo',)

@admin.register(Vestimenta)
class VestimentaAdmin(admin.ModelAdmin):
    list_display = ('vestimenta',)
    list_filter = ('vestimenta',)
    search_fields = ('vestimenta',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horarioLlegada', 'horarioPruebaSonido', 'horarioTocar',)
    search_fields = ('horarioLlegada', 'horarioPruebaSonido', 'horarioTocar',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'dineroCobrar', 'localidad', 'tipo', 'vestimenta', 'horario')
    list_filter = ('localidad', 'tipo', 'vestimenta', 'horario')
    search_fields = ('nombre',)

