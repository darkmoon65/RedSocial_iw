from django.db import models
from .SalaChatGrupo import SalaChatGrupo
from .Miembro import Miembro

class MiembrosSala(models.Model):
    num_sala = models.ForeignKey(SalaChatGrupo, on_delete=models.CASCADE)
    usuario  = models.ForeignKey(Miembro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Usuario {self.usuario} en Sala {self.num_sala.id}"
