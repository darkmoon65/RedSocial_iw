from django.db import models
from apps.usuarios.models.Usuario import Usuario

ESTADOS = [
    (0, 'Pendiente'),
    (1, 'Rechazado'),
    (2, 'Aceptado')
]

class SolicitudAmistad(models.Model):
    usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitud_usuario1')
    usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitud_usuario2')
    estado   = models.IntegerField(choices=ESTADOS, default=0)
    fecha    = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    class Meta:
        ordering = ['usuario1', 'usuario2', 'estado', 'fecha']