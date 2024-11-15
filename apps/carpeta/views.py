from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import  CarpetaForm, SubirArchivoForm
from django.shortcuts import get_object_or_404
from apps.grupo.models import Grupo
from .models import Carpeta, Multimedia
from django.contrib.auth.mixins import LoginRequiredMixin

class CarpetaView(LoginRequiredMixin, TemplateView):
    template_name='carpeta.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carpeta_id = self.kwargs['carpeta_id']
        carpeta = get_object_or_404(Carpeta, id=carpeta_id)
        grupo_id = self.kwargs['grupo_id']
        grupo = get_object_or_404(Grupo, id=grupo_id, userDueño=self.request.user)
        context['carpeta_nombre'] = carpeta.nombre
        context['grupo_id'] = grupo_id
        context['carpeta_id'] = carpeta_id
        context['carpetas'] = Carpeta.objects.filter(id=carpeta_id).all()
        context['archivos'] = Multimedia.objects.filter(carpeta=carpeta_id).all()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'eliminar_archivo_id' in kwargs:
            archivo = get_object_or_404(Multimedia, id=kwargs['eliminar_archivo_id'])
            archivo.delete()
            return redirect('carpeta', grupo_id=self.kwargs['grupo_id'], carpeta_id=self.kwargs['carpeta_id'])



class SubirArchivoView(LoginRequiredMixin, FormView):
    template_name='subir-archivo.html'
    form_class = SubirArchivoForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        carpeta_id = self.kwargs['carpeta_id']
        context['grupo_id'] = grupo_id
        context['carpeta_id'] = carpeta_id
        return context
    
    def form_valid(self, form):
        carpeta_id = self.kwargs.get('carpeta_id')
        carpeta = get_object_or_404(Carpeta, id=carpeta_id, grupo__userDueño=self.request.user)
        carpetaForm = form.save(commit=False)
        carpetaForm.carpeta = carpeta
        carpetaForm.save()
        return super().form_valid(form) 
    
    def get_success_url(self):
        grupo_id = self.kwargs['grupo_id']
        carpeta_id = self.kwargs['carpeta_id']
        return reverse_lazy('carpeta', kwargs={'grupo_id': grupo_id, 'carpeta_id': carpeta_id})

class CrearCarpetaView(LoginRequiredMixin, FormView):
    template_name = 'crear-carpeta.html'
    form_class = CarpetaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['grupo_id']
        grupo = get_object_or_404(Grupo, id=grupo_id, userDueño=self.request.user)
        context['grupo'] = grupo
        context['carpetas'] = Carpeta.objects.all()
        return context

    def form_valid(self, form):
        grupo_id = self.kwargs.get('grupo_id')
        grupo = get_object_or_404(Grupo, id=grupo_id)
        carpeta = form.save(commit=False)
        carpeta.grupo = grupo
        carpeta.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        grupo_id = self.kwargs['grupo_id']
        return reverse_lazy('nuevo-grupo', kwargs={'grupo_id': grupo_id})
    
