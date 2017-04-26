from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.

class Usuarios(models.Model):
	"""docstring for Login"""
	nombre=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	contrasenya=models.CharField(max_length=64)
	def __str__(self):
		return self.nombre

class Genero(models.Model):
	"""docstring for Missatges"""
	nombre=models.CharField(max_length=20,default='')
	"""incidencia=models.CharField(max_length=120)"""
	"""usuaris=models.ManyToManyField(Usuaris)"""
	def __str__(self):
		return self.nombre

class Libros(models.Model):
	"""docstring for Hashtags"""
	"""identificador=models.IntegerField(default=0)"""
	"""departament=models.ForeignKey(Departaments)"""
	nombre=models.CharField(max_length=50, default='')
	genero=models.ManyToManyField(Genero)
	usuario=models.ForeignKey(Usuarios,default='')
	portada=models.ImageField(upload_to='imagenes/portada')
	sinopsis=models.CharField(max_length=200,default='')
	
	
	def __str__(self):
		return self.nombre