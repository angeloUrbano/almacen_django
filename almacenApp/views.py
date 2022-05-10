from django.shortcuts import render, redirect
from django.http.response import HttpResponse , JsonResponse
from django.urls import reverse , NoReverseMatch

from almacenApp.models import *
from django.views.generic import  View ,TemplateView , ListView , UpdateView ,CreateView , DeleteView ,DetailView
from django.urls import reverse_lazy

from django.contrib import messages

import json
from django.core.serializers import serialize
from almacenApp.forms import Registar_Misil_form , DetalleExtra_Misil_form ,  Crea_Usuario , update_Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth import get_user_model



from almacenApp.Mixins import validarPermisosRequeridosMixin , obtenvalor_mixin
from django.contrib.auth.mixins import LoginRequiredMixin









def error_404(request, exception):
    return render(request , "404.html")




class get_misil_number(LoginRequiredMixin , obtenvalor_mixin , View):
	model = Misil
	second_model = DetallesExtras
	template_name = "misil/numero_misil.html"
	
	

	def get(self , request , *args ,**kwargs):

		dato = request.GET.get('prueba')
		variable = super().realiza_proceso_mixin(dato)
		url = reverse('almacenApp:detalle_m' , kwargs={'pk':variable.relacion.id})
		return redirect(url)





class lista_misiles(LoginRequiredMixin  , View):
	model = DetallesExtras
	template_name = "misil/lista_misiles.html"

	def get_queryset(self):
		query = self.model.objects.all()
		return query
	
	

	def get(self , request , *args , **kwargs):
		self.object_list = self.get_queryset()
		if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			
			#eso del serialize cambia en el detailview
			data = serialize('json' , self.get_queryset())
			
			return HttpResponse(data , 'application/json')

		else:
			
			return redirect('almacenApp:inicio_m')







class registrar_misil(LoginRequiredMixin , validarPermisosRequeridosMixin , View):
	permission_required = 'almacenApp.add_misil'
	model = Misil
	second_model= DetallesExtras
	third_model = Lote
	four_model= Condicion
	form_class = Registar_Misil_form
	second_form_class = DetalleExtra_Misil_form
	template_name = "misil/registro_misil.html"
	second_template_name = "misil/prueba.html"
	success_url = reverse_lazy('almacenApp:prueba')




	def get_context_data(self , **kwargs):
		context = {}
		context['form'] = self.form_class
		context['form2'] = self.second_form_class
		return context

	def post(self , request , *args , **kwargs):

		is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
		if is_ajax:
			form = self.form_class(request.POST)
			form2 = self.second_form_class(request.POST , request.FILES)
			if form.is_valid() and form2.is_valid():
				form.save()
				misil_extra_info_object =  self.second_model()
				# I get the last misil create
				consulta1 =  self.model.objects.latest('fecha_creacionde_registro')
				# I get the name's lote
				consulta2= self.third_model.objects.get(nombre_lote = form2.cleaned_data['lote_relacion'])
				consulta3= self.four_model.objects.get(nombre_condicion = form2.cleaned_data['condicion'])
				misil_extra_info_object.relacion = consulta1
				misil_extra_info_object.serial = form2.cleaned_data['serial']
				misil_extra_info_object.numero_fabricacion  =form2.cleaned_data['numero_fabricacion']
				misil_extra_info_object.lote_relacion = consulta2
				misil_extra_info_object.condicion =consulta3
				misil_extra_info_object.fecha_vencimiento =form2.cleaned_data['fecha_vencimiento']
				misil_extra_info_object.fecha_ultimo_mantenimiento =form2.cleaned_data['fecha_ultimo_mantenimiento']
				misil_extra_info_object.fecha_ultima_comprobacion =form2.cleaned_data['fecha_ultima_comprobacion']
				misil_extra_info_object.descripcion = form2.cleaned_data['descripcion']
				misil_extra_info_object.imagen1 =form2.cleaned_data['imagen1']
				misil_extra_info_object.imagen2 =form2.cleaned_data['imagen2']
				misil_extra_info_object.imagen3 =form2.cleaned_data['imagen3']
				misil_extra_info_object.save()
				mensaje=f'{self.model.__name__} registrado correctamente'
				error = 'No hay error'
				response = JsonResponse({'mensaje':mensaje , 'error':error})
				response.status_code = 201
				return response
			else:
				mensaje=f'{self.model.__name__} No registrado correctamente'
				error = form.errors
				error2 = form2.errors
				response = JsonResponse({'mensaje':mensaje , 'error':error ,'error2':error2 })
				response.status_code = 400
				return response
		else:
			
			return redirect('almacenApp:lista_m')
   


	def get(self , request , *args , **kwargs ):
		 return render(request , self.template_name , self.get_context_data())








