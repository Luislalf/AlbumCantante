from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone
from django.dispatch import receiver

class Musico(models.Model):
    nombre = models.CharField(max_length=50,default='Nombre')
    apellido = models.CharField(max_length=50,default='Apellidos')
    instrumento = models.CharField(max_length=100,default='Instrumento')
    fecha_nacimiento = models.DateField(default='01/01/2000')
    direccion = models.CharField(max_length=80,default='Dirección')
    telefono = models.CharField(max_length=15,default='Télefono')
    correo = models.CharField(max_length=50,default='Correo')
    foto = models.ImageField(upload_to='musicos/')
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Album(models.Model):
    autor = models.ForeignKey('auth.User')
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,default='Sin titulo')
    fecha_lanzamiento = models.DateField(default='01/01/2016')
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

class Cometario2(models.Model):
	foto = models.ForeignKey(Musico)
	cometario = models.TextField()
	def __str__(self):
		return self.cometario
