from django import forms
from django.forms import ModelForm
from persona.models import Rol
from persona.models import Persona
from persona.models import Estudiante

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields= "__all__"

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields= "__all__"

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields= "__all__"