
from .models.Amistad import Amistad
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import AmistadSerializer


class AmistadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Amistad.objects.all()
    serializer_class = AmistadSerializer

    #permission_classes = [permissions.IsAuthenticated]


# Create your views here.
