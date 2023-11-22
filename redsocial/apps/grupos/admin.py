from django.contrib import admin

# Register your models here.
from .models.Grupo import Grupo
from .models.MenChatSalaGrupo import MenChatSalaGrupo
from .models.Miembro import Miembro
from .models.MiembrosSala import MiembrosSala
from .models.SalaChatGrupo import SalaChatGrupo
from .models.SolicitudGrupo import SolicitudGrupo

class GrupoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_crea', 'creador']
    search_fields = ['nombre', 'creador__email']

class MenChatSalaGrupoAdmin(admin.ModelAdmin):
    list_display = ['num_sala', 'usuario', 'mensaje', 'fecha']
    list_filter = ['num_sala', 'usuario']
    # search_fields = ['sala_grupo__nombre', 'usuario__email', 'mensaje']

class MiembroAdmin(admin.ModelAdmin):
    list_display = ['grupo', 'usuario', 'rol', 'fecha_entrada', 'fecha_ult_con']
    list_filter = ['grupo', 'rol']
    search_fields = ['usuario__email']

class MiembrosSalaAdmin(admin.ModelAdmin):
    list_display = ['num_sala', 'usuario']
    list_filter = ['num_sala', 'usuario']
    # search_fields = ['sala__nombre', 'miembro__usuario__email']

class SalaChatGrupoAdmin(admin.ModelAdmin):
    list_display = ['id', 'grupo']
    search_fields = ['grupo__fecha_crea']

class SolicitudGrupoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'estado']
    list_filter = ['estado']
    # search_fields = ['grupo__nombre', 'usuario__email']

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(MenChatSalaGrupo, MenChatSalaGrupoAdmin)
admin.site.register(Miembro, MiembroAdmin)
admin.site.register(MiembrosSala, MiembrosSalaAdmin)
admin.site.register(SalaChatGrupo, SalaChatGrupoAdmin)
admin.site.register(SolicitudGrupo, SolicitudGrupoAdmin)