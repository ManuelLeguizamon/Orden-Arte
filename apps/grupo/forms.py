from django.forms import ModelForm
from .models import Grupo   
from django.contrib.auth.models import User  

class CrearGrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre']

