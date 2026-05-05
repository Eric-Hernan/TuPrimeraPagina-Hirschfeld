from django import forms
from .models import Amigo, Libro, Prestamo

class AmigoForm(forms.ModelForm):
        class Meta:
                    model = Amigo
                    fields = ['nombre', 'email']

class LibroForm(forms.ModelForm):
            class Meta:
                    model = Libro
                    fields = ['titulo', 'autor', 'categoria']

class PrestamoForm(forms.ModelForm):
        class Meta:
                model = Prestamo
                fields = ['libro', 'amigo']
                
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'sinopsis', 'imagen', 'fecha_publicacion']