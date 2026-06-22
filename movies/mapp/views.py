from django.shortcuts import render
from django.http import HttpResponse

# Models
from .models import *

# Class Based Views
from django.views.generic import TemplateView
from django.views.generic import ListView

# Main
class HomeView(TemplateView):
    template_name = "mapp/index.html"

class GenderList(ListView):
    model = Gender

    #def get_queryset(self):
    #    return Gender.objects.all().order_by("id").values()

    #def get_queryset(self):
    #    return Gender.objects.filter(name__icontains="i").order_by("id").values()

class CompanyList(ListView):
    model = Company

class MovieList(ListView):
    model = Movie
    template_name = "mapp/peliculas.html" # Un ejemplo si quiero cambiar el nombre del template por un nombre mio