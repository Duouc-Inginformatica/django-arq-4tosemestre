from django.shortcuts import render
from importlib.resources import contents
from multiprocessing import context
import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import redirect, render #importar funciones redirect y render
from api.models import Maule #importar la tabla maule
# from api.forms import MauleForm #importar formulario

from api_dote.models import Lola
from api_dote.forms import LolaForm

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

def prueba(request):
    return render(request, 'prueba.html')

def form2(request): #crear funcion index
    litio = Lola.objects.all() #crear variable litio y llamar a la tabla lola
    return render(request, 'form2.html', {'litio': litio}) #enviar datos a la pagina index.html en variable litio

def prueba(request): #crear funcion index
    Maules = Maule.objects.all() #crear variable maules y llamar a la tabla maule
    return render(request, 'prueba.html', {'Maules': Maules}) #enviar datos a la pagina index.html en variable maules

#django editar datos de la tabla
def editare(request, id): #crear funcion editar
    order2 = Lola.objects.get(id=id) #crear variable order y llamar a la tabla maule
    return render(request, 'editar2.html', {'order2': order2}) #enviar datos a la pagina editar.html en variable order

def editalola(request): #crear funcion editar
    id = request.POST.get('id') #crear variable rut y llamar a la variable rut de la pagina index.html
    nombre = request.POST.get('nombre') #crear variable nombres y llamar a la variable nombres de la pagina index.html
    correo = request.POST.get('correo') #crear variable apellidos y llamar a la variable apellidos de la pagina index.html
    telefono = request.POST.get('telefono') #crear variable correo y llamar a la variable correo de la pagina index.html
    edad = request.POST.get('edad') #crear variable ticket y llamar a la variable ticket de la pagina index.html
    asignatura = request.POST.get('asignatura') #crear variable edad y llamar a la variable edad de la pagina index.html
    fecha = request.POST.get('fecha') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    precio = request.POST.get('precio') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    slt2 = Lola.objects.get(id=id) #crear variable slt y llamar a la tabla maule
    slt2.id = id #crear variable slt y llamar a la variable rut de la tabla maule
    slt2.nombre = nombre #crear variable slt y llamar a la variable nombres de la tabla maule
    slt2.correo = correo #crear variable slt y llamar a la variable apellidos de la tabla maule
    slt2.telefono = telefono #crear variable slt y llamar a la variable correos de la tabla maule
    slt2.edad = edad #crear variable slt y llamar a la variable ticket de la tabla maule
    slt2.asignatura = asignatura #crear variable slt y llamar a la variable edad de la tabla maule
    slt2.fecha = fecha #crear variable slt y llamar a la variable fecha de la tabla maule
    slt2.precio = precio #crear variable slt y llamar a la variable fecha de la tabla maule
    slt2.save() #guardar datos de la tabla
    return redirect('form2') #redireccionar a la pagina index.html

# eliminar datos de la tabla
def registrare(request): #crear funcion registrar
    id = request.POST.get('id') #crear variable rut y llamar a la variable rut de la pagina index.html
    nombre = request.POST.get('nombre') #crear variable nombres y llamar a la variable nombres de la pagina index.html
    correo = request.POST.get('correo') #crear variable apellidos y llamar a la variable apellidos de la pagina index.html
    telefono = request.POST.get('telefono') #crear variable correo y llamar a la variable correo de la pagina index.html
    edad = request.POST.get('edad') #crear variable ticket y llamar a la variable ticket de la pagina index.html
    asignatura = request.POST.get('asignatura') #crear variable edad y llamar a la variable edad de la pagina index.html
    fecha = request.POST.get('fecha') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    precio = request.POST.get('precio') #crear variable fecha y llamar a la variable fecha de la pagina index.html
    datala = Lola.objects.create(id=id, nombre=nombre, correo=correo, telefono=telefono, edad=edad, asignatura=asignatura, fecha=fecha, precio=precio) #crear variable registro y llamar a la tabla maule
    return redirect('form2') #redireccionar a la pagina index.html


# eliminar datos de la tabla
def eliminare(request, id): #crear funcion eliminar
    removere = Lola.objects.get(id=id) #crear variable remover y llamar a la tabla maule
    removere.delete() #eliminar datos de la tabla
    return redirect('form2') #redireccionar a la pagina index.html