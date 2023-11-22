from django.db import models
from .Grupo import Grupo


class SalaChatGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grupo.id}: {self.grupo.nombre}'