from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy, reverse
from .forms import EventoForm, HorarioForm, LocalidadForm
from .models import Evento, Horario, Localidad
from django.shortcuts import get_object_or_404, redirect, render
from apps.grupo.models import Grupo
from django.contrib.auth.mixins import LoginRequiredMixin

#----------------------------------------------------------------------------------------------------------------------------

class EventoView(LoginRequiredMixin, TemplateView):
    template_name='evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(grupo__userDueño=self.request.user).all()      
        return context

#----------------------------------------------------------------------------------------------------------------------------
class EventoDetalleView(LoginRequiredMixin, TemplateView):
    template_name = 'evento-detalle.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento_id = self.kwargs['evento_id']
        grupo_id = self.kwargs['grupo_id']
        evento = get_object_or_404(Evento, id=evento_id, grupo__userDueño=self.request.user)
        horarios = evento.horario
        localidad = evento.localidad
        context['evento'] = evento
        context['evento_id'] = evento_id
        context['detalles'] = Evento.objects.filter(id=evento_id, grupo__userDueño=self.request.user).all()
        context['nombre'] = evento.nombre
        context['fecha'] = evento.fecha
        context['dineroCobrar'] = evento.dineroCobrar
        context['tipo'] = evento.tipo
        context['vestimenta'] = evento.vestimenta
        context['horarioLlegada'] = horarios.horarioLlegada 
        context['horarioPrueba'] = horarios.horarioPruebaSonido
        context['horarioTocar'] = horarios.horarioTocar 
        context['pais'] = localidad.pais
        context['ciudad'] = localidad.ciudad
        context['direccion'] = localidad.direccion 
        return context


#----------------------------------------------------------------------------------------------------------------------------

class CrearEventoView(LoginRequiredMixin, FormView):
    template_name = 'crear-evento.html'
    form_class = EventoForm

    def form_valid(self, form):
        grupo = get_object_or_404(Grupo, id=self.kwargs['grupo_id'])
        horario_form = HorarioForm(self.request.POST)
        horario = horario_form.save()
        localidad_form = LocalidadForm(self.request.POST)
        localidad = localidad_form.save()
        evento = form.save(commit=False)
        evento.grupo = grupo
        evento.horario = horario
        evento.localidad = localidad
        evento.save()
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        grupo = get_object_or_404(Grupo, id=grupo_id)
        context['grupo_id'] = grupo_id
        context['eventoForm'] = EventoForm()
        context['horarioForm'] = HorarioForm()
        context['localidadForm'] = LocalidadForm()
        return context

    def get_success_url(self):
        grupo_id = self.kwargs['grupo_id']
        return reverse_lazy('nuevo-grupo', kwargs={'grupo_id': grupo_id})
#----------------------------------------------------------------------------------------------------------------------------

class ModificarEventoView(LoginRequiredMixin, FormView):
    template_name = 'modificar-evento.html'
    form_class = EventoForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        evento_id = self.kwargs['evento_id']        
        context['grupo_id'] = grupo_id
        context['evento_id'] = evento_id

        evento = get_object_or_404(Evento, id=evento_id)
        context['eventoForm'] = EventoForm(instance=evento)

        horario_id = evento.horario.pk
        horario = get_object_or_404(Horario, id=evento.horario_id) #Se agrego evento. al id=evento.horario_id
        context['horarioForm'] = HorarioForm(instance=horario)

        localidad_id = evento.localidad.pk
        localidad = get_object_or_404(Localidad, id=evento.localidad_id)#Se agrego evento. al id=evento.localidad_id
        context['localidadForm'] = LocalidadForm(instance=localidad)

        return context

    def form_valid(self, form):        
        grupo = get_object_or_404(Grupo, id=self.kwargs['grupo_id'], userDueño=self.request.user)
        evento = get_object_or_404(Evento, id=self.kwargs['evento_id'])

        horario = get_object_or_404(Horario, id=evento.horario.id)
        horarioForm = HorarioForm(self.request.POST, instance=horario)
        if horarioForm.is_valid():
            horarioForm.save()

        localidad = get_object_or_404(Localidad, id=evento.localidad.id)
        localidadForm = LocalidadForm(self.request.POST, instance=localidad)
        if localidadForm.is_valid():
            localidadForm.save()

        eventoForm = EventoForm(self.request.POST, instance=evento)
        if eventoForm.is_valid():
            eventoForm.save()

        form.instance = evento # Enlaza el formulario al evento original
        evento = form.save(commit=False)
        evento.horario = horario
        evento.localidad = localidad
        evento.grupo = grupo
        evento.fecha = evento.fecha
        evento.tipo = evento.tipo
        evento.vestimenta = evento.vestimenta
        evento.dineroCobrar = evento.dineroCobrar
        evento.nombre = evento.nombre
        evento.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        grupo_id = self.kwargs['grupo_id']
        return reverse_lazy('nuevo-grupo', kwargs={'grupo_id': grupo_id})