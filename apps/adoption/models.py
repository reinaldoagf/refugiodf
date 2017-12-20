from django.db import models
# Create your models here.

class People(models.Model):
	identityCard=models.IntegerField(primary_key=True) #cedula de identidad
	name = models.CharField(max_length=50) #nombre 
	lastname = models.CharField(max_length=70) #apellido
	age = models.IntegerField() #edad
	phone = models.CharField(max_length=20) #numero de telefono
	email = models.EmailField() #correo electronico
	domicile = models.TextField() #domicilio
	def __str__(self):
		return '{} {}'.format(self.name, self.lastname)
class Request(models.Model): #solicitud
	people = models.ForeignKey(People, null=True, blank=True) #persona
	numberOfPets= models.IntegerField() #cantidad de mascotas a adoptar
	reasons = models.TextField() #razones
