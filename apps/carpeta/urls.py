from django.urls import path
from apps.carpeta.views import CarpetaView, CrearCarpetaView, SubirArchivoView

urlpatterns = [
    path('<int:grupo_id>/<int:carpeta_id>', CarpetaView.as_view(), name="carpeta"),
    path('<int:grupo_id>/<int:carpeta_id>/eliminar-archivo/<int:eliminar_archivo_id>/', CarpetaView.as_view(), name="eliminar-archivo"),
    path('crear-carpeta/<int:grupo_id>/', CrearCarpetaView.as_view(), name='crear-carpeta'),
    path('<int:grupo_id>/<int:carpeta_id>/subir-archivo/', SubirArchivoView.as_view(), name='subir-archivo'),
]
