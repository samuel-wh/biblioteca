from __future__ import unicode_literals

from django.db import models

from biblioteca.apps.editor.models import Editor


# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return '{}'.format(self.nombre)
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(
        Editor, null=True, blank=True, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to="images/", null=True, blank=True)

    def __unicode__(self,):
        return str(self.portada)
