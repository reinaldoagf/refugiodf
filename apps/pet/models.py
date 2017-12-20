from django.db import models

from apps.adoption.models import People


class Vaccine(models.Model): #vacuna
	name = models.CharField(max_length=50) #nombre
	def __str__(self):
		return '{}'.format(self.name)
class Pet(models.Model):
	name = models.CharField(max_length=50) #nombre
	sex = models.CharField(max_length=10) #sexo
	aproximatedAge = models.IntegerField() #edad aproximada
	rescueDate = models.DateField() #fecha de rescate
	people = models.ForeignKey(People, null=True, blank=True, on_delete=models.CASCADE)
	vaccine = models.ManyToManyField(Vaccine, blank=True)