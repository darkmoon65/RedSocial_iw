from .models.Amistad import Amistad
from rest_framework import serializers

class AmistadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amistad
        fields = ['usuario1', 'usuario2', 'fecha_inicio']
