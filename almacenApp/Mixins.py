from django.http import request
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404




class obtenvalor_mixin(object):
    

    def realiza_proceso_mixin(self , dato):
        
        query=  get_object_or_404(self.model , numero_misil= dato)
        query2 = get_object_or_404(self.second_model , relacion= query.id)
        return query2
  
        




class validarPermisosRequeridosMixin(object):

    permission_required = ''
    url_redirect = None

    def get_perms(self):

        if isinstance(self.permission_required , str):

            perms=(self.permission_required)

        else:

            perms= self.permission_required

        return perms    


    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('almacenApp:lista_m')

        return self.self.url_redirect   

    def dispatch(self , request , *args , **kwargs):
  
        if request.user.has_perm(self.get_perms()):
            
            return super().dispatch(request , *args , **kwargs)
     
        messages.error(request, 'no tiene permitido el acceso')    
        return redirect(self.get_url_redirect())    


