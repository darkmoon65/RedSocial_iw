from django.db import models
from apps.usuarios.models.Usuario import Usuario


class Publicacion(models.Model):
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha       = models.DateTimeField(editable=False, auto_now_add=True)
    descripcion = models.TextField()

    class Meta:
        ordering = ['usuario', 'fecha', 'descripcion']

    def __str__(self) :
        return f"{self.usuario.email} {self.fecha} {self.descripcion}"
