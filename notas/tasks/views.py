from django.shortcuts import render, get_object_or_404, redirect
from .models import notes 
from .forms import NotasForm  #Formulário que cria/edita uma nota

def criar_task(request):
    if request.method == 'POST': #se o metodo request é POST (envia dados para o server, por meio de uma ação  (formulario nesse caso))
        form = NotasForm(request.POST)
        if form.is_valid(): #se o formulário for validado então, tudo é salvo.
            form.save()
            return redirect('notes/lista_notas')  #Redireciona para a lista de notas
    else:
        form = NotasForm() #cria um formulario vazio, caso seja GET (ocorre ao carregar uma página pela primeira vez)
    return render(request, 'notes/notes.html', {'create_form': form})


def editarnotas(request, note_id): #note_id: localiza o objeto no banco de dados
    note = get_object_or_404(notes, id=note_id) #note: variavel, get_object_or_404: função(busca o objeto se nao encontra retorna erro 404), notes: class model, id: parametro que localiza id.
    if request.method == 'POST': 
        form = NotasForm(request.POST, instance=note) #NotasForm: forms.py criado, request.POST: dados enviados pelo usuário, instance=note: parametro que preenche previamente o form com dados existentes
        if form.is_valid():
            form.save()
            return redirect('notes/lista_notas')  # Redireciona após editar
    else:
        form = NotasForm(instance=note)
    return render(request, 'notes/lista_notas.html', {'edit_form': form, 'note': note})


def deletar_task(request, note_id):
    note = get_object_or_404(notes, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes/lista_notas')  # Redireciona para a lista de notas após excluir
    return render(request, 'notes/lista_notas.html', {'delete_note': note})

def listar_task(request):
    all_notes = notes.objects.all()  # Busca todas as notas no banco de dados
    return render(request, 'notes/lista_notas.html', {'notes': all_notes})
