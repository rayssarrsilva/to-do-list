from django.shortcuts import render, redirect #se o user for enviado com sucesso sera redirecionado para outra pagina
from django.shortcuts import render #renderiza os templates. return render(request, endereço)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #importa biblioteca pra criar registro do user e a pra fazer a autenticação do layout de login nesse caso
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout 
# Create your views here.

from django.http import HttpResponse 

def registro(request):
    if request.method == "POST": # se o form de html for enviado com o metodo POST
        form = UserCreationForm(request.POST) #request.post = informação recebida no form. form submitted with the information
        if form.is_valid():
            #form.save()
            login(request, form.save())
            return redirect("/layout/") #Ou nome do app dado a url, e atributo dado como name na url user/urls.py
    else:
        form = UserCreationForm() #cria a variavel pra criação do layout do user
   
    return render(request, "registro/register.html", {"form": form }) #passa o form pro template

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) # LOGA: pega a variavel form, que autentica o usuario e chama a função get user
            return redirect("/layout/")
    else:
        form = AuthenticationForm() 
    return render(request, "login/login.html", {"form": form}) # Inserção da pasta e arquivo

def logaut(request):
    if request.method == "POST":
        logout(request) 
        return redirect("user:login")
    return render(request, "layout.html") # Inserção da pasta e arquivo
