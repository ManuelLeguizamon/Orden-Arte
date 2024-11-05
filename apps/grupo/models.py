from django.db import models
from apps.usuario.models import Usuario


class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    listaCanciones = models.TextField()
    usuarios = models.ManyToManyField(Usuario, related_name='grupos')
    foto_grupo = models.ImageField(upload_to='grupos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
