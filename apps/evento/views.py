from django.shortcuts import render
from django.views.generic import TemplateView

class EventoView(TemplateView):
    template_name='evento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        context["alumnos"] = Alumno.objects.all().etcetera(filter, order_by, etc)......
        return context
        """ 
