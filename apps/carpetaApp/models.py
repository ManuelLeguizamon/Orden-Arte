from django.db import models
from apps.grupoApp.models import GrupoModel 

class CarpetaModel(models.Model):
    nombre = models.CharField(max_length=100)
    partitura = models.FileField(upload_to='partituras/')
    fechaCarga = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(GrupoModel, on_delete=models.CASCADE, related_name='carpetas')

    def __str__(self):
        return self.nombre
#----------------------------------------------------------------------------------------------------------------------
class MultimediaModel(models.Model):
    nombreMultimedia = models.CharField(max_length=20)
    archivo = models.FileField()
    fechaSubida = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(CarpetaModel, on_delete=models.CASCADE, related_name='multimedias')
    
    def __str__(self):
        return self.nombreMultimedia