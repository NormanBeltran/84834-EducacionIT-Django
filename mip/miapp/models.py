from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    inscriptos = models.IntegerField()
    profesor = models.CharField(max_length=50, default="Norman")
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        ordering = ["nombre"]


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ESPECIALIDADES = (
        (1, "Python"),
        (2, "Data Analitycs"),
        (3, "Data Science"),
        (4, "IA Prompts"),
        (5, "IA Agentes"),
    )
    especialidad = models.IntegerField(choices=ESPECIALIDADES)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"