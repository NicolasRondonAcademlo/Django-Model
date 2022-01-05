from django.db import models


# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']

# Entregable: Crear una aplicación para estudiantes que contenga un modelo
# Estudiante, una vista para listar los estudiantes en la base de datos y
# poder acceder al detalle de cada estudiante. Además crear un modelo para
# Clase, y una vista para poder ver la lista de clases disponibles y
# al dar click, poder listar los alumnos inscritos a cada clase.
