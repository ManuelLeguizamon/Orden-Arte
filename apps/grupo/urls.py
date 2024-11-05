from django.urls import path
from apps.grupo.views import GrupoView
urlpatterns = [
    path('', GrupoView.as_view(), name='grupo')
]