

function listar_misiles(){

    $.ajax({
        // la url es la que aparece en el navegador , NO es la forma en la que se ponen normalmente las rutas en django
        url:"/misil/lista_m/",
        type:"get",
        dataType:"json",
        success:function(response){
            console.log(response)
            
           

          
            for (let x = 0; x < response.length; x++) {
                let fila1 ="<div class='col-md-3'>";
                
                 if (response[x]['fields']['condicion']==1) {
                     
               
                    fila1+= '<a id="misil_naranja" style="hover:orange;"  href="/misil/detalle_m/'+response[x]['pk'] +'">'
                    fila1+='<h3 style="color: orangered;">_______________</h3>'

                    fila1 += '<label id="misil_naranja" style="size: 5px; color:white;" >' + 'Misil Nro: '  +response[x]['pk']   + '</label>';
                    fila1+='<br>'
                    fila1 += '<label id="misil_naranja" style="size: 5px; color: white;" >' + 'Serial Nro: '  +response[x]['fields']['serial']  + '</label>';

                    
                    fila1+=  '</a>';

                    fila1+='</div>'
                    fila1+='</div>'




                    // fila1+=  '<a href="/misil/detalle_m/ '+response[x]['pk'] +'">detalle</a>';
                    // fila1+='<h1>-------------------</h1>'
                    
                    $('#div_id #div_rowid').append(fila1);
                }
            }

             
            for (let x = 0; x < response.length; x++) {
                let fila2 ="<div class='col-md-3'>";
                
                 if (response[x]['fields']['condicion']==2) {
                     
               
                    fila2+= '<a id="misil_naranja" style="hover:blue;"  href="/misil/detalle_m/'+response[x]['pk'] +'">'
                    fila2+='<h3 style="color: blue;">_______________</h3>'

                    fila2 += '<label id="misil_naranja" style="size: 5px; color:white;" >' + 'Misil Nro: '  +response[x]['pk']   + '</label>';
                    fila2+='<br>'
                    fila2 += '<label id="misil_naranja" style="size: 5px; color: white;" >' + 'Serial Nro: '  +response[x]['fields']['serial']  + '</label>';

                    
                    fila2+=  '</a>';

                    fila2+='</div>'
                    fila2+='</div>'






                    // fila1+=  '<a href="/misil/detalle_m/ '+response[x]['pk'] +'">detalle</a>';
                    // fila1+='<h1>-------------------</h1>'
                    
                    $('#div_id_aptos #div_rowid_aptos').append(fila2);
                }
            }





            for (let x = 0; x < response.length; x++) {
                let fila3 ="<div class='col-md-3'>";
                
                 if (response[x]['fields']['condicion']==3) {
                     
               
                    fila3+= '<a id="misil_naranja" style="hover:red;"  href="/misil/detalle_m/'+response[x]['pk'] +'">'
                    fila3+='<h3 style="color: red;">_______________</h3>'

                    fila3 += '<label id="misil_naranja" style="size: 5px; color:white;" >' + 'Misil Nro: '  +response[x]['pk']   + '</label>';
                    fila3+='<br>'
                    fila3 += '<label id="misil_naranja" style="size: 5px; color: white;" >' + 'Serial Nro: '  +response[x]['fields']['serial']  + '</label>';

                    
                   


                    // fila1+=  '<a href="/misil/detalle_m/ '+response[x]['pk'] +'">detalle</a>';
                    // fila1+='<h1>-------------------</h1>'
                    
                    $('#div_id_Noaptos #div_rowid_Noaptos').append(fila3);
                   
                }
            }





            for (let x = 0; x < response.length; x++) {
                let fila4 ="<div class='col-md-4'>";
                
                 if (response[x]['fields']['condicion']==4) {
                     
               
                    fila4+= '<a id="misil_naranja" style="hover:red;"  href="/misil/detalle_m/'+response[x]['pk'] +'">'
                    fila4+='<h4 style="color: red;">_______________</h4>'

                    fila4 += '<label id="misil_naranja" style="size: 5px; color:white;" >' + 'Misil Nro: '  +response[x]['pk']   + '</label>';
                    fila4+='<br>'
                    fila4 += '<label id="misil_naranja" style="size: 5px; color: white;" >' + 'Serial Nro: '  +response[x]['fields']['serial']  + '</label>';

                    
                   


                    // fila1+=  '<a href="/misil/detalle_m/ '+response[x]['pk'] +'">detalle</a>';
                    // fila1+='<h1>-------------------</h1>'
                    
                    $('#div_id_enconservacion #div_rowid_enconservacion').append(fila4);
                   
                }
            }






        },
        error:function (error){
         
            console.log(error)
        }
        
    });
}








 function mensaje_error(obj){
    let error = "";
    $.each(obj.responseJSON.error , function(key , value) {
        
        error+=  '<div class="alert alert-danger"><strong>' + key + "  " +  value  +'</strong></div>';

        
     });
    
     $('#errores').append(error);   
 }


 function mensaje_error2(obj){
    let errorn2 = "";
    $.each(obj.responseJSON.error2 , function(key , value) {
        
        errorn2+=  '<div class="alert alert-danger"><strong>' + key + "  " +  value  +'</strong></div>';

        
     });
    
     $('#errores').append(errorn2);   
 }
 


  



