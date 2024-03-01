from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from biblioteca.apps.libro.views.class_views import AutorCreate, AutorDelete, AutorList, AutorUpdate, LibroCreate, LibroDelete, LibroEdit, LibroList

from biblioteca.apps.libro.views.fuctions_views import autor_create, autor_delete, autor_list, autor_update, index, libro_create, libro_delete, libro_list, libro_update

urlpatterns = [
    path('', index, name='index'),
    path('autor/nuevo_cv', AutorCreate.as_view(), name='autor_crear_c'),
    path('autor/listar_cv', AutorList.as_view(), name='autor_listar_c'),
    path('autor/editar_cv/<int:pk>', AutorUpdate.as_view(), name='autor_editar_c'),
    path('autor/eliminar_cv/<int:pk>',
         AutorDelete.as_view(), name='autor_eliminar_c'),

    path('autor/nuevo_fv', autor_create, name='autor_crear_f'),
    path('autor/listar_fv', autor_list, name='autor_listar_f'),
    path('autor/editar_fv/<int:pk>', autor_update, name='autor_editar_f'),
    path('autor/eliminar_fv/<int:autor_id>',
         autor_delete, name='autor_eliminar_f'),

    path('libro/nuevo_cv', LibroCreate.as_view(), name='libro_crear_c'),
    path('libro/listar_cv', LibroList.as_view(), name='libro_listar_c'),
    path('libro/editar_cv/<int:pk>', LibroEdit.as_view(), name='libro_editar_c'),
    path('libro/eliminar_cv/<int:pk>',
         LibroDelete.as_view(), name='libro_eliminar_c'),

    path('libro/nuevo_fv', libro_create, name='libro_crear_f'),
    path('libro/listar_fv', libro_list, name='libro_listar_f'),
    path('libro/editar_fv/<int:id_libro>', libro_update, name='libro_editar_f'),
    path('libro/eliminar_fv/<int:id_libro>',
         libro_delete, name='libro_eliminar_f'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
