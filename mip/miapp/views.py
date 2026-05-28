from django.shortcuts import render
from django.http import HttpResponse

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