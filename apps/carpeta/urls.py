from django.urls import path
from apps.carpeta.views import CarpetaView

urlpatterns = [
    path('', CarpetaView.as_view(), name="carpeta")
]