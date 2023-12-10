from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from datetime import datetime
from models.cursos import Cursos
from models.Equipo import Equipo
from models.login import Login
from models.inscripciones import Inscripciones
from models.progresoLecciones import ProgresoLecciones
import secrets
import json


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
            return render_template('Login.html')
        else:
            # Registro fallido, devuelve un mensaje de error
            return jsonify({'success': False, 'message': 'Error al registrar el usuario'})

        # Agrega un retorno por defecto para el método GET
    return render_template('registro.html')

@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('Login.html')


@app.route('/inicio_usuario')
def inicio_usuario():
    if 'usuario' in session:
        cursos_aleatorios = Cursos().get_random_cursos()
        usuario_id = session['usuario']['ID']
        inscripciones = Inscripciones().get_inscripciones_by_usuario(usuario_id)

        return render_template('inicio_usuario.html', usuario=session['usuario'], cursos_aleatorios=cursos_aleatorios, inscripciones=inscripciones)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


@app.route('/ver_curso/<int:curso_id>')
def ver_curso(curso_id):
    cursos_handler = Cursos()
    curso = cursos_handler.obtener_curso_por_id(curso_id)
    lecciones = cursos_handler.obtener_lecciones_por_curso(curso_id)
    
    if curso:
        return jsonify(curso=curso, lecciones=lecciones)
    else:
        return jsonify(error='Curso no encontrado'), 404

@app.route("/inscribir_usuario_curso", methods=["POST"]) 
def inscribir_usuario_curso():
    try:
        # Obtén los datos del usuario y curso desde la solicitud
        usuario_id = request.form.get('usuarioId')
        curso_id = request.form.get('cursoId')

        print("get id_user: ", usuario_id, "get_curso: ", curso_id )
        # Llama a la función para inscribir al usuario en el curso
        cursos = Cursos()  # Suponiendo que tienes una instancia de la clase Cursos
        exito = cursos.inscribir_usuario_en_curso(usuario_id, curso_id)

        # Devuelve una respuesta JSON indicando si la inscripción fue exitosa
        if exito:
            return jsonify({'success': True, 'message': 'Registro Existoso.'}), 200
        else:
            return jsonify({'success': False, 'message': 'Error al registrarse.'}), 500

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500
    
@app.route('/continuar_curso/<int:curso_id>')
def mostrar_curso(curso_id):
    curso_handler = Cursos()
    curso = curso_handler.obtener_curso_por_id(curso_id)
    if curso:
        # Obtén las lecciones del curso
        lecciones = curso_handler.obtener_lecciones_por_curso(curso_id)
        return render_template('curso.html', curso=curso, lecciones=lecciones)
    else:
        # Si el curso no existe, puedes redirigir a una página de error o manejarlo de otra forma
        return "Curso no encontrado", 404

@app.route('/eliminar_inscripcion', methods=['POST'])
def eliminar_inscripcion():
    inscripcion_id = request.form.get('inscripcion_id')  # Asegúrate de enviar el 'inscripcion_id' desde tu AJAX

    curso_handler = Cursos()
    exito = curso_handler.eliminar_inscripcion_por_id(inscripcion_id)

    if exito:
        return jsonify({'success': True, 'message': 'Inscripción eliminada con éxito'})
    else:
        return jsonify({'success': False, 'message': 'Error al eliminar la inscripción'})

@app.route('/library')
def library():
    with open('static/data/library.json') as f:
        library_data = json.load(f)
        
    return render_template('library.html', library_data=library_data)


if __name__ == '__main__':
    app.run(debug=True)
