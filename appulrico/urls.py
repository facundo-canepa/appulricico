from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('entregables/', views.entregables, name='entregables'),
    path('curso-formulario/', views.curso_formulario, name='curso_formulario'),
    path('form-con-api/', views.form_con_api, name='form_con_api'),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]
