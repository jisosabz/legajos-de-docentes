
from django.forms import ModelForm, TextInput, EmailInput, DateInput, Select
from django.forms.widgets import ClearableFileInput
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
            'fecha_ingreso': DateInput( format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'nivel': Select(attrs={'class': 'form-select'}),
        }
from django.core.exceptions import ValidationError

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'fecha_emision': DateInput(format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_vencimiento': DateInput(format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'archivo': ClearableFileInput(attrs={'class': 'form-control'}),
            'docente': Select(attrs={'class': 'form-select'}),
            'tipo_documento': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_emision = cleaned_data.get('fecha_emision')
        fecha_vencimiento = cleaned_data.get('fecha_vencimiento')

        if fecha_emision and fecha_vencimiento:
            if fecha_vencimiento < fecha_emision:
                raise ValidationError("La fecha de vencimiento no puede ser anterior a la fecha de emisión.")

