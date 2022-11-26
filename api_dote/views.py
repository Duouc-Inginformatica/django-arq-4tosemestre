from email import message
import json #email_message
from re import I #importar libreria re
from django.http import HttpResponse #importar libreria http
from django.utils.decorators import method_decorator #importar libreria decorators
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Lola #importar tabla Lola
from django.views.decorators.csrf import csrf_exempt #importar libreria csrf_exempt

# Create your views here.

class LolaViews(View): #crear clase LolaViews
    @method_decorator(csrf_exempt) #decorar funcion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): #crear funcion get
        if (id > 0): #si id_usuario es mayor a 0
            Datos = list(Lola.objects.filter(id=id).values())
            if len(Datos) > 0:
                Dates = Datos[0]
                datos={'message': 'correcto', 'Datos': Dates}
            else:
                datos={'message': 'No hay datos!'}
        else:
            Datos=list(Lola.objects.values()) #crear variable Datos
            if len(Datos)>0:
                datos={'message': 'correcto', 'peralta': Datos} #crear variable datos
            else:
                datos={'message': 'No hay datos'}
            return JsonResponse(datos) #retornar datos


    def post(self, request): #crear funcion post
        jd = json.loads(request.body) #crear variable jd
        Lola.objects.create(nombre=jd['nombre'], correo=jd['correo'], telefono=jd['edad'], asignatura=jd['asignatura'],fecha=jd['fecha'],precio=jd['precio'])
        Dates={'message': 'Datos creados!'} #crear variable dates
        return JsonResponse (Dates) #retornar Dates


    #     class Lola(models.Model): #crear clase Maule
    # id = models.AutoField(primary_key=True) #crear campo rut
    # nombre = models.CharField(max_length=50, verbose_name='Nombre') #crear campo nombre
    # correo = models.EmailField(max_length=200, verbose_name='Correo') #crear campo correo
    # telefono = models.CharField(max_length=200, verbose_name='Ticket') #crear campo ticket
    # edad = models.IntegerField() #crear campo edad
    # asignatura = models.CharField(max_length=200, verbose_name='Movilidad') #crear campo movilidad
    # fecha = models.DateField() #crear campo fecha
    # precio = models.IntegerField() #crear campo precio

        
    def put(self, request, id):
        jd = json.loads(request.body)
        Datos = list(Lola.objects.filter(id=id).values())
        if len(Datos) > 0:
            Lola = Lola.objects.get(id=id)
            Lola.nombre = jd['nombre']
            Lola.correo = jd['correo']
            Lola.telefono = jd['telefono']
            Lola.edad = jd['edad']
            Lola.asignatura = jd['asignatura']
            Lola.fecha = jd['fecha']
            Lola.precio = jd['precio']
            Lola.save()
            datos = {'message': "Actualizado"}
        else:
            datos = {'message': "Lola not found..."}
        return JsonResponse(datos)

    def delete(self, request, id): #crear funcion delete
        Datos = list(Lola.objects.filter(id=id).values()) 
        if len(Datos) > 0:
            Lola.objects.filter(id=id).delete() #crear variable Datos
            datos={'message': 'Eliminado'} #crear variable datos
        else:
            datos={'message': 'No hay datos'}
        return JsonResponse(datos) #retornar datos

