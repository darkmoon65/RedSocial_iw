from rest_framework import serializers
from .models.Publicacion import Publicacion
from .models.PublicacionComentario import PublicacionComentario
from .models.PublicacionFile import PublicacionFile
from .models.PublicacionReaccion import PublicacionReaccion
from apps.usuarios.serializer import UsuarioSerializer

class PublicacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'fecha', 'descripcion']

class PublicacionComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionComentario
        fields = ['id', 'publicacion', 'usuario', 'fecha', 'descripcion']

class PublicacionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionFile
        fields = ['id', 'publicacion','tipo', 'media']

class PublicacionReaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionReaccion
        fields = ['id', 'publicacion', 'usuario', 'fecha', 'reaccion']