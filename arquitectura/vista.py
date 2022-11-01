from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def profe(request):
    return render(request, 'profe.html')