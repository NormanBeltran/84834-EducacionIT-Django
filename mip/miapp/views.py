from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import sqlite3

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos al curso de Django - EducacionIT")

def acerca(request):
    return HttpResponse("Acerca de mi ... les cuento que soy profe de Django")

def contacto(request):
    return HttpResponse("""
                        <html>
                        <h1>Contacto: Norman Beltran</h1>
                        </html>
                        """)

# Lectura de BD y envío de Información al cliente

def consultar_cursos(request):
    conn = sqlite3.connect('curso.db')
    
    cursor = conn.cursor()

    cursor.execute('SELECT id, nombre, inscriptos from cursos;')

    html = """
    <html>
    <title>Lista de Cursos</title>
    <table style="border:1px solid">
    <thead>
        <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Inscriptos</th>
        </tr>
    </thead>
    """

    for (id, nombre, inscriptos) in cursor.fetchall():
        html += "<tr>"
        html += "<td>" + str(id) + "</td>" 
        html += "<td>" + nombre + "</td>" 
        html += "<td>" + str(inscriptos) + "</td>" 
        html += "</tr>"

    html += """
    </table>
    </html>
    """
    conn.close()
    return HttpResponse(html)

# Lectura de Archivos (CSV) para enviar formateado al cliente

def aeropuertos(request):
    html = """
    <html>
    <title>Lista de Aeropuertos</title>
    <table style="border:1px solid">
    <thead>
        <tr>
            <th>Aeropuerto</th>
            <th>Ciudad</th>
            <th>País</th>
            <th>Código</th>
        </tr>
    </thead
    """

    with open("aeropuertos.csv", "r", encoding="utf-8") as file:
        for linea in file:
            datos = linea.split(',')
            html += "<tr>"
            html += "<td>" + datos[1].replace('"', '')  + "</td>"
            html += "<td>" + datos[2].replace('"', '')  + "</td>"
            html += "<td>" + datos[3].replace('"', '')  + "</td>"
            html += "<td>" + datos[4].replace('"', '')  + "</td>"
            html += "</tr>"

    html += """
    </table>
    </html>
    """
    return HttpResponse(html)

#  APIS con Django 

def aero_api(request):
    aeropuertos = []

    with open("aeropuertos.csv", "r", encoding="utf-8") as file:
        for linea in file:
            datos = linea.split(',')

            a_nombre = datos[1].replace('"', '')
            a_ciudad = datos[2].replace('"', '')
            a_pais   = datos[3].replace('"', '')
            a_codigo = datos[4].replace('"', '')

            aeropuerto = {
                "nombre": a_nombre,
                "ciudad": a_ciudad,
                "pais"  : a_pais,
                "codigo": a_codigo,
            }
            aeropuertos.append(aeropuerto)
    return JsonResponse(aeropuertos, safe=False) 

# Separa código HTML del código Django / Python

def bienvenido(request):
    with open("miapp/templates/miapp/bienvenido.html", "r", encoding="utf-8") as file:
        html = file.read()
    return HttpResponse(html)

def bienvenido2(request):
    pagina = "miapp/bienvenido2.html"  # Por default Django busca la carpeta /templates dentro de la aplicacion
    ctx = { "nombre": "Curso De Django (Desarrollo Web)", "comision": 84834, "dias": "Lunes y Jueves",
           "profesor": "Norman Beltran"}
    return render(request, pagina, ctx)
    