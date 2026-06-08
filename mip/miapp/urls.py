from django.urls import path, include
from . import views

urlpatterns = [
    path("",            views.index,                name="index"),  
    path("acerca",      views.acerca,               name="acerca"),  
    path("contacto",    views.contacto,             name="contacto"),  
    path("cursos",      views.consultar_cursos,     name="cursos"),  
    path("aero",        views.aeropuertos,          name="aero"),  
    path("aero_api",    views.aero_api,             name="aero_api"),  

    path("bienvenido",  views.bienvenido,           name="bienvenido"),  
    path("bienvenido2", views.bienvenido2,          name="bienvenido2"),  

    # Sin ORM
    path("allcursos",       views.allCursos,        name="allcursos"),  
    path("uncurso/<id>/",   views.unCurso,          name="uncurso"),  
    path("nuevocurso",      views.nuevoCurso,       name="nuevocurso"),  

    # Con ORM
    path("nuevocursoorm",   views.nuevoCursoORM,    name="nuevocursoorm"),  
    path("allcursosorm",    views.cursos_orm,       name="allcursosorm"),  
]