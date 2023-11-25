from models.db import Database
import os
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
from models.cryptography import Cryptography

class Login:
    UPLOAD_FOLDER = 'C:/Users/Erick/Documents/dig-env/static/images/Usuarios'
    global UPLOAD_FOLDER_TECH  # Asegúrate de indicar que estás usando la variable global
    UPLOAD_FOLDER_TECH = 'C:\\Users\\Erick\\Documents\\GitHub\\PY_Empo_Tec\\static\\documents'


    def __init__(self):
        self.cryptography = Cryptography()

    def verificar_credenciales(self, correo, contrasena):
        db = Database()
        
        print("Correo recuperado: ", correo)
        
        query = "SELECT * FROM Usuarios WHERE CorreoElectronico = %s"
        cursor = db.execute_query(query, (correo,))
        resultado = cursor.fetchone()

        if resultado:
            contrasena_en_db = resultado['Contrasena']  # La contraseña almacenada en la base de datos
            cryptography = Cryptography()
            contrasena_fn = cryptography.decrypt_data(contrasena_en_db)
            
            print("Recuperé la contraseña de la BD: ", contrasena_en_db)
            print("Decrypt", contrasena_fn)
            print("Contraseña ingresada por el usuario: ", contrasena)
            
            if contrasena_fn == contrasena:
                print("Las contraseñas coinciden. ¡Éxito!")
                return resultado
            else:
                print("Las contraseñas no coinciden.")
                return None
        else:
            # No se encontró ningún usuario con ese correo
            print("No se encontró ningún usuario con ese correo.")
            return None



    
    def allowed_file(self, filename):
            ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
            return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
                
    def insert_usuario(self, nombre, apellido, correo, contrasena, rol, foto, fecha_nacimiento, pais_origen, instituto_empresa):
        db = Database()

            # Concatena los datos a encriptar
            #datos_a_encriptar = f"{nombre}|{apellido}|{correo}|{contrasena}|{rol}|{fecha_nacimiento}|{pais_origen}|{instituto_empresa}"

            # Encripta los datos (espera una cadena en lugar de bytes)
            #datos_encriptados = self.cryptography.encrypt_data(datos_a_encriptar)
            
            #clave_encriptacion = self.cryptography.get_key()
            #print("Clave de encriptación:", clave_encriptacion)  # Agrega esta línea para imprimir la clave
            

        if foto and self.allowed_file(foto.filename):
            filename = secure_filename(foto.filename)
            nombre_imagen, extension = os.path.splitext(filename)
            nombre_imagen = f"profile_{nombre[:2]}{apellido[:2]}{extension}"
            foto.save(os.path.join(self.UPLOAD_FOLDER, nombre_imagen))
        else:
            nombre_imagen = None

        query = "INSERT INTO Usuarios (Nombre, Apellido, CorreoElectronico, Contrasena, Rol, Imagen, FechaNacimiento, PaisOrigen, InstitutoEmpresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = db.execute_query(query, (nombre, apellido, correo, contrasena, rol, nombre_imagen, fecha_nacimiento, pais_origen, instituto_empresa))
        db.close()

        return True  # Assuming everything went well
    
    def insert_profesor(self, id_usuario, documento, documento_filename):            
            try:
                # Guarda el documento en la carpeta deseada
                documento_path = os.path.join(UPLOAD_FOLDER_TECH, documento_filename)
                documento.save(documento_path)

                # Inserta el profesor en la tabla de profesores
                query = "INSERT INTO profesores (Usuario, DocumentoPath) VALUES (%s, %s)"
                values = (id_usuario, documento_path)
                self.execute_query(query, values)

                return True
            except Exception as e:
                print("Error al insertar profesor:", str(e))
                return False