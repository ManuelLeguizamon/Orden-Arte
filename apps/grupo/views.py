from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import CrearGrupoForm
from .models import Grupo
from django.contrib.auth.models import User  
# from apps.usuario.models import Usuario 
from apps.evento.forms import EventoForm
from apps.evento.models import Evento
from apps.carpeta.models import Carpeta
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin



class GrupoView(LoginRequiredMixin, TemplateView):
    template_name='grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        # context['grupos'] = Grupo.objects.filter(userDueño=id_usuario).all() 
        # context['grupos'] = Grupo.objects.all()   
        context['grupos'] = self.request.user.grupos.all()

        return context 
    
    def post(self, request, *args, **kwargs):
        if 'borrar_grupo_id' in kwargs:
            grupo = get_object_or_404(Grupo, id=kwargs['borrar_grupo_id'])     
            grupo.delete()
            return redirect('grupo')



class CrearGrupoView(LoginRequiredMixin, FormView):
    template_name = 'crear_grupo.html'
    form_class = CrearGrupoForm
    success_url = reverse_lazy('grupo') 

    
    def form_valid(self, form):
        grupoNuevo= form.save(commit=False)
        grupoNuevo.userDueño = self.request.user
        grupoNuevo.save()
        return super().form_valid(form) 



#----- TEMPLATE QUE CADA GRUPO TIENE QUE TENER PARA CONTENER TODA SU INFO
class NuevoGrupoView(LoginRequiredMixin, TemplateView):
    template_name='nuevo_grupo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        grupo = get_object_or_404(Grupo, id=grupo_id, userDueño=self.request.user)
        context['grupo'] = grupo
        context['eventos']= Evento.objects.filter(grupo=grupo_id, grupo__userDueño=self.request.user).all()
        context['carpetas'] = Carpeta.objects.filter(grupo=grupo_id).all()
        return context
        
    def post(self, request, *args, **kwargs):
        if 'borrar_evento_id' in kwargs:
            evento = get_object_or_404(Evento, id=kwargs['borrar_evento_id'])
            evento.delete()
            return redirect('nuevo-grupo', grupo_id=kwargs['grupo_id'])
        elif 'borrar_carpeta_id' in kwargs:
            carpeta = get_object_or_404(Carpeta, id=kwargs['borrar_carpeta_id'])
            carpeta.delete()
            return redirect('nuevo-grupo', grupo_id=kwargs['grupo_id'])

