from django.shortcuts import redirect, render

from biblioteca.apps.editor.forms import EditorForm
from biblioteca.apps.editor.models import Editor


def index(request):
    return render(request, 'editor/index.html')


def editor_create(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('editor_listar_f')
    else:
        form = EditorForm()
    return render(request, 'editor/view_functions/editor_form.html', {'form': form})


def editor_list(request):
    editor = Editor.objects.all().order_by('id')
    contexto = {'editores': editor}
    return render(request, 'editor/view_functions/editor_list.html', contexto)


def editor_update(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'GET':
        form = EditorForm(instance=editor)
    else:
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
        return redirect('editor_listar_f')
    return render(request, 'editor/view_functions/editor_form.html', {'form': form})


def editor_delete(request, id_editor):
    editor = Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        editor.delete()
        return redirect('editor_listar_f')
    return render(request, 'editor/view_functions/editor_delete.html', {'editor': editor})