class crear_usuario(LoginRequiredMixin ,  validarPermisosRequeridosMixin , View):
	permission_required = 'almacenApp.add_user'
	template_name = 'misil/signup.html'
	form_class = Crea_Usuario

	def get (self, request):

		return render(request,self.template_name , {'form':self.form_class})


	def post(self , request , *args , **kwargs):
		form  = self.form_class(request.POST) 
		
		if form.is_valid():
			datos_limpios = form.cleaned_data

			for x in datos_limpios['groups']:
			
				

				email = datos_limpios['email']
				first_name = datos_limpios['first_name']
				last_name = datos_limpios['last_name']
				password = datos_limpios['password']
				password_confirmation = datos_limpios['password_confirmation']
				cedula= datos_limpios['cedula']	
				Telefono = datos_limpios['Telefono']
				User = get_user_model()
				User = User.objects.create_user(username= cedula, email=email , last_name =last_name , password = password , is_active = True ,
				cedula =cedula , first_name = first_name , Telefono=Telefono )


				User.groups.add(x)
			return redirect('almacenApp:listar_usu')

		return render(request , self.template_name , {'form':form})






def login_view(request):
	
	
	if request.method== 'POST':
		
		
		username = request.POST['email']
		password = request.POST['password']
	
		User = authenticate( username=username, password = password)
		
		
		if User :
			
			login(request , User)
		   
			
			return redirect('almacenApp:lista_m')
		else:
			return render(request ,  "misil/login.html" , {'error': 'Correo o Contraseña Invalido'})	
	return render(request , "misil/login.html")




@login_required
def logout_view(request):
	logout(request)
	return redirect('login') 




class prueba (TemplateView):
	
	template_name = "misil/prueba.html"








class listar_user(LoginRequiredMixin  , validarPermisosRequeridosMixin , ListView):
	permission_required = 'almacenApp.view_user'
	
	model = User
	template_name = 'misil/lista_user.html'





class editar_usuario( LoginRequiredMixin  , validarPermisosRequeridosMixin , UpdateView):
	permission_required = 'almacenApp.change_user'
	model= User
	form_class =  update_Usuario
	template_name ='misil/editar_usuario.html'
	success_url= reverse_lazy('almacenApp:listar_usu')



    




#para evitar el error de que me muestre el json cuando navego de atras hacia delante en el sistema 
class inicil_misiles(LoginRequiredMixin , TemplateView):
	template_name = "misil/lista_misiles.html"
	model = DetallesExtras
	

	def get_queryset(self):
		query = self.model.objects.all()
		return query
	
	def get_context_data(self ,   **kwargs):
		context ={}
		context['object_list'] = self.get_queryset()
		return context







class listar_lote1(LoginRequiredMixin  , ListView):
	model = DetallesExtras
	template_name = "misil/lista_misiles_lote1.html"

	def get_queryset(self):
		query= self.model.objects.filter(lote_relacion=1)
		return query





class listar_lote2(LoginRequiredMixin  , ListView):
	model = DetallesExtras
	template_name = "misil/lista_misiles_lote2.html"

	def get_queryset(self):
		query= self.model.objects.filter(lote_relacion=2)
		return query





class listar_lote3(LoginRequiredMixin  ,ListView):
	model = DetallesExtras
	template_name = "misil/lista_misiles_lote3.html"

	def get_queryset(self):
		query= self.model.objects.filter(lote_relacion=3)
		return query





class editar_misil(LoginRequiredMixin  , validarPermisosRequeridosMixin , UpdateView):
	permission_required = 'almacenApp.change_misil'
	model=  Misil
	second_model= DetallesExtras
	form_class =  Registar_Misil_form
	second_form_class = DetalleExtra_Misil_form  
	template_name = "misil/editar_misil.html"

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		consulta = self.second_model.objects.get(relacion = self.kwargs['pk'])
		context['form2'] = self.second_form_class(instance = consulta )
		return context


	def post(self , request , *args , **kwargs):
		instancia = self.model.objects.get(id=self.kwargs['pk'])
		instancia2 = self.second_model.objects.get(relacion = self.kwargs['pk'])
		form  = self.form_class(request.POST , instance=instancia)
		form2 = self.second_form_class(request.POST , request.FILES , instance=instancia2)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return redirect('almacenApp:lista_m')
		return render(request , self.template_name , {'form':form ,'form2':form2 }) 





class eliminar_misil(LoginRequiredMixin  ,  validarPermisosRequeridosMixin , DeleteView):
	permission_required = 'almacenApp.change_misil'
	model= DetallesExtras
	template_name = "misil/eliminar_misil.html"
	success_url = reverse_lazy('almacenApp:lista_m')




class detalle_misil(LoginRequiredMixin  ,  DetailView):
	model = Misil
	second_model = DetallesExtras
	template_name ="misil/detalle_misil.html"
	pk_url_kwargs = 'pk'
		
	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		consulta1 = self.model.objects.get(id = self.kwargs['pk'])
		consulta2 = self.second_model.objects.get(relacion = self.kwargs['pk'])
		context['datos_misil']=consulta1
		context['datos_extras_misil']= consulta2
		return context





		
		
	

	

	

		
