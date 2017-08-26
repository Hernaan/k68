from __future__ import absolute_import
from django.forms import ModelForm, TextInput
from denuncias.models import Denuncia
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}

class DenunciaForm(forms.ModelForm):

	class Meta:
		model = Denuncia
		exclude = ('user', 'fecha', )
		fields = [
			'descripcion',
			'dn_servicio',
			'dn_tiposervicio',
			'lat',
			'lng',
		]
		labels = {
			'dn_servicio': 'Que esta ocurriendo?',
			'dn_tiposervicio': 'Que tipo de servicio?',
			'descripcion': 'Comenta que esta pasando',	 
			'lat': 'Latitud',
			'lng': 'Longitud',

		}
		widgets = {
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'dn_servicio':forms.Select(attrs={'class':'form-control'}),
			'dn_tiposervicio':forms.Select(attrs={'class':'form-control'}),
			'latitud':forms.HiddenInput(),
			'longitud':forms.HiddenInput(),
			
		}