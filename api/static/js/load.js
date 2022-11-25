

window.logine = async () => {
    Swal.fire({
      position: 'top-end',
      title: '<strong>Recuerda</u></strong>',
      icon: 'info',
      html:
        '<b>Si eres profesor tienes que iniciar con las credenciales que te mando el GREMIO</b>, ' +
        // '<a href="tags.html">Aqui</a> ' +
        '',
      showCloseButton: true,
      showCancelButton: false,
      background: 'var(--bs-body-color)',
      focusConfirm: false,
      confirmButtonText:
        '<a class="col btn" style="color: var(--bs-white);" role="button" href="login">Iniciar sesión</a>',
      // confirmButtonAriaLabel: 'Ir!',
      // cancelButtonText:
      //   '<a href="tags.html">Can</a>',
      // cancelButtonAriaLabel: 'Cerrar'
    })
    
  }

  window.assign = async () => {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-right',
      iconColor: 'green',
      customClass: {
        popup: 'colored-toast'
      },
      showConfirmButton: false,
      timer: 2000,
      timerProgressBar: true,
    })
    await Toast.fire({
      icon: 'success',
      title: 'Se agendo correctamente la clase'
    })
    }

window.logen = async () => {
  Swal.fire({
    title: 'Inicio de session',
    html: `<input type="text" id="login" class="swal2-input" placeholder="nombre">
    <input type="password" id="password" class="swal2-input" placeholder="contraseña">`,
    confirmButtonText: 'Sign in',
    focusConfirm: false,
    background: 'var(--bs-body-color)',
      confirmButtonText:
        '<a class="col btn" style="color: var(--bs-white);" role="button" onclick="itprofe()">Iniciar sesión</a>',
    preConfirm: () => {
      const login = Swal.getPopup().querySelector('#login').value
      const password = Swal.getPopup().querySelector('#password').value
      if (!login || !password) {
        Swal.showValidationMessage(`Por favor ingresa credenciales validas`)
      } else {
        window.location.assign(('profe'));
      }
      }
    }
)}

function test() {
  let detecte = document.getElementById('login')
  if (detecte=="profe") {
    window.location.assign(profe)
  } else {
    errrores()
  }
}

function itprofe() {  
  if (document.getElementById("login") == 'profesor') {
    window.location.assign(('profe'));
  }
  else {
     if (document.getElementById("login") == 'alumno')
     errrores()
  }
}

window.errrores= async () => {
  const Toast = Swal.mixin({
    toast: true,
    position: 'top-right',
    iconColor: 'red',
    customClass: {
      popup: 'colored-toast'
    },
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
  })
  await Toast.fire({
    icon: 'error',
    title: 'usuario bloqueado'
  })
  }