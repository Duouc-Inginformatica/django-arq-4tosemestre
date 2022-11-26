from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms
from api_dote.models import Lola #importar tabla maule

class LolaForm(forms.ModelForm): #crear clase MauleForm
    class Meta: #crear clase Meta
        model = Lola #crear modelo Maule
        fields = ['id', 'nombre', 'correo', 'telefono', 'edad', 'asignatura', 'fecha', 'precio'] #crear campos



    #     class Lola(models.Model): #crear clase Maule
    # id = models.AutoField(primary_key=True) #crear campo rut
    # nombre = models.CharField(max_length=50, verbose_name='Nombre') #crear campo nombre
    # correo = models.EmailField(max_length=200, verbose_name='Correo') #crear campo correo
    # telefono = models.CharField(max_length=200, verbose_name='Ticket') #crear campo ticket
    # edad = models.IntegerField() #crear campo edad
    # asignatura = models.CharField(max_length=200, verbose_name='Movilidad') #crear campo movilidad
    # fecha = models.DateField() #crear campo fecha
    # precio = models.IntegerField() #crear campo precio