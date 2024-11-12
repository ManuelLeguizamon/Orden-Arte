from django.urls import path
from apps.carpeta.views import CarpetaView, CrearCarpetaView, SubirArchivoView

urlpatterns = [
    path('<int:grupo_id>/<int:carpeta_id>', CarpetaView.as_view(), name="carpeta"),
    path('crear-carpeta/<int:grupo_id>/', CrearCarpetaView.as_view(), name='crear-carpeta'),
    path('<int:grupo_id>/<int:carpeta_id>/subir-archivo/', SubirArchivoView.as_view(), name='subir-archivo'),
]
