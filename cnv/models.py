from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Paciente(ClaseModelo):
	dni = models.CharField(max_length=8, unique=True)
	nombre = models.CharField(max_length=30)
	apellido_paterno = models.CharField(max_length=30)
	apellido_materno = models.CharField(max_length=30)
	fecha_nac = models.DateField()
	celular = models.CharField(max_length=9)
	sintoma = models.ManyToManyField('Sintoma')


	def NombreCompleto(self):
		cadena = "{0} {1}, {2}"
		return cadena.format(self.dni, self.nombre, self.fecha_nac)

	def __str__(self):
		return self.NombreCompleto()

class Sintoma(models.Model):
	descripcion  = models.CharField(max_length=100, help_text='Descripción de la Categoría', unique=True)

	def __str__(self):
		return "{0}".format(self.descripcion,)


