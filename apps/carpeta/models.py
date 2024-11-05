from django.db import models
from apps.grupo.models import Grupo

class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    partitura = models.FileField(upload_to='partituras/')
    fechaCarga = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='carpetas')

    def __str__(self):
        return self.nombre
#----------------------------------------------------------------------------------------------------------------------
class Multimedia(models.Model):
    nombreMultimedia = models.CharField(max_length=20)
    archivo = models.FileField()
    fechaSubida = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='multimedias')
    
    def __str__(self):
        return self.nombreMultimedia