from django.contrib import admin
from apps.carpetaApp.models import CarpetaModel, MultimediaModel

@admin.register(CarpetaModel)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'partitura', 'fechaCarga', 'grupo')
    list_filter = ('nombre', 'fechaCarga')
    search_fields = ('nombre',)

@admin.register(MultimediaModel)
class MultimediaAdmin(admin.ModelAdmin):
    list_display = ('nombreMultimedia', 'archivo', 'fechaSubida', 'carpeta')
    list_filter = ('nombreMultimedia', 'fechaSubida')
    search_fields = ('nombreMultimedia',)