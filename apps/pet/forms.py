from django import forms
from apps.pet.models import Pet
class PetForm(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model=Pet
		fields=[
			'name', 
			'sex',
			'aproximatedAge', 
			'rescueDate', 
			'people',
			'vaccine',
		]
		labels={
			'name':'Nombre',
			'sex':'Sexo',
			'aproximatedAge':'Edad',
			'rescueDate':'Fecha de rescate',
			'people':'Adoptivo',
			'vaccine':'Vacuna(s)',
		}
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
			'sex':forms.TextInput(attrs={'class':'form-control','placeholder':'Sexo'}),
			'aproximatedAge':forms.TextInput(attrs={'class':'form-control','placeholder':'Edad'}),
			'rescueDate':forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha de rescate'}),
			'people':forms.Select(attrs={'class':'form-control btn-default','placeholder':'Seleccione persona adoptiva'}),
			'vaccine':forms.CheckboxSelectMultiple(),
		}