from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

#La función envía una solicitud y responde con un texto
def inicio(request):
    return render(request, 'paginas/inicio.html')

#Busca un archivo html accediendo a templates
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')

