from django.urls import path
from apps.grupo.views import GrupoView, CrearGrupoView, NuevoGrupoView
from apps.evento.views import CrearEventoView

urlpatterns = [
    path('', GrupoView.as_view(), name='grupo'),
    path('crear-grupo/', CrearGrupoView.as_view(), name='crear-grupo'),
    path('<int:grupo_id>/', NuevoGrupoView.as_view(), name='nuevo-grupo'),
    path('<int:grupo_id>/evento', CrearEventoView.as_view(), name='nuevo-evento')
]