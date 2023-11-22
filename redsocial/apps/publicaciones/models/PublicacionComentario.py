from django.db import models
from apps.usuarios.models.Usuario import Usuario
from .Publicacion import Publicacion


class PublicacionComentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha       = models.DateTimeField(editable=False, auto_now_add=True)
    descripcion = models.TextField()

    class Meta:
        ordering = ['publicacion', 'usuario', 'fecha', 'descripcion']
