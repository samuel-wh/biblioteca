from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from biblioteca.apps.editor.forms import EditorForm
from biblioteca.apps.editor.models import Editor


class EditorCreate(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'editor/view_class/editor_form.html'
    success_url = reverse_lazy('editor_listar_c')


class EditorList(ListView):
    model = Editor
    template_name = 'editor/view_class/editor_list.html'


class EditorDelete(DeleteView):
    model = Editor
    template_name = 'editor/view_class/editor_delete.html'
    success_url = reverse_lazy('editor_listar_c')


class EditorUpdate(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/view_class/editor_form.html"
    success_url = reverse_lazy('editor_listar_c')
