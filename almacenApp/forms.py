from django import forms

from .models  import  *
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import get_user_model
from datetime import date, time, datetime
from django.utils import timezone


class update_Usuario(forms.ModelForm):
	
	

	class Meta:
		User = get_user_model()

		model=User
	

		fields=['email','first_name','last_name','cedula' ,'Telefono' , 'groups']

		help_texts = {
            "groups":None,
        }


		labels={
			'email':'correo',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'cedula' :'Cedula' ,
			'Telefono':'tlfn'
			
			
		}

		widgets = {

		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),
		'cedula': forms.TextInput(attrs={'class':'form-control'}),
		
		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		'Telefono': forms.TextInput(attrs={'class':'form-control'}),

		'groups': forms.SelectMultiple(attrs={'class':'form-control'}),
		
		}
	

	
		




class Crea_Usuario(forms.ModelForm):
	
	password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput(
		attrs={'class':'form-control'}
	))


	class Meta:
		User = get_user_model()

		model=User
	

		fields=['email','first_name','last_name', 'Telefono' ,'cedula', 'password' , 'groups' ]
		help_texts = {
            "groups":None,
        }
		


		labels={
			'email':'correo',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'Telefono':'Telefono',
			'cedula': 'Cedula',
			
			'password':'password'
		}


		widgets = {

		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),
		'cedula': forms.TextInput(attrs={'class':'form-control'}),
		'Telefono': forms.TextInput(attrs={'class':'form-control'}),
		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		'groups': forms.SelectMultiple(attrs={'class':'form-control'}),
		
		}

	
	
	

	def clean_first_name(self):

		#patron = re.compile("^\w+$")
		first_name = self.cleaned_data.get('first_name')
		
		
		if not re.match(r'[a-zA-Z\s]+$', first_name) or first_name == "":
			
			raise forms.ValidationError(" Campo Nombre debe ser solo letras y  es un campo obligatorio")

		
		return first_name


	def clean_last_name(self):

		#patron = re.compile("^\w+$")
		last_name = self.cleaned_data.get('last_name')
		
		
		if not re.match(r'[a-zA-Z\s]+$', last_name) or last_name == "":
			
			raise forms.ValidationError("debe campo Apellido ser solo letras y  es un campo obligatorio")

		
		return last_name


	def clean_cedula(self):

		#patron = re.compile("^\w+$")
		cedula = self.cleaned_data.get('cedula')
		
		
		if not re.match(r'\d+$', cedula) or len(cedula)>8:
			
			raise forms.ValidationError("Error! campo Cedula solo debe ser numero y un maximo de 8 caracteres")

		else:
			User = get_user_model()
			if User.objects.filter(cedula =cedula).exists():
				
				
				raise forms.ValidationError("Error! la cedula ya se encuentra en uso")	

		
		return cedula	
	
	
	
	"""The problem is that User refers to django.contrib.auth.models.User 
	and now you have got a Custom User pet.Person assuming you have in the settings.py
	you have to define User with the Custom User model and you can do this with
	get_user_model at the top of the file where you use User"""

	User = get_user_model()
	def clean_email(self):

		email = self.cleaned_data['email']
		q = self.User.objects.filter(email=email).exists()
		if q:
		
			raise forms.ValidationError('Email ya esta en uso') 

		return email	

		

	def clean(self):
		data = super().clean()

		password= data['password']
		password_confirmation = data['password_confirmation']
		
		
		
		if password != password_confirmation:
			raise forms.ValidationError('Las contrañas no coninciden ')

		

	def save(self):
		#esta funcion es para guardar los datos
		data = self.cleaned_data
		data.pop('password_confirmation')#este campo es para eliminar por que no lo necesito
		user= User.objects.create_user(**data)
		profile= Profile(user=user)
		profile.save()






