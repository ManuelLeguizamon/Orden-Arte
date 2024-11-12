from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy, reverse
from .forms import EventoForm, HorarioForm, LocalidadForm
from .models import Evento, Horario
from django.shortcuts import get_object_or_404, redirect, render
from apps.grupo.models import Grupo

#----------------------------------------------------------------------------------------------------------------------------

class EventoView(TemplateView):
    template_name='evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos']= Evento.objects.all()
        
        return context

#----------------------------------------------------------------------------------------------------------------------------
class EventoDetalleView(TemplateView):
    template_name = 'evento-detalle.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento_id = self.kwargs['evento_id']
        evento = get_object_or_404(Evento, id=evento_id)
        context['evento_id'] = evento_id
        context['detalles'] = Evento.objects.filter(id=evento_id).all()
        context['nombre'] = evento.nombre
        context['fecha'] = evento.fecha
        context['dineroCobrar'] = evento.dineroCobrar
        context['tipo'] = evento.tipo
        context['vestimenta'] = evento.vestimenta
        context['horarioLlegada'] = '...'
        context['horarioPrueba'] = '...'
        context['horarioTocar'] = '...'
        return context
#----------------------------------------------------------------------------------------------------------------------------

class CrearEventoView(FormView):
    template_name = 'crear-evento.html'
    form_class = EventoForm

    def form_valid(self, form):
        grupo = get_object_or_404(Grupo, id=self.kwargs['grupo_id'])
        evento = form.save(commit=False)
        evento.grupo = grupo
        evento.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupo_id'] = self.kwargs['grupo_id']
        context['eventoForm'] = EventoForm()
        context['horarioForm'] = HorarioForm()
        context['localidadForm'] = LocalidadForm()
        return context  
    
    def get_success_url(self):
        grupo_id = self.kwargs['grupo_id']
        return reverse_lazy('nuevo-grupo', kwargs={'grupo_id': grupo_id})
#----------------------------------------------------------------------------------------------------------------------------

