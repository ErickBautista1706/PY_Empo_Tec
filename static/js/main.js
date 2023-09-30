document.addEventListener('DOMContentLoaded', () => {
  const btnModeDark = document.querySelector('.btnModeDark');
  const btnUserR = document.querySelector('.btnUserR');
  const btnProfR = document.querySelector('.btnProfR');
  let darkModeEnabled = localStorage.getItem('darkModeEnabled') === 'true';

  // Función para cambiar el modo oscuro
  function toggleDarkMode() {
    // Obtiene el elemento body
    const body = document.querySelector('body');

    // Cambia el estado del modo oscuro
    darkModeEnabled = !darkModeEnabled;

    // Aplica la clase 'dark-mode' al body si el modo oscuro está habilitado, o la elimina si está deshabilitado
    if (darkModeEnabled) {
      body.classList.add('dark-mode');
    } else {
      body.classList.remove('dark-mode');
    }

    // Guarda el estado del modo oscuro en localStorage
    localStorage.setItem('darkModeEnabled', darkModeEnabled.toString());
  }
  if (darkModeEnabled) {
    const body = document.querySelector('body');
    body.classList.add('dark-mode');
  }

  if (btnModeDark) {
    btnModeDark.addEventListener('click', toggleDarkMode);
  }

  if (btnUserR) {
    btnUserR.addEventListener('click', () => {
      showAlert('Usuario');
    });
  }

  if (btnProfR) {
    btnProfR.addEventListener('click', () => {
      showAlert('Profesor/a');
    });
  }
});

function showAlert(role) {
  Swal.fire({
    icon: 'info',
    title: `Registro de ${role}`,
    text: `Por el momento, solo los estudiantes pueden registrarse.`,
    confirmButtonText: 'Entendido',
  });
}

function setRol(rol) {
  document.getElementById('rol').value = rol;
}


function saludoCardIndex() {
  Swal.fire({
    title: '¡Hola!',
    text: 'Empieza a explorar, puede haber sorpresas :D',
    imageUrl: 'https://i.pinimg.com/originals/1b/1e/37/1b1e37721cf248b07ae7ed07966df60b.gif',
    imageWidth: 400,
    imageHeight: 300,
    confirmButtonText: 'Aceptar',
    width: 600,
    padding: '3em',
    color: '#716add',
    backdrop: `
      rgba(0,0,123,0.4)
      url("/images/nyan-cat.gif")
      left top
      no-repeat
    `
  });
}

function btnReg() {
  const nombre = document.getElementById('registerNombre').value;
  const apellido = document.getElementById('registerApellido').value;
  const correo = document.getElementById('registerEmail').value;
  const contrasena = document.getElementById('registerPassword').value;
  const rol = document.getElementById('rol').value;
  const fotoPerfil = document.getElementById('registerFotoPerfil').files[0];
  const fechaNacimiento = document.getElementById('registerFechaNacimiento').value;
  const escuela = document.getElementById('registerEscuela').value;
  const paisOrigen = document.getElementById('registerPaisOrigen').value;

  const formData = new FormData();
  formData.append('nombre', nombre);
  formData.append('apellido', apellido);
  formData.append('email', correo);
  formData.append('password', contrasena);
  formData.append('rol', rol);
  formData.append('fotoPerfil', fotoPerfil);
  formData.append('fechaNacimiento', fechaNacimiento);
  formData.append('escuela', escuela);
  formData.append('paisOrigen', paisOrigen);

  $.ajax({
    url: '/registro',
    type: 'POST',
    data: formData,
    processData: false,
    contentType: false,
    success: function(response) {
      if (response.success) {
        Swal.fire({
          icon: 'success',
          title: 'Registro exitoso',
          text: 'Tu registro ha sido exitoso. ¡Bienvenido!',
          confirmButtonText: 'Ir al inicio'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = '/login';

          }
        });
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Error de registro',
          text: 'Hubo un problema al registrar el usuario. Por favor, inténtalo de nuevo.',
          confirmButtonText: 'Aceptar'
        });
      }
    },
    error: function(error) {
      console.error(error);
    }
  });
}


