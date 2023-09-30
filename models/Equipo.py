from models.db import Database

class Equipo:
    def get_usuarios_destacados(self):
        db = Database()
        cursor = db.execute_query("SELECT * FROM Usuarios WHERE ID IN (1,2,6)")
        usuarios_data = cursor.fetchall()
        usuarios = []
        for usuario_data in usuarios_data:
            imagen = usuario_data['Imagen'] if usuario_data['Imagen'] is not None else ''
            usuario = {
                'id': usuario_data['ID'],
                'nombre': usuario_data['Nombre'],
                'apellido': usuario_data['Apellido'],
                'correo': usuario_data['CorreoElectronico'],
                'imagen': imagen
            }
            usuarios.append(usuario)
        cursor.close()
        db.close()
        return usuarios
