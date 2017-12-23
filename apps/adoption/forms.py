from django import forms
from apps.pet.models import Request
class RequestForm(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model=Request
		fields=[
			'people', 
			'idOfPets',
			'reasons',
		]
		labels={
			'people':'Persona',
			'idOfPets':'Cantidad de mascotas',
			'reasons':'Motivo',
		}
		widgets={
			'people':forms.Select(attrs={'class':'form-control btn-default','placeholder':'Seleccione persona adoptiva'}),
			'reasons':forms.TextInput(attrs={'class':'form-control','placeholder':'Motivo de la adopción'}),
			'idOfPets':forms.CheckboxSelectMultiple(),
		}