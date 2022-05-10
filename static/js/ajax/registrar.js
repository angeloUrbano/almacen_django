


function registar(){


    var fd = new FormData(document.getElementById("form_creacion"));
    $.ajax({
        // la url es la que aparece en el navegador , NO es la forma en la que se ponen normalmente las rutas en django

        data:fd,
        url:$("#form_creacion").attr('action'),
        type: "POST",
        
        success:function(response){
            console.log("aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            console.log(response)
      
        },
        error:function (error){
         
            console.log(error)
        }
        
    });

}

