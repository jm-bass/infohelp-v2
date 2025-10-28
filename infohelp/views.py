from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def inicio(request):
    return render(request, "inicio.html")

def cursos(request):
    return render(request, "cursos.html")

def biblioteca(request):
    return render(request, "biblioteca.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")