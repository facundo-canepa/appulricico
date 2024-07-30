from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
from .models import Profesor

# Create your views here.

def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "appcoder/cursos.html", {"cursos": cursos})

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "appcoder/profesores.html", {"profesores": profesores})

def entregables(request):
    return render(request, "appcoder/entregables.html")

