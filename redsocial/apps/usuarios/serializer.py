from .models.Usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellidos', 'fecha_reg','genero', 'passw', 'imagen_perfil', 'fecha_nac', 'ultima_conexion']