function registar(){
  



    var nr_misil = document.getElementById("id_numero_misil")
    var version = document.getElementById("id_version")
    var fechacreacion = document.getElementById("id_fecha_creacion")
    var peso = document.getElementById("id_peso")
    
    var  velocidad = document.getElementById("id_velocidad")
    var  daimetro = document.getElementById("id_diametro_cuerpo")
    var  largo = document.getElementById("id_largo")
    var  alcance = document.getElementById("id_alcance_max")
    
    var masacombustible = document.getElementById("id_masa_combustible")
    var masaexplosiva = document.getElementById("id_masa_sustancia_explosiva")
    var  serial = document.getElementById("id_serial")
    var  numerofabricacion = document.getElementById("id_numero_fabricacion")
    var  lote = document.getElementById("id_lote_relacion")
    var  condicion = document.getElementById("id_condicion")
    var  vencimiento = document.getElementById("id_fecha_vencimiento")
    var  mantenimiento = document.getElementById("id_fecha_ultimo_mantenimiento")
    var  comprobacion = document.getElementById("id_fecha_ultima_comprobacion")
    var  descripcion = document.getElementById("id_descripcion")
    var  imagen1 = document.getElementById("id_imagen1")
    var  imagen2 = document.getElementById("id_imagen2")
    var  imagen3 = document.getElementById("id_imagen3")
    var csrf = document.getElementsByName("csrfmiddlewaretoken")
    
    
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken' , csrf[0].value)
    fd.append('numero_misil' , nr_misil.value)
    fd.append('version' , version.value)
    fd.append('fecha_creacion' , fechacreacion.value)
    fd.append('peso' , peso.value)
    fd.append('velocidad' , velocidad.value)
    fd.append('diametro_cuerpo' , daimetro.value)
    fd.append('largo' , largo.value)
    fd.append('alcance_max' , alcance.value)
    fd.append('masa_combustible' , masacombustible.value)
    fd.append('masa_sustancia_explosiva' , masaexplosiva.value)
    fd.append('serial' , serial.value)
    fd.append('numero_fabricacion' , numerofabricacion.value)
    fd.append('lote_relacion' , lote.value)
    fd.append('condicion' , condicion.value)
    fd.append('fecha_vencimiento' , vencimiento.value)
    fd.append('fecha_ultimo_mantenimiento' , mantenimiento.value)
    fd.append('fecha_ultima_comprobacion' , comprobacion.value)
    fd.append('descripcion' , descripcion.value)
    
    fd.append('imagen1' , imagen1.files[0])
    fd.append('imagen2' , imagen2.files[0])
    fd.append('imagen3' , imagen3.files[0])
 
    $.ajax({
        // la url es la que aparece en el navegador , NO es la forma en la que se ponen normalmente las rutas en django
        type: "POST",
        data:fd,
        url:$("#form_creacion").attr('action'),
        
        
        success:function(response){

            alert("Misil registrado con exito!")
           
            window.location.replace("/misil/lista_m/"); 
      
        },
        error:function (errores){

          
            mensaje_error(errores)
            mensaje_error2(errores)
           
        },
        cache:false,
        contentType:false,
        processData:false
        
    });
    
    }




$(document).ready(function(){

    listar_misiles();
   

});