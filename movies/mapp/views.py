from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages

# Models
from .models import *

# Forms
from .forms import *

# Class Based Views
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Class auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

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

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('peliculas')

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('peliculas')    

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('peliculas')    

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o Contraseña Inválidos")
        return super().form_invalid(form)