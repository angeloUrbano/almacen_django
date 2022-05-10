from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.





class User(AbstractUser):
	email = models.EmailField(unique=True)
	cedula = models.CharField(max_length=100 , blank=False, null= False)
	telefono_regex= RegexValidator(
		regex=r'\+?1?\d{9,15}$',
		message = 'formato permitido +999999999'
		)
	Telefono = models.CharField(validators=[telefono_regex], max_length=10 )
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS=[ 'username',  'first_name' , 'last_name'  , 'cedula' , 'Telefono']


""" version 
	creacion
	peso
	velocidad
	diametro del cuerpo
	largo
	alcance maximo
	masa de combustible
	masa de la sustancia explosiva
"""



"""
		serial
		numero de fabricacion
		lote "que se divide en 3"
		condicion
		fecha de vencimiento
		fecha de ultimo mantenimiento
		fecha de ultima comprobacion
		descripcion

"""



class Misil(models.Model):

	numero_misil = models.IntegerField(unique=True)
	version  = models.CharField(error_messages={'unique': 'Prueba de error.'}, max_length=100)
	fecha_creacion = models.DateTimeField()
	peso = models.CharField(max_length=100)
	velocidad = models.CharField(max_length=100)
	diametro_cuerpo = models.CharField(max_length=100)
	largo = models.CharField(max_length=100)
	alcance_max =  models.CharField(max_length=100)
	masa_combustible = models.CharField(max_length=100)
	masa_sustancia_explosiva = models.CharField(max_length=100)
	fecha_creacionde_registro= models.DateTimeField(auto_now_add=True)
 

	def __str__(self):
		return self.version




class Lote(models.Model):
	nombre_lote = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre_lote


class Condicion(models.Model):
	nombre_condicion = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre_condicion





class DetallesExtras(models.Model):

	relacion = models.OneToOneField(Misil ,  on_delete=models.CASCADE)   
	serial  = models.IntegerField(unique=True)
	numero_fabricacion = models.IntegerField()
	lote_relacion =  models.ForeignKey(Lote ,  on_delete=models.CASCADE)  
	condicion = models.ForeignKey(Condicion ,  on_delete=models.CASCADE) 
	fecha_vencimiento = models.DateTimeField()
	fecha_ultimo_mantenimiento= models.DateTimeField()
	fecha_ultima_comprobacion = models.DateTimeField()
	descripcion = models.TextField(max_length=250)
	imagen1 = models.ImageField(upload_to='imagenes/')
	imagen2 = models.ImageField(upload_to='imagenes/')
	imagen3 = models.ImageField(upload_to='imagenes/')



	

	def __str__(self):
		return self.condicion

