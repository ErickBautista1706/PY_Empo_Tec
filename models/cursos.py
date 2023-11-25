import random
from models.db import Database

class Cursos:
    def get_all_cursos(self):
        db = Database()
        cursor = db.execute_query("SELECT * FROM Cursos")
        cursos_data = cursor.fetchall()
        cursos = []
        for curso_data in cursos_data:
            imagen = curso_data['Imagen'] if curso_data['Imagen'] is not None else ''
            curso = {
                'id': curso_data['ID'],
                'titulo': curso_data['Titulo'],
                'descripcion': curso_data['Descripcion'],
                'duracion': curso_data['Duracion'],
                'nivel': curso_data['Nivel'],
                'imagen': imagen
            }
            cursos.append(curso)
        cursor.close()
        db.close()
        return cursos

    def get_random_cursos(self, num_cursos=6):
        db = Database()
        cursor = db.execute_query("SELECT * FROM Cursos ORDER BY RAND() LIMIT %s", (num_cursos,))
        #cursor = db.execute_query("SELECT * FROM Cursos WHERE ID = 1")
        cursos_data = cursor.fetchall()
        cursos = []
        for curso_data in cursos_data:
            imagen = curso_data['Imagen'] if curso_data['Imagen'] is not None else ''
            curso = {
                'id': curso_data['ID'],
                'titulo': curso_data['Titulo'],
                'descripcion': curso_data['Descripcion'],
                'duracion': curso_data['Duracion'],
                'nivel': curso_data['Nivel'],
                'imagen': imagen
            }
            cursos.append(curso)
        cursor.close()
        db.close()
        return cursos
    
    def obtener_curso_por_id(self, curso_id):
        db = Database()
        cursor = db.execute_query("SELECT * FROM Cursos WHERE ID = %s", (curso_id,))
        curso_data = cursor.fetchone()
        if curso_data:
            imagen = curso_data['Imagen'] if curso_data['Imagen'] is not None else ''
            curso = {
                'id': curso_data['ID'],
                'titulo': curso_data['Titulo'],
                'descripcion': curso_data['Descripcion'],
                'duracion': curso_data['Duracion'],
                'nivel': curso_data['Nivel'],
                'imagen': imagen
            }
            cursor.close()
            db.close()
            return curso
        else:
            cursor.close()
            db.close()
            return None

    def obtener_lecciones_por_curso(self, curso_id):
        db = Database()
        cursor = db.execute_query("SELECT * FROM Lecciones WHERE Curso = %s", (curso_id,))
        lecciones_data = cursor.fetchall()
        lecciones = []
        for leccion_data in lecciones_data:
            leccion = {
                'id': leccion_data['ID'],
                'titulo': leccion_data['Titulo'],
                'descripcion': leccion_data['Descripcion'],
                'contenido': leccion_data['Contenido'],
                'curso_id': leccion_data['Curso']
            }
            lecciones.append(leccion)
        cursor.close()
        db.close()
        return lecciones
    
    def inscribir_usuario_en_curso(self, usuario_id, curso_id):
        db = Database()
        cursor = db.execute_query("INSERT INTO Inscripciones (Usuario, Curso) VALUES (%s, %s)",
                                 (usuario_id, curso_id))
        
        cursor.close()
        db.close()
        return True

    def registrar_progreso_lecciones(self, usuario_id, curso_id, lecciones_progreso):
        db = Database()
        for leccion_id in lecciones_progreso:
            cursor = db.execute_query("INSERT INTO ProgresoLecciones (Usuario, Curso, Leccion) VALUES (%s, %s, %s)",
                                     (usuario_id, curso_id, leccion_id))
            
            cursor.close()
        db.close()
        return True
    
    def eliminar_inscripcion_por_id(self, inscripcion_id):
            db = Database()
            cursor = db.execute_query("DELETE FROM Inscripciones WHERE ID = %s", (inscripcion_id,))
            cursor.close()
            db.close()
            return True
        