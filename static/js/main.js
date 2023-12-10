document.addEventListener('DOMContentLoaded', () => {
  const btnModeDark = document.querySelector('.btnModeDark');
  const btnUserR = document.querySelector('.btnUserR');
  const btnProfR = document.querySelector('.btnProfR');
  let darkModeEnabled = localStorage.getItem('darkModeEnabled') === 'true';
  const switchToggle = document.getElementById('switch-toggle');
  const modeLabel = document.getElementById('mode-label');

  function toggleDarkMode() {
    const body = document.querySelector('body');

    darkModeEnabled = !darkModeEnabled;

    if (darkModeEnabled) {
      body.classList.add('dark-mode');
      modeLabel.textContent = 'Modo Oscuro';
    } else {
      body.classList.remove('dark-mode');
      modeLabel.textContent = 'Modo Claro';

    }


    localStorage.setItem('darkModeEnabled', darkModeEnabled.toString());


    document.getElementById('switch-toggle').checked = darkModeEnabled;
  }


  if (switchToggle) {
    switchToggle.checked = darkModeEnabled;
    switchToggle.addEventListener('change', toggleDarkMode);

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

  const validationError = validar_usuarios(nombre, apellido, correo, contrasena, rol, fechaNacimiento, escuela, paisOrigen);

  if (validationError) {
    Swal.fire({
      icon: 'error',
      title: 'Error de registro',
      text: `El campo ${validationError} es obligatorio.`,
      confirmButtonText: 'Aceptar'
    });
    return;
  }

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
    success: function (response) {
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
    error: function (error) {
      console.error(error);
      Swal.fire({
        icon: 'error',
        title: 'Error de registro',
        text: 'Hubo un problema al registrar el usuario. Por favor, inténtalo de nuevo.',
        confirmButtonText: 'Aceptar'
      });
    }
  });
}


function access() {
  const modal = new bootstrap.Modal(document.getElementById('accessibilityModal'));
  modal.show();
}


function translatePage(targetLanguage) {
  const elementsToTranslate = document.querySelectorAll('h1,h2,h3,h4,h5, p, a');
  elementsToTranslate.forEach(element => {
    const text = element.innerText;
    translateText(text, targetLanguage)
      .then(translation => {
        element.innerText = translation;
      })
      .catch(error => console.error('Translation error:', error));
  });
}

async function translateText(text, targetLanguage) {
  const response = await fetch(
    `https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=${targetLanguage}&dt=t&q=${encodeURI(text)}`
  );
  const translation = await response.json();
  return translation[0][0][0];
}

function changeLanguage() {
  const selectedLanguage = document.getElementById('language-select').value;
  translatePage(selectedLanguage);
}


function validar_usuarios(nombre, apellido, correo, psw, rol, fecha, escuela, pais) {
  if (nombre === '') return 'Nombre';
  if (apellido === '') return 'Apellido';
  if (correo === '') return 'Correo electrónico';
  if (psw === '') return 'Contraseña';
  if (rol === '') return 'Rol';
  if (fecha === '') return 'Fecha de nacimiento';
  if (escuela === '') return 'Escuela';
  if (pais === '') return 'País de origen';

  return null;
}