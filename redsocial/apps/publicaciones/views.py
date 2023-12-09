from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models.Publicacion import Publicacion
from .serializers import PublicacionSerializer
from .models.PublicacionComentario import PublicacionComentario
from .serializers import PublicacionComentarioSerializer
from .models.PublicacionFile import PublicacionFile
from .serializers import PublicacionFileSerializer
from .models.PublicacionReaccion import PublicacionReaccion
from .serializers import PublicacionReaccionSerializer
from apps.usuarios.serializer import UsuarioSerializer
from django.core.files.uploadedfile import SimpleUploadedFile

@csrf_exempt
def publicacion_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        publicacions = Publicacion.objects.all()
        serializer = PublicacionSerializer(publicacions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def publicacion_detail(request, pk):
    """
    Retrieve, update or delete a code publicacion.
    """
    try:
        publicacion = Publicacion.objects.get(pk=pk)
    except publicacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PublicacionSerializer(publicacion)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublicacionSerializer(publicacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publicacion.delete()
        return HttpResponse(status=204)
    


@csrf_exempt
def publicacionComentario_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        publicacionComens = PublicacionComentario.objects.all()
        serializer = PublicacionComentarioSerializer(publicacionComens, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicacionComentarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def publicacionComentario_detail(request, pk):
    """
    Retrieve, update or delete a code publicacion.
    """
    try:
        publicacion = PublicacionComentario.objects.get(pk=pk)
    except publicacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PublicacionComentarioSerializer(publicacion)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublicacionComentarioSerializer(publicacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publicacion.delete()
        return HttpResponse(status=204)
    

@csrf_exempt
def publicacionFile_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        publicacionFiles = PublicacionFile.objects.all()
        serializer = PublicacionFileSerializer(publicacionFiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        media_file = request.FILES['media']
        print(media_file)
        publicacion = request.POST.get('publicacion', '')
        tipo = request.POST.get('tipo', '')

        serializer_data = {
            'media': SimpleUploadedFile(media_file.name, media_file.read(), media_file.content_type),
            'publicacion': publicacion,
            'tipo': tipo
        }
        # data = JSONParser().parse(request)
        serializer = PublicacionFileSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def publicacionFile_detail(request, pk):
    """
    Retrieve, update or delete a code publicacion.
    """
    try:
        publicacion = PublicacionFile.objects.get(pk=pk)
    except publicacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PublicacionFileSerializer(publicacion)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublicacionFileSerializer(publicacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publicacion.delete()
        return HttpResponse(status=204)

@csrf_exempt
def publicacionReaccion_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        publicacionReaccions = PublicacionReaccion.objects.all()
        serializer = PublicacionReaccionSerializer(publicacionReaccions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicacionReaccionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def publicacionReaccion_detail(request, pk):
    """
    Retrieve, update or delete a code publicacion.
    """
    try:
        publicacion = PublicacionReaccion.objects.get(pk=pk)
    except publicacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PublicacionReaccionSerializer(publicacion)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublicacionReaccionSerializer(publicacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publicacion.delete()
        return HttpResponse(status=204)