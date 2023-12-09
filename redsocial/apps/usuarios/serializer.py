from .models.Usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre', 'apellidos', 'fecha_reg','genero', 'passw', 'imagen_perfil', 'fecha_nac', 'ultima_conexion']
