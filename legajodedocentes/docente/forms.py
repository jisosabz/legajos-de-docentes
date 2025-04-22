
from django.forms import ModelForm, TextInput, EmailInput, DateInput, Select
from docente.models import Docente

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'ci': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'nivel': Select(attrs={'class': 'form-select'}),
        }
