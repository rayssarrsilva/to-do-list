# forms.py
from django import forms
from .models import notes

class NotasForm(forms.ModelForm): # Formulario que lida com a criação e edição de notas
    class Meta: # especifica o modelo e os campos que o formulário irá manipular
        model = notes # nome do model previamente criado
        fields = ['title', 'content',  'prioridade', 'completed', 'color'] # nome dos fields que serão criados junto
    
