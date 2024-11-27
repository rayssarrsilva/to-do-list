from django.db import models

# Create your models here.

class notes(models.Model):
    title = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    opcoes_prioridade = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'), # valor armazenado no bd x valor exibido para o usuario
      ]
    prioridade = models.CharField(
        max_length=6,
        blank = True,
        choices = opcoes_prioridade,
        default = 'prioridade não definida'
      )
    color = models.CharField(max_length=7, default='#FFFFFF') #permite ao usuario mudar a cor
    def __str__(self):
            return self.title
