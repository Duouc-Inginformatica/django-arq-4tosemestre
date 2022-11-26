from email import message
import json #email_message
from re import I #importar libreria re
from django.http import HttpResponse #importar libreria http
from django.utils.decorators import method_decorator #importar libreria decorators
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Maule #importar tabla maule
from django.views.decorators.csrf import csrf_exempt #importar libreria csrf_exempt
import json #importar libreria json

class MauleViews(View):
    @method_decorator(csrf_exempt) #decorar funcion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): #crear funcion get
        if (id > 0): #si id_usuario es mayor a 0
            Datos = list(Maule.objects.filter(id=id).values())
            if len(Datos) > 0:
                Dates = Datos[0]
                datos={'message': 'Success', 'Datos': Dates}
            else:
                datos={'message': 'No hay datos'}
        else:
            Datos=list(Maule.objects.values()) #crear variable Datos
            if len(Datos)>0:
                datos={'message': 'Success', 'peralta': Datos} #crear variable datos
            else:
                datos={'message': 'No hay datos'}
            return JsonResponse(datos) #retornar datos


    def post(self, request): #crear funcion post
        jd = json.loads(request.body) #crear variable jd
        Maule.objects.create(correo=jd['nombre'], nombre=jd['nombre'], apellido=jd['costo'], rut=jd['comment'],pwd=jd['asignatura'])
        Dates={'message': 'Success'} #crear variable dates
        return JsonResponse (Dates) #retornar Dates

        # 'id', 'nombre','costo','valor','asignatura','comentario']
    def put(self, request, id):
        jd = json.loads(request.body)
        Datos = list(Maule.objects.filter(id=id).values())
        if len(Datos) > 0:
            Maule = Maule.objects.get(id=id)
            Maule.nombre = jd['nombre']
            Maule.costo = jd['costo']
            Maule.asignaturia = jd['asignatura']
            Maule.comentario = jd['comentario']
            Maule.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Maule not found..."}
        return JsonResponse(datos)

    
    
    
    
    def delete(self, request, id): #crear funcion delete
        Datos = list(Maule.objects.filter(id=id).values()) 
        if len(Datos) > 0:
            Maule.objects.filter(id=id).delete() #crear variable Datos
            datos={'message': 'Success'} #crear variable datos
        else:
            datos={'message': 'No hay datos'}
        return JsonResponse(datos) #retornar datos
 

