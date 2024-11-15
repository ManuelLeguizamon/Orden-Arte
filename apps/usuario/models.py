"""from django.db import models

class Usuario(models.Model):
    roll_opciones=[
        ('administrador', 'Administrador'), 
        ('invitado', 'Invitado'), 
    ]
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    contraseña = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    roll = models.CharField(max_length=20, choices=roll_opciones, null=True, blank=True, default='invitado')
    foto_perfil = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre"""