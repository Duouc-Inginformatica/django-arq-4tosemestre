from models import Maule
from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms

class MauleForm(forms.ModelForm): #crear clase MauleForm
    class Meta: #crear clase Meta
        model = Maule #crear modelo Maule
        fields = ['id', 'nombre','costo','valor','asignatura','comentario'] #crear campos