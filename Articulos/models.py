from django.db import models

# Create your models here.

class Entrada(models.Model):#formulario de add usuario
    nombre = models.CharField(max_length=50)#longitid del nombre
    contenido = models.TextField(max_length=400)#cuadro mas grande de texto
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

    def __str__(self):
       return self.nombre #agrega el nombre a la list

class Comentario(models.Model):#formulario de comentario
    nombre = models.CharField(max_length=60)
    mensaje = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nombre

