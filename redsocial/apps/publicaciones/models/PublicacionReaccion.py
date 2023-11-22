from django.db import models
from apps.usuarios.models.Usuario import Usuario
from .Publicacion import Publicacion

REACCIONES = [
    (0, 'Me divierte'),
    (1, 'Me enoja'),
    (2, 'Me entristese'),
    (3, 'Me gusta'),
    (4, 'Me encorazona'),
    (5, 'No me Gusta')
]

class PublicacionReaccion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha       = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    reaccion    = models.IntegerField(null=False, choices=REACCIONES)

    class Meta:
        ordering = ['publicacion', 'usuario', 'fecha', 'reaccion']
