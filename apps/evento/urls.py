from django.urls import path
from apps.evento.views import EventoView, CrearEventoView, EventoDetalleView

urlpatterns = [
    path('', EventoView.as_view(), name="evento"),
    path('<int:grupo_id>/crear-evento/', CrearEventoView.as_view(), name='crear-evento'),
    path('<int:grupo_id>/<int:evento_id>/evento-detalle', EventoDetalleView.as_view(), name='evento-detalle')
]