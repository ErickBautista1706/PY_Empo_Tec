from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from datetime import datetime
from models.cursos import Cursos
from models.Equipo import Equipo
from models.login import Login
from models.inscripciones import Inscripciones
from models.progresoLecciones import ProgresoLecciones
from models.cryptography import Cryptography
import secrets


app = Flask(__name__, static_folder='static')
app.secret_key = secrets.token_hex(1012//2)  # 1024 caracteres para la cookie


def inject_current_year():
    current_year = datetime.now().year
    return dict(current_year=current_year)

@app.route('/')
def index():
    cursos = Cursos()
    cursos_destacados = cursos.get_all_cursos()
    cursos_aleatorios = cursos.get_random_cursos()
    
    equipo = Equipo()
    usuarios_destacados = equipo.get_usuarios_destacados()
    
    return render_template('index.html', cursos=cursos_destacados, cursos_aleatorios=cursos_aleatorios, usuarios_destacados=usuarios_destacados)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['email']
        contrasena = request.form['password']
        
        login = Login()
        usuario_data = login.verificar_credenciales(correo, contrasena)
        
        if usuario_data:
            session['usuario'] = usuario_data
            return redirect(url_for('inicio_exitoso', success=True))  
        else:
            return render_template('login.html', alerta='Inicio de sesión fallido')
    
    return render_template('login.html')

@app.route('/inicio_exitoso')
def inicio_exitoso():
    if 'usuario' in session:
        success = request.args.get('success')
        
        # Obtener el ID del usuario desde la sesión
        usuario_id = session['usuario']['ID']
        
        # Crear instancias de las clases Inscripciones y ProgresoLecciones
        inscripciones = Inscripciones()
        progreso_lecciones = ProgresoLecciones()
        
        # Obtener la lista de inscripciones y progreso de lecciones del usuario
        lista_inscripciones = inscripciones.get_inscripciones_by_usuario(usuario_id)
        lista_progreso = progreso_lecciones.get_progresos_by_usuario(usuario_id)
        
        # Agregar el estado correspondiente a cada inscripción
        for inscripcion in lista_inscripciones:
            for progreso in lista_progreso:
                if progreso['leccion']['curso_id'] == inscripcion['curso']['id']:
                    inscripcion['estado'] = progreso['estado']
        
        return render_template('profile.html', success=success, inscripciones=lista_inscripciones)

    else:
        return redirect(url_for('index'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('email')
        contrasena = request.form.get('password')
        rol = request.form.get('rol')
        foto = request.files.get('fotoPerfil')
        fecha_nacimiento = request.form.get('fechaNacimiento')
        pais_origen = request.form.get('paisOrigen')
        instituto_empresa = request.form.get('escuela')
        
        # Crear una instancia de Login
        login_manager = Login()

        #Encriptar la contraseña
        contrasena_encriptada = login_manager.cryptography.encrypt_data(contrasena)  # <-- Aquí se encripta


        print(f"Datos recibidos del formulario:")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Correo: {correo}")
        print(f"Contraseña encriptada: {contrasena_encriptada}")  # <-- Contraseña ya encriptada

        if login_manager.insert_usuario(nombre, apellido, correo, contrasena_encriptada, rol, foto, fecha_nacimiento, pais_origen, instituto_empresa=instituto_empresa):
            # Registro exitoso, devuelve un mensaje de éxito
            return jsonify({'success': True})
        else:
            # Registro fallido, devuelve un mensaje de error
            return jsonify({'success': False, 'message': 'Error al registrar el usuario'})

        # Agrega un retorno por defecto para el método GET
    return render_template('registro.html')

@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('Login.html')


if __name__ == '__main__':
    app.run(debug=True)
