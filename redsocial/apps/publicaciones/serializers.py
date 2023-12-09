from rest_framework import serializers
from .models.Publicacion import Publicacion
from .models.PublicacionComentario import PublicacionComentario
from .models.PublicacionFile import PublicacionFile
from .models.PublicacionReaccion import PublicacionReaccion
from apps.usuarios.serializer import UsuarioSerializer
from apps.usuarios.models.Usuario import Usuario

class PublicacionSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'fecha', 'descripcion']
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        validated_data['usuario'] = usuario_data
        publicacion = Publicacion.objects.create(**validated_data)

        return publicacion
class PublicacionComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionComentario
        fields = ['id', 'publicacion', 'usuario', 'fecha', 'descripcion']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        validated_data['usuario'] = usuario_data
        publicacion = PublicacionComentario.objects.create(**validated_data)

        return publicacion

class PublicacionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionFile
        fields = ['id', 'publicacion','tipo', 'media']

class PublicacionReaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionReaccion
        fields = ['id', 'publicacion', 'usuario', 'fecha', 'reaccion']