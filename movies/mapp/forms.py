from django import forms
from .models import Movie
from ckeditor.widgets import CKEditorWidget


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description',
                  'rating', 'premiere',
                  'genders', 'company',
                  'image']
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Película'}),
            #'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Sinopsis'}),
            'description': CKEditorWidget(),
            'rating': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Rating'}),
            'genders': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Géneros'}),
            'company': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Compañía'}),
            'premiere': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de Estreno'}),
        }

        labels = {
            'name': 'Título',
            'description': 'Sinopsis'
        }