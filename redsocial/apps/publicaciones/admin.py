from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models.Publicacion import Publicacion
from .models.PublicacionComentario import PublicacionComentario
from .models.PublicacionFile import PublicacionFile
from .models.PublicacionReaccion import PublicacionReaccion

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['usuario_email', 'descripcion', 'fecha']
    list_filter = ['fecha']
    search_fields = ['usuario_email', 'fecha']

    def usuario_email(self, obj):
        return obj.usuario.email
    
class PublicacionComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'publicacion', 'fecha', 'descripcion')
    list_filter = ('fecha',)
    search_fields = ('usuario__email', 'fecha')
    
class PublicacionFileAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'tipo', 'get_media_preview')
    list_filter = ('tipo',)
    
    def get_media_preview(self, obj):
        if obj.media:
            if obj.tipo == 0: 
                return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.media.url)
            elif obj.tipo == 1: 
                return format_html('<video controls style="max-width: 100px; max-height: 100px;"><source src="{}" type="video/mp4"></video>', obj.media.url)
            elif obj.tipo == 2: 
                return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.media.url)
        return "N/A"
    
class PublicacionReaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'publicacion', 'reaccion', 'fecha')
    list_filter = ('fecha', 'reaccion')
    search_fields = ('usuario__email', 'publicacion__contenido')

admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(PublicacionComentario, PublicacionComentarioAdmin)
admin.site.register(PublicacionFile, PublicacionFileAdmin)
admin.site.register(PublicacionReaccion, PublicacionReaccionAdmin)
