from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("generos/", GenderList.as_view(), name="generos"),
    path("companias/", CompanyList.as_view(), name="companias"),

    path("peliculas/", MovieList.as_view(), name="peliculas"),
    path("pelicula_create/", MovieCreate.as_view(), name="pelicula_create"),
    path("pelicula_update/<int:pk>/", MovieUpdate.as_view(), name="pelicula_update"),
    path("pelicula_delete/<int:pk>/", MovieDelete.as_view(), name="pelicula_delete"),

    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),

]
