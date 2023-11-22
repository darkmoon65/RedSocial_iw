from .models.Usuario import Usuario
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Create your views here.
