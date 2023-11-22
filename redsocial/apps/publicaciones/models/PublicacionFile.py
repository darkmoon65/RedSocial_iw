from django.db import models
from .Publicacion import Publicacion

TIPOS = [
        (0, 'FOTO'),
        (1, 'VIDEO'),
        (2, 'GIF')
]

class PublicacionFile(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo        = models.IntegerField(null=False, choices=TIPOS)
    media       = models.FileField(null=True, blank=True, upload_to="apps/publicaciones/filesPublicaciones/")

    class Meta:
        ordering = ['publicacion', 'media']
