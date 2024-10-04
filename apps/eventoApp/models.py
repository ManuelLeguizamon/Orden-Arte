from django.db import models


class LocalidadModel(models.Model):
    pais = models.CharField(max_length=35)
    ciudad = models.CharField(max_length=35)
    direccion = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.ciudad}, {self.direccion}"
#---------------------------------------------------------------------------------------------------

class EventoTipoModel(models.Model):
    eventoTipoOpciones = [
        ('ensayo', 'Ensayo'),
        ('grabacion', 'Grabacion'),
        ('show', 'Show'),
        ('otro', 'Otro')
    ]
    eventoTipo = models.CharField(max_length=10, choices=eventoTipoOpciones, unique=False, default='otro')

    def __str__(self):
        return self.eventoTipo
#---------------------------------------------------------------------------------------------------

class VestimentaModel(models.Model):
    vestimentaOpciones = [
        ('formal', 'Formal'), 
        ('informal', 'Informal'), 
        ('disfraz', 'Disfraz'), 
        ('libre', 'Libre')
    ]
    vestimenta = models.CharField(max_length=8, choices=vestimentaOpciones, unique=True, default='libre')

    def __str__(self):
        return self.vestimenta
#---------------------------------------------------------------------------------------------------

class HorarioModel(models.Model):
    horarioLlegada = models.DateField(null=True, blank=True)
    horarioPruebaSonido = models.DateField(null=True, blank=True)
    horarioTocar = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Horario de tocar: {self.horarioTocar}"
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class EventoModel(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    dineroCobrar = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    localidad = models.ForeignKey(LocalidadModel, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    tipo = models.ForeignKey(EventoTipoModel, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    vestimenta = models.ForeignKey(VestimentaModel, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    horario = models.ForeignKey(HorarioModel, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}: {self.tipo}"