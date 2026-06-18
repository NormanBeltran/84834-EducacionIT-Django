from django.db import models
from django.utils.html import format_html
from django.contrib import admin

# Géneros de Películas (1 a +)
class Gender(models.Model):
    name = models.CharField(verbose_name="Género", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Géneros"
        verbose_name = "Género"
        ordering = ["name"]

# Compañía de una Película (1 a 1)
class Company(models.Model):
    name = models.CharField(verbose_name="Compañía", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Compañías"
        verbose_name = "Compañía"
        ordering = ["name"]

# Películas
class Movie(models.Model):
    name = models.CharField(verbose_name="Película", max_length=50)
    description = models.TextField(verbose_name="Sinopsis")
    RATING = [
        (1, "Mala"),
        (2, "Mediocre"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Excelente"),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING)
    premiere = models.PositiveSmallIntegerField(verbose_name="Año de Estreno", null=False, blank=False)
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    company = models.ForeignKey(Company, verbose_name="Compañía", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Cover", upload_to="movies", null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Películas"
        verbose_name = "Película"
        ordering = ["name"]    

    @admin.display(ordering="description")
    def sinopsis(self):
        return format_html(self.description[:50])
