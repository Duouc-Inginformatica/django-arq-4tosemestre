from django.db import models

# Create your models here.

class Maule(models.Model): #crear clase Maule
    id = models.AutoField(primary_key=True) #crear campo rut
    nombre = models.CharField(max_length=50, verbose_name='nombre') #crear campo nombre
    costo = models.CharField(max_length=50, verbose_name='costo') #crear campo nombre
    asignatura = models.CharField(max_length=50, verbose_name='asignatura') #crear campo nombre
    comentario = models.CharField(max_length=250, verbose_name='comentario') #crear campo nombre

