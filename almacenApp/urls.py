from django.urls import path

from almacenApp.views import *

get_misil_number
urlpatterns = [
    path('prueba/',  prueba.as_view() , name="prueba"),
     path('Registro_misil/',  registrar_misil.as_view() , name="Registro_misil"),
      path('lista_m/',  lista_misiles.as_view() , name="lista_m"),
       path('editar_m/<int:pk>',  editar_misil.as_view() , name="editar_m"),
        path('eliminar_m/<int:pk>',  eliminar_misil.as_view() , name="eliminar_m"),
         path('detalle_m/<int:pk>',  detalle_misil.as_view() , name="detalle_m"),
          path('inicio_m/',  inicil_misiles.as_view() , name="inicio_m"),
           path('crear_usu/',  crear_usuario.as_view() , name="crear_usu"),
            path('listar_usu/',  listar_user.as_view() , name="listar_usu"),
             path('editar_usu/<int:pk>',  editar_usuario.as_view() , name="editar_usu"),
              path('lsiatr_l1/', listar_lote1.as_view() , name="lsiatr_l1"),
              path('lsiatr_l2/', listar_lote2.as_view() , name="lsiatr_l2"),
              path('lsiatr_l3/', listar_lote3.as_view() , name="lsiatr_l3"),
              path('get_misil_number1/', get_misil_number.as_view() , name="get_misil_number1"),
]
