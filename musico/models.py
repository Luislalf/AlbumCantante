from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone
from django.dispatch import receiver

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
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,default='Sin titulo')
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField(default='Sin Descripcion')
    foto = models.ImageField(upload_to='fotos/')
    favorito = models.BooleanField(default=False)
    def __str__(self):
	    return self.titulo


class Cometario(models.Model):
	foto = models.ForeignKey(Album)
	cometario = models.TextField()
	def __str__(self):
		return self.cometario
