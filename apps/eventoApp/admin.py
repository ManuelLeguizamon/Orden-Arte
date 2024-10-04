from django.contrib import admin
from apps.eventoApp.models import EventoModel, VestimentaModel, HorarioModel, LocalidadModel, EventoTipoModel

@admin.register(LocalidadModel)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('pais', 'ciudad', 'direccion')
    list_filter = ('pais', 'ciudad', 'direccion')
    search_fields = ('pais', 'ciudad', 'direccion')

@admin.register(EventoTipoModel)
class EventoTipoAdmin(admin.ModelAdmin):
    list_display = ('eventoTipo',)
    list_filter = ('eventoTipo',)
    search_fields = ('eventoTipo',)

@admin.register(VestimentaModel)
class VestimentaAdmin(admin.ModelAdmin):
    list_display = ('vestimenta',)
    list_filter = ('vestimenta',)
    search_fields = ('vestimenta',)

@admin.register(HorarioModel)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horarioLlegada', 'horarioPruebaSonido', 'horarioTocar',)
    search_fields = ('horarioLlegada', 'horarioPruebaSonido', 'horarioTocar',)


@admin.register(EventoModel)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'dineroCobrar', 'localidad', 'tipo', 'vestimenta', 'horario')
    list_filter = ('localidad', 'tipo', 'vestimenta', 'horario')
    search_fields = ('nombre',)

