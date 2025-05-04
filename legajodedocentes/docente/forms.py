
from django.forms import ModelForm, TextInput, EmailInput, DateInput, Select
from docente.models import Docente, Documento


class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'ci': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'telefono': TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'nivel': Select(attrs={'class': 'form-select'}),
        }

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'fecha_emision': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_vencimiento': DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'archivo': TextInput(attrs={
                'type': 'file',
                'class': 'form-control'
            }),
            'docente': Select(attrs={'class': 'form-select'}),
            'tipo_documento': Select(attrs={'class': 'form-select'}),
        }
