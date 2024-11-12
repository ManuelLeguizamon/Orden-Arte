from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import CrearGrupoForm
from .models import Grupo
from django.contrib.auth.models import User  
from apps.usuario.models import Usuario 
from apps.evento.forms import EventoForm
from apps.evento.models import Evento
from apps.carpeta.models import Carpeta
from django.shortcuts import get_object_or_404


class GrupoView(TemplateView):
    template_name='grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupos'] = Grupo.objects.all()      
        return context 



class CrearGrupoView(FormView):
    template_name = 'crear_grupo.html'
    form_class = CrearGrupoForm
    success_url = reverse_lazy('grupo') 

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



#----- TEMPLATE QUE CADA GRUPO TIENE QUE TENER PARA CONTENER TODA LA INFO
class NuevoGrupoView(TemplateView):
    template_name='nuevo_grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        grupo = get_object_or_404(Grupo, id=grupo_id)
        context['grupo'] = grupo
        context['eventos']= Evento.objects.filter(grupo=grupo_id).all()
        context['carpetas'] = Carpeta.objects.filter(grupo=grupo_id).all()
        return context

