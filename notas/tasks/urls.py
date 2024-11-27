from django.urls import path
from . import views #importa as views do arquivo notas

app_name = 'tasks'

urlpatterns = [
    path('notes/', views.criar_task, name="notas"),
    path('listanotas/', views.listar_task, name="lista_task"),
    path('editarnotas/<int:note_id>/', views.editarnotas, name="editarnotas"),
]
