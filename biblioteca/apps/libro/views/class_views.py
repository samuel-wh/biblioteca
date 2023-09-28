from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from biblioteca.apps.libro.forms import AutorForm, LibroForm
from biblioteca.apps.libro.models import Autor, Libro


# Autores cv
class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/view_class/autor_form.html'
    success_url = reverse_lazy('autor_listar_c')


class AutorList(ListView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/view_class/autor_listar.html'


class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/view_class/autor_form.html'
    success_url = reverse_lazy('autor_listar_c')


class AutorDelete(DeleteView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/view_class/autor_delete.html'


# Libros cv


class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/view_class/libro_form.html'
    success_url = reverse_lazy('libro_listar_c')

class LibroList(ListView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/view_class/libro_listar.html'

class LibroEdit(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/view_class/libro_form.html'
    success_url = reverse_lazy('libro_listar_c')

class LibroDelete(DeleteView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/view_class/libro_delete.html'
    success_url = reverse_lazy('libro_listar_c')
