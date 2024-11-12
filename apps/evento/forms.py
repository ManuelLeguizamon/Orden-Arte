from django.forms import ModelForm
from .models import Evento, Horario, Localidad, EventoTipo, Vestimenta
from django import forms

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'dineroCobrar', 'tipo', 'vestimenta']
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tipo = forms.ModelChoiceField(queryset=EventoTipo.objects.all(), required=False)
    vestimenta = forms.ModelChoiceField(queryset=Vestimenta.objects.all(), required=False)
    
    

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['horarioLlegada', 'horarioPruebaSonido', 'horarioTocar']
    horarioLlegada = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    horarioPruebaSonido = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    horarioTocar = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = ['pais', 'ciudad', 'direccion']
    pais = forms.CharField(required=False)
    ciudad = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
