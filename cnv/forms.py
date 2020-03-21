from django import forms
from django.forms import ModelForm
from .models import Paciente

class PacienteForm(forms.Form):
	class Meta:

		model = Paciente
		fiels = [
			'dni',
			'nombre',
			'apellido_paterno',
			'apellido_materno',
			'fecha_nac',
			'celular',
			]
		labels = {
			'dni':'DNI', 
			'nombre':'Nombre',
			'apellido_paterno':'Apellido Paterno',
			'apellido_materno':'Apellido Materno',
			'fecha_nac':'Fecha de Nacimiento',
			'Celular':'Celular',
			}
		
	    def __init__(self, *args, **kwargs):
	    	super().__init__(*args,**kwargs)
	    	for field in iter(self.fields):
	    		self.fields[field].widget.attrs.update({'class':'form-control'}):



	

	