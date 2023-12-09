from .models.Usuario import Usuario
from rest_framework import permissions
from .serializer import UsuarioSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView
from .authSerializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

@csrf_exempt
def usuario_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        print(data)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_login(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)
        user = Usuario.objects.get(email=data['correo'])

        if (user.passw == data['contrasena']):
            refresh = RefreshToken.for_user(user)
            print(refresh.access_token)
            return JsonResponse({'message': 'ok', 'access': str(refresh.access_token), 'email': user.email}, status=201)
        return JsonResponse({'message': 'error'}, status=400)


@csrf_exempt
def get_user_by_email(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)
        user = Usuario.objects.get(email=data['correo'])

        if (user):
            serializer = UsuarioSerializer(user)
            return JsonResponse({'message': 'ok', 'user': serializer.data}, status=201)
        return JsonResponse({'message': 'error'}, status=400)
