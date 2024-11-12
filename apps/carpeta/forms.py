from django.forms import ModelForm
from .models import Carpeta, Multimedia
from django import forms

class CarpetaForm(ModelForm):
    class Meta:
        model = Carpeta
        fields = ['nombre']
    
class SubirArchivoForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['nombreMultimedia', 'archivo',]
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,audio/mpeg'}))

