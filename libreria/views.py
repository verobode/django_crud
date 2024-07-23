from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .form import LibroForm

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

#Identifica los elementos que nos están enviando a través del formulario e igualarlo en el mismo
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None) 
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request):
    return render(request, 'libros/editar.html')

