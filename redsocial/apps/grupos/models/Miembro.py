from django.db import models
from .Grupo import Grupo  
from apps.usuarios.models.Usuario import Usuario

class Miembro(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('mod', 'Moderador'),
        ('miembro', 'Miembro'),
    )
    
    grupo         = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    usuario       = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol           = models.CharField(max_length=50, choices=ROLES, default='miembro')
    fecha_entrada = models.DateField(auto_now=True, editable=False)
    fecha_ult_con = models.DateField(auto_now=True, editable=True)

    class Meta:
        ordering = ['grupo', 'usuario', 'rol', 'fecha_entrada', 'fecha_ult_con']

    def __str__(self):
        return f"Miembro de {self.grupo.nombre} - {self.usuario.nombre} - {self.rol}"
