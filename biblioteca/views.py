from django.shortcuts import render, redirect
from .forms import LibroForm
from .models import Libro
from .forms import LibroForm, AmigoForm, PrestamoForm

def inicio(request):
    # pagina principal
    return render(request, 'biblioteca/inicio.html')

def agregar_libro(request):

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})


def buscar_libro(request):
   
    query = request.GET.get('titulo')
    resultados = []

    if query:
       
        resultados = Libro.objects.filter(titulo__icontains=query)

    return render(request, 'biblioteca/buscar_libro.html', {'resultados': resultados, 'query': query})

def agregar_amigo(request):
    if request.method == 'POST':
        form = AmigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AmigoForm()
    return render(request, 'biblioteca/agregar_amigo.html', {'form': form})

def registrar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/registrar_prestamo.html', {'form': form})

# Create your views here.
