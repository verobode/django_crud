from django import forms 
from .models import Libro

# A partir de acá se construye el mapeado de nuestro modelo a partir de la declaración de estos formularios (views)
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'