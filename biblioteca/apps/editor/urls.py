from django.urls import path

from biblioteca.apps.editor.views.class_views import EditorCreate, EditorDelete, EditorList, EditorUpdate
from biblioteca.apps.editor.views.fuctions_views import editor_create, editor_delete, editor_list, editor_update, index


urlpatterns = [
    path('', index, name='index'),
    path('editor/nuevo_cv', EditorCreate.as_view(), name='editor_crear_c'),
    path('editor/listar_cv', EditorList.as_view(), name='editor_listar_c'),
    path('editor/eliminar_cv/<int:pk>',
         EditorDelete.as_view(), name='editor_eliminar_c'),
    path('editor/editar_cv/<int:pk>',
         EditorUpdate.as_view(), name='editor_editar_c'),

    path('editor/nuevo_fv', editor_create, name='editor_crear_f'),
    path('editor/listar_fv', editor_list, name='editor_listar_f'),
    path('editor/editar_fv/<int:id_editor>',
         editor_update, name='editor_editar_f'),
    path('editor/eliminar_fv/<int:id_editor>',
         editor_delete, name='editor_eliminar_f'),
]
