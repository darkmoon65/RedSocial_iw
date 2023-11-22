from django.contrib import admin

# Register your models here.
from .models.Amistad import Amistad
from .models.SolicitudAmistad import SolicitudAmistad

class AmistadAdmin(admin.ModelAdmin):
    list_display = ['usuario1', 'usuario2', 'fecha_inicio']
    list_filter = ['usuario1', 'usuario2']
    search_fields = ['usuario1__email', 'usuario2__email']

class SolicitudAmistadAdmin(admin.ModelAdmin):
    list_display = ['usuario1', 'usuario2', 'estado', 'fecha']
    list_filter = ['usuario1', 'usuario2', 'estado']
    search_fields = ['usuario1__email', 'usuario2__email']

admin.site.register(Amistad, AmistadAdmin)
admin.site.register(SolicitudAmistad, SolicitudAmistadAdmin)