from django.db import models
from django.utils import timezone

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    instrumento = models.CharField(max_length=100,default='Sin instrumento')
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    def __str__(self):
	    return self.nombre

class Album(models.Model):
    autor = models.ForeignKey('auth.User')
    artista = models.ForeignKey(Musico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()
    foto = models.ImageField(blank= 'True')

    def __str__(self):
	    return self.titulo

