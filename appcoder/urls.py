from django.urls import path

from appcoder.views import *

urlpatterns = [
    
    path('', inicio),
    path('pagina-cursos', cursos),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
    path('entregables', entregables),

    ]