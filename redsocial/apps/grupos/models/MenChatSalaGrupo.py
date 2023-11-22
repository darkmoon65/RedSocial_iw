from django.db import models
from .MiembrosSala import MiembrosSala
from apps.usuarios.models.Usuario import Usuario


class MenChatSalaGrupo(models.Model):
    num_sala = models.ForeignKey(MiembrosSala, on_delete=models.CASCADE)
    usuario  = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje  = models.TextField()
    fecha    = models.DateField(auto_now=True, editable=False)


    class Meta:
        #exclude = ['fecha']
        ordering = ['num_sala', 'usuario', 'fecha', 'mensaje']