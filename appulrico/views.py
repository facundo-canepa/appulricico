from django.shortcuts import render
from django.http import HttpResponse
from appulrico.forms import CursoFormulario

from .models import Curso
from .models import Profesor

# Create your views here.

def inicio(request):
    return render(request, "appulrico/inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "appulrico/cursos.html", {"cursos": cursos})

def estudiantes(request):
    return render(request, "appulrico/estudiantes.html")

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appulrico/profesores.html", {"profesores": profesores})

def entregables(request):
    return render(request, "appulrico/entregables.html")

def curso_formulario(request):
    if request.method == 'POST':
        curso_formulario = CursoFormulario(request.POST)
        if curso_formulario.is_valid():
            curso = Curso(
                nombre=curso_formulario.cleaned_data['curso'],
                comision=curso_formulario.cleaned_data['comision']
            )
            curso.save()
            return render(request, "appulrico/index.html")
    else:
        curso_formulario = CursoFormulario()
    return render(request, "appulrico/curso_formulario.html", {'curso_formulario': curso_formulario})


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)  
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "appulrico/index.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "appulrico/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appulrico/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "appulrico/buscar_form_con_api.html", {"miFormulario": miFormulario})


