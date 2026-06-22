from django.contrib import admin
from .models import *

class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")   
    list_display = ("id", "pelicula", "sinopsis", "stars", "premiere") 
    list_filter = ("genders", "company")

# Register your models here.
admin.site.register(Gender, GenderAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Movie, MovieAdmin)