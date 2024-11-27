from django.contrib import admin
from .models import notes

@admin.register(notes) #decorador - modifica ou adiciona funcionalidades a funções ou classes de forma simples e legível, sem alterar diretamente o código original.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', 'content') 
    search_fields = ('title', 'content') 