from django.db import models

# Create your models here.


class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return '{}'.format(self.nombre)
    
    def __str__(self):
        return '{}'.format(self.nombre)
