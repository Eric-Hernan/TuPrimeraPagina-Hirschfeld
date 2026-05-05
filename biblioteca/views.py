from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro, Amigo, Prestamo
from .forms import LibroForm, AmigoForm, PrestamoForm



def inicio(request):
    libros = Libro.objects.all() 
    return render(request, 'biblioteca/inicio.html', {'libros': libros})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'biblioteca/detalle_libro.html', {'libro': libro})

def about(request):
    return render(request, 'biblioteca/about.html')

def buscar_libro(request):
    query = request.GET.get('titulo')
    resultados = Libro.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'biblioteca/buscar_libro.html', {'resultados': resultados, 'query': query})



@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', pk=pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/libro_form.html', {'form': form, 'titulo': 'Editar Libro'})

@login_required
def agregar_amigo(request):
    if request.method == 'POST':
        form = AmigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AmigoForm()
    return render(request, 'biblioteca/agregar_amigo.html', {'form': form})

@login_required
def registrar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/registrar_prestamo.html', {'form': form})


class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/agregar_libro.html' 
    success_url = reverse_lazy('lista_libros')

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'biblioteca/borrar_confirm.html'
    success_url = reverse_lazy('lista_libros')