from django.db import models
from apps.usuarios.models.Usuario import Usuario


class Amistad(models.Model):
    usuario1     = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amistad_usuario1')
    usuario2     = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amistad_usuario2')
    fecha_inicio = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['usuario1', 'usuario2', 'fecha_inicio']
