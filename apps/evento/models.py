from django.db import models


class Localidad(models.Model):
    pais = models.CharField(max_length=35)
    ciudad = models.CharField(max_length=35)
    direccion = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.ciudad}, {self.direccion}"
#---------------------------------------------------------------------------------------------------

class EventoTipo(models.Model):
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

class Vestimenta(models.Model):
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

class Horario(models.Model):
    horarioLlegada = models.TimeField(null=True, blank=True)
    horarioPruebaSonido = models.TimeField(null=True, blank=True)
    horarioTocar = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Horario de tocar: {self.horarioTocar}"
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class Evento(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    dineroCobrar = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    tipo = models.ForeignKey(EventoTipo, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    vestimenta = models.ForeignKey(Vestimenta, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='eventos', null=True, blank=True)
    grupo = models.ForeignKey("grupo.Grupo", on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return f"{self.nombre}: {self.tipo}"