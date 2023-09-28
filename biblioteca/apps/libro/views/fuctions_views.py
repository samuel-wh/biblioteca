from django.shortcuts import render, redirect

from models import Autor, Libro
from forms import AutorForm, LibroForm

# Create your views here.


def index(request):
    return render(request, 'libro/index.html')


# Autores fv


def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('autor_listar_f')
    else:
        form = AutorForm()
    return render(request, 'libro/view_functions/autor_form.html', {'form':form})


def autor_list(request):
    autor = Autor.objects.all().order_by('id')
    contexto = {'autores':autor}
    return render(request,'libro/view_functions/autor_listar.html', contexto)


def autor_update(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'GET':
        form = AutorForm(instance=autor)
    else:
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        return redirect('autor_listar_f')
    return render(request, 'libro/view_functions/autor_form.html', {'form':form})


def autor_delete(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_listar_f')
    return render(request, 'libro/view_functions/autor_delete.html',{'autor':autor})


# Libros fv


def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('libro_listar_f')
    else:
        form = LibroForm()
    return render(request, 'libro/view_functions/libro_form.html', {'form':form})

def libro_list(request):
    libro = Libro.objects.all().order_by('id')
    contexto = {'libros':libro}
    return render(request,'libro/view_functions/libro_listar.html', contexto)

def libro_update(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST,request.FILES, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('libro_listar_f')
    return render(request, 'libro/view_functions/libro_form.html', {'form':form})

def libro_delete(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_listar_f')
    return render(request, 'libro/view_functions/libro_delete.html',{'libro':libro})
