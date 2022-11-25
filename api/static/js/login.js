$("#signup").click(function() {
    $("#first").fadeOut("fast", function() {
    $("#second").fadeIn("fast");
    });
    });
    
    $("#signin").click(function() {
    $("#second").fadeOut("fast", function() {
    $("#first").fadeIn("fast");
    });
    });
    
    
      
             $(function() {
               $("form[name='login']").validate({
                 rules: {
                   
                   email: {
                     required: false,
                     email: false
                   },
                   Username: {
                    required: true,
                    email: false
                  },
                   password: {
                     required: true,
                     
                   }
                 },
                  messages: {
                   email: "Ingresa un corrreo valido",
                  
                   password: {
                     required: "Ingresa una contraseña valida",
                    
                   }

                   Username: {
                    required: "Ingresa un nombre valida",
                   
                  }
                   
                 },
                 submitHandler: function(form) {
                   form.submit();
                 }
               });
             });
             
    
    
    $(function() {
      
      $("form[name='registration']").validate({
        rules: {
          firstname: "required",
          lastname: "required",
          email: {
            required: true,
            email: true
          },
          password: {
            required: true,
            minlength: 5
          }
        },
        
        messages: {
          firstname: "No puedes dejar este espacio vacio",
          lastname: "No puedes dejar este espacio vacio",
          password: {
            required: "Por favor proporcione una contraseña",
            minlength: "Tu contraseña debe tener al menos 5 caracteres"
          },
          email: "Por favor ingresa un correo valido"
        },
      
        submitHandler: function(form) {
          form.submit();
        }
      });
    });