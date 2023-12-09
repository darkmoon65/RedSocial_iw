from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# defailt blank=False, null=False -> no puede ser vacio, obligatorio

GENEROS = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro')
]

class Usuario(models.Model):
    email           = models.EmailField(max_length=155)
    nombre          = models.CharField(max_length=155)
    apellidos       = models.CharField(max_length=155)
    fecha_reg       = models.DateTimeField(editable=False, auto_now_add=True) 
    genero          = models.CharField(max_length=1, choices=GENEROS)
    passw           = models.CharField(max_length=155)
    imagen_perfil   = models.ImageField(upload_to='apps/usuarios/imagenesPerfil/', blank=True, null=True)
    fecha_nac       = models.DateField(blank=True, null=True, editable=True)
    ultima_conexion = models.DateTimeField(blank=True, null=True, editable=True, auto_now=True)
    
    class Meta:
        # exclude = ['fecha_reg', 'ultima_conexion']
        ordering = ['email', 'nombre', 'apellidos', 'genero', 'ultima_conexion']
        
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellidos = self.apellidos.upper()
        return super(Usuario, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.email} {self.nombre} {self.apellidos} {self.genero}'