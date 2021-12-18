from django import forms
from django.db import models
from django.forms import widgets
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del autor',
            'apellido': 'Apellidos del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripción del autor',
        }

    widgets = {
        'nombre': forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del autor',
                'id' : 'nombre'
            }
        ),
        'apellido': forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido del autor',
                'id' : 'apellido'
            }
        ),
        'nacionalidad': forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la nacionalidad del autor',
                'id' : 'nacionalidad'
            }
        ),
        'descripcion': forms.Textarea(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una descripcion del autor',
                'id' : 'descripcion'
            }
        )  
    }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor_id', 'fecha_publicacion']
        labels = {
            'titulo': 'Titulo del libro',
            'autor_id': 'Autores del libro',
            'fecha_publicacion': 'Fecha de publicacion del libro'
        }

    widgets = {
        'titulo': forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el titulo del libro',
                'id' : 'titulo'
            }
        ),
        'autor_id': forms.SelectMultiple(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido del autor',
                'id' : 'autor_id'
            }
        ),
        'fecha_publicacion': forms.DateInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la fecha de publicacion',
                'id' : 'fecha_publicacion'
            }
        )
    }