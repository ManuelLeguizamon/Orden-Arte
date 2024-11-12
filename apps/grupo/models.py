from django.db import models
from apps.usuario.models import Usuario


class Grupo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    listaCanciones = models.TextField(null=True, blank=True)
    userDueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='grupos', null=True, blank=True)

    def __str__(self):
        return self.nombre
