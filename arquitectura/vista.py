from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def calendario(request):
    return render(request, 'calendario.html')

def index(request):
    return render(request, 'index.html')

def tienda(request):
    return render(request, 'tienda.html')

def profe(request):
    return render(request, 'profe.html')