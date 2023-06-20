from django.shortcuts import render,redirect
from .models import Rol, Persona, Estudiante
from .forms import RolForm, PersonaForm, EstudianteForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def acerca(request):
    return render(request, "acerca.html")

def crear(request):
    if request.method == 'POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            try:    
                form.save()
                return redirect('/index')
            except:
                pass
    else:
        form=PersonaForm()
    return render(request, 'crear.html', {'form': form})


def editar(request, id):
    persona = Persona.objects.get(id=id)
    form = PersonaForm (instance = persona)
    if request.method == 'POST':
        form = PersonaForm (request.POST, instance=persona)
        if form.is_valid():
            try:
                form.save()
                return redirect('/index')
            except:
                pass
    context = {
        'persona' : persona,
        'form' : form
    }
    return render(request, 'editar.html', context)

def eliminar(request ,id):
    
    framework = Persona.objects.get(id=id)
    framework.delete()
    return redirect('/index')

def index(request):
    personas = Persona.objects.all()
    return render (request , 'index.html', {'personas':personas})

def layouts(request):
    return render(request, "layouts.html")
"""---------------------------------------------------"""
def crearestudiante(request):
    if request.method == 'POST':
        form=EstudianteForm(request.POST)
        if form.is_valid():
            try:    
                form.save()
                return redirect('/indexestudiante')
            except:
                pass
    else:
        form=EstudianteForm()
    return render(request, 'crearestudiante.html', {'form': form})

def indexestudiante(request):
    estudiantes = Estudiante.objects.all()
    return render (request , 'indexestudiante.html', {'estudiantes':estudiantes})

def editarestudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    form = EstudianteForm (instance = estudiante)
    if request.method == 'POST':
        form = EstudianteForm (request.POST, instance=estudiante)
        if form.is_valid():
            try:
                form.save()
                return redirect('/indexestudiante')
            except:
                pass
    context = {
        'estudiante' : estudiante,
        'form' : form
    }
    return render(request, 'editarestudiante.html', context)

def eliminarestudiante(request ,id):
    
    framework = Estudiante.objects.get(id=id)
    framework.delete()
    return redirect('/indexestudiante')

"""---------------------------------------------------"""
def crearrol(request):
    if request.method == 'POST':
        form=RolForm(request.POST)
        if form.is_valid():
            try:    
                form.save()
                return redirect('/indexrol')
            except:
                pass
    else:
        form=RolForm()
    return render(request, 'crearrol.html', {'form': form})

def indexrol(request):
    rols = Rol.objects.all()
    return render (request , 'indexrol.html', {'rols':rols})

def editarrol(request, id):
    rol = Rol.objects.get(id=id)
    form = RolForm (instance = rol)
    if request.method == 'POST':
        form = RolForm (request.POST, instance=rol)
        if form.is_valid():
            try:
                form.save()
                return redirect('/indexrol')
            except:
                pass
    context = {
        'rol' : rol,
        'form' : form
    }
    return render(request, 'editarrol.html', context)

def eliminarrol(request ,id):
    
    framework = Rol.objects.get(id=id)
    framework.delete()
    return redirect('/indexrol')