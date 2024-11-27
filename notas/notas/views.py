from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello")

def layout(request):
    return render (request, 'layout.html')
