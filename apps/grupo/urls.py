from django.urls import path
from apps.grupo.views import GrupoView, CrearGrupoView, NuevoGrupoView
from apps.evento.views import CrearEventoView

urlpatterns = [
    path('', GrupoView.as_view(), name='grupo'),
    path('borrar-grupo/<int:borrar_grupo_id>/', GrupoView.as_view(), name='borrar_grupo'),
    path('crear-grupo/', CrearGrupoView.as_view(), name='crear-grupo'),
    path('<int:grupo_id>/', NuevoGrupoView.as_view(), name='nuevo-grupo'),
    path('<int:grupo_id>/eliminar-evento/<int:borrar_evento_id>/', NuevoGrupoView.as_view(), name='eliminar-evento'),
    path('<int:grupo_id>/eliminar-carpeta/<int:borrar_carpeta_id>/', NuevoGrupoView.as_view(), name='eliminar-carpeta'),
    path('<int:grupo_id>/evento', CrearEventoView.as_view(), name='nuevo-evento')
]
