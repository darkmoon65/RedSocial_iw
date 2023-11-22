from django.contrib import admin

# Register your models here.
from .models.Chat import Chat
from .models.MensajeChat import MensajeChat


class ChatAdmin(admin.ModelAdmin):
    list_display = ['usuario1', 'usuario2', 'fecha_inicio']
    search_fields = ['usuario1', 'usuario2', 'fecha_inicio']

class MensajeChatAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'usuario', 'fecha', 'mensaje_text']
    list_filter = ['fecha', 'usuario']
    search_fields = ['fecha', 'usuario__email']

admin.site.register(Chat, ChatAdmin)
admin.site.register(MensajeChat, MensajeChatAdmin)