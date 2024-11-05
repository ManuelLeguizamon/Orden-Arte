from django.urls import path
from apps.evento.views import EventoView

urlpatterns = [
    path('', EventoView.as_view(), name="evento")
]