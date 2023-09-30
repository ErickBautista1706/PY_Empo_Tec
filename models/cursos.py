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