class Registar_Misil_form(forms.ModelForm):
	
	

	class Meta:
	

		model=Misil
	

		fields=['numero_misil','version','fecha_creacion','peso'  ,
		'velocidad' ,'diametro_cuerpo' , 'largo'  , 'alcance_max' , 'masa_combustible'  , 'masa_sustancia_explosiva']

		


		labels={
			'numero_misil':'Nr Misil',
			'version':'version',
			'fecha_creacion':'Fecha de Creacion',
			'peso': 'Peso',
			'velocidad' :'Velocidad' ,
			'diametro_cuerpo':'Diametro de Cuerpo',
			'largo':'Largo',
			'alcance_max':'Alcance Maximo',
            'masa_combustible':'Masa de Combustible',
            'masa_sustancia_explosiva':'Masa de Sustancia Explosiva  ',

			
		}


		widgets = {

		'numero_misil': forms.TextInput(attrs={'class':'form-control'}),
		'version': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_creacion': forms.DateInput(attrs={'type':'date' , 'class':'form-control'}, format=('%Y-%m-%d')),

		'peso': forms.TextInput(attrs={'class':'form-control'}),
		'velocidad': forms.TextInput(attrs={'class':'form-control'}),
		'diametro_cuerpo': forms.TextInput(attrs={'class':'form-control'}),
		'largo': forms.TextInput(attrs={'class':'form-control'}),


		'alcance_max': forms.TextInput(attrs={'class':'form-control'}),
        'masa_combustible': forms.TextInput(attrs={'class':'form-control'}),
        'masa_sustancia_explosiva': forms.TextInput(attrs={'class':'form-control'}),

		


		
		
		}



	def clean_fecha_creacion(self):

		fecha_creacion= self.cleaned_data.get('fecha_creacion')
		fecha_actual = timezone.now()
		

		if  fecha_creacion >= fecha_actual :

			raise ValidationError("Valor en campo fecha creacion no puede ser mayor a fecha actual ")

		return fecha_creacion

		
				

	def clean_numero_misil(self):
		numero_misil = self.cleaned_data.get('numero_misil')
		
		if not re.match(r'[0-9]', str(numero_misil)):
		
			
			raise forms.ValidationError("debe ser solo  numeros y  es un campo obligatorio")

		return numero_misil	


	def clean_version(self):
		version = self.cleaned_data.get('version')
		
		if not re.match(r'[a-zA-Z\s]+$', str(version)):
		
			
			raise forms.ValidationError("Campo version debe ser solo  letras y  es un campo obligatorio")

		return version	



	def clean_peso(self):
		peso = self.cleaned_data.get('peso')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(peso)):
		
			
			raise forms.ValidationError("Campo peso solo se deben ingresar numero y letras")

		return peso	


	def clean_velocidad(self):
		velocidad = self.cleaned_data.get('velocidad')
		
		if not re.match(r'[a-zA-Z0-9-/]+$', str(velocidad)):
		
			
			raise forms.ValidationError("Campo velocidad solo se deben ingresar numero y letras")

		return velocidad



	def clean_diametro_cuerpo(self):
		diametro_cuerpo = self.cleaned_data.get('diametro_cuerpo')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(diametro_cuerpo)):
		
			
			raise forms.ValidationError("campo Diametro de cuerpo solo se deben ingresar numero y letras")

		return diametro_cuerpo	

	def clean_largo(self):
		largo = self.cleaned_data.get('largo')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(largo)):
		
			
			raise forms.ValidationError("campo Largo solo se deben ingresar numero y letras")

		return largo


	def clean_alcance_max(self):
		alcance_max = self.cleaned_data.get('alcance_max')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(alcance_max)):
		
			
			raise forms.ValidationError("campo alcance maximo solo se deben ingresar numero y letras")

		return alcance_max


	def clean_masa_combustible(self):
		masa_combustible = self.cleaned_data.get('masa_combustible')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(masa_combustible)):
		
			
			raise forms.ValidationError("campo Masa de  combustible solo se deben ingresar numero y letras")

		return masa_combustible	


	def clean_masa_sustancia_explosiva(self):
		masa_sustancia_explosiva = self.cleaned_data.get('masa_sustancia_explosiva')
		
		if not re.match(r'[a-zA-Z0-9_]+$', str(masa_sustancia_explosiva)):
		
			
			raise forms.ValidationError("campo mase de sustancia explosiva solo se deben ingresar numero y letras")

		return masa_sustancia_explosiva			

	
							
				





