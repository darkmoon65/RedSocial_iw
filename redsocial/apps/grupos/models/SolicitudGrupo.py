from django.db import models
from apps.usuarios.models.Usuario import Usuario

ESTADOS = [
        (0, 'Pendiente'),
        (1, 'Rechazado'),
        (2, 'Aceptado')
]

class SolicitudGrupo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado  = models.IntegerField(choices=ESTADOS, default=0)
    fecha   = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    class Meta:
        ordering = ['usuario', 'estado', 'fecha']
