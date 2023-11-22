from django.db import models
from apps.usuarios.models.Usuario import Usuario


class Chat(models.Model):
    usuario1     = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chat_usuario1')
    usuario2     = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chat_usuario2')
    fecha_inicio = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['usuario1', 'usuario2', 'fecha_inicio']

    def __str__(self):
        return f'{self.id} {self.usuario1.nombre} <-> {self.usuario2.nombre} '