class DetalleExtra_Misil_form(forms.ModelForm):
	
	

	class Meta:
	

		model=DetallesExtras
	

		fields=['serial','numero_fabricacion','lote_relacion','condicion'  ,
		'fecha_vencimiento' ,'fecha_ultimo_mantenimiento' , 'fecha_ultima_comprobacion',
         'descripcion' , 'imagen1'  , 'imagen2' , 'imagen3']

		


		labels={
			'serial':'Serial',
			'numero_fabricacion':'Numero de Fabricacion',
			'lote_relacion':'Lote',
			'condicion': 'Condicion',
			'fecha_vencimiento' :'Fecha de Vencimiento' ,
			'fecha_ultimo_mantenimiento':'Fecha de Ultimo Mantenimiento',
			'fecha_ultima_comprobacion':'fecha de Ultima Comprobacion',
			'descripcion':'Descripcion',
            'imagen1':'Imagen Nr1',
            'imagen2':'Imagen Nr2',
            'imagen3':'Imagen Nr3',

			
		}


		widgets = {

		'serial': forms.TextInput(attrs={'class':'form-control'}),
		'numero_fabricacion': forms.TextInput(attrs={'class':'form-control'}),
		'lote_relacion': forms.Select(attrs={'class':'form-control'}),

		'condicion': forms.Select(attrs={'class':'form-control'}),
		'fecha_vencimiento': forms.DateInput(attrs={'type':'date' , 'class':'form-control'} , format=('%Y-%m-%d')),
		'fecha_ultimo_mantenimiento': forms.DateInput(attrs={'type':'date' , 'class':'form-control'} , format=('%Y-%m-%d')),
		'fecha_ultima_comprobacion': forms.DateInput(attrs={'type':'date' , 'class':'form-control'} , format=('%Y-%m-%d')),


		'descripcion': forms.Textarea(attrs={'class':'form-control'}),
       

		
		
		}


	def clean_fecha_ultimo_mantenimiento(self):

		fecha_ultimo_mantenimiento= self.cleaned_data.get('fecha_ultimo_mantenimiento')
		fecha_actual = timezone.now()
		

		if  fecha_ultimo_mantenimiento > fecha_actual :

			raise ValidationError("Valor en campo fecha ultimo mantenimiento no puede ser mayor a fecha actual ")

		return fecha_ultimo_mantenimiento	



	def clean_fecha_ultima_comprobacion(self):

		fecha_ultima_comprobacion= self.cleaned_data.get('fecha_ultima_comprobacion')
		fecha_actual = timezone.now()
		

		if  fecha_ultima_comprobacion > fecha_actual :

			raise ValidationError("Valor en campo fecha ultima comprobacion no puede ser mayor a fecha actual ")

		return fecha_ultima_comprobacion

	def clean_condicion(self):
		condicion = self.cleaned_data.get('condicion')
		
		if not re.match(r'[a-zA-Z\s]+$', str(condicion)):
		
			
			raise forms.ValidationError("campo Condicion debe ser solo  letras y  es un campo obligatorio")

		return condicion


	def clean_descripcion(self):
		descripcion = self.cleaned_data.get('descripcion')
		
		if not re.match(r'[a-zA-Z\s]+$', str(descripcion)):
		
			
			raise forms.ValidationError("Campo Desscripcion debe ser solo  letras y  es un campo obligatorio")

		return descripcion		

