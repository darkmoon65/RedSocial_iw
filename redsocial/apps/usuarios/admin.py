from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models.Usuario import Usuario

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('imagen_perfil_display', 'email', 'nombre', 'apellidos', 'fecha_reg', 'genero', 'fecha_nac', 'ultima_conexion')
    search_fields = ['email', 'nombre', 'apellidos']
    
    def imagen_perfil_display(self, obj):
        if obj.imagen_perfil:
            print(obj.imagen_perfil.url)
            url = "usuarios/imagenesPerfil/profile11.png"
            return format_html('<img src="{}" width="50" height="50" />', obj.imagen_perfil.url)
        else:
            return "Sin imagen"
        
    imagen_perfil_display.allow_tags = True
    imagen_perfil_display.short_description = 'Imagen de perfil'
    
admin.site.register(Usuario, UsuariosAdmin)