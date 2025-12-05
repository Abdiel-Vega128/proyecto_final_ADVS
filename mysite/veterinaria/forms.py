from django import forms
from .models import Dueno, Veterinario, Mascota, Consulta, Vacuna

class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = '__all__'
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'})
        }

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'fecha_consulta': forms.DateInput(attrs={'type': 'date'})
        }

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = '__all__'
        widgets = {
            'fecha_aplicacion': forms.DateInput(attrs={'type': 'date'})
        }
