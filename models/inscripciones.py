# models/inscripciones.py

from models.db import Database

class Inscripciones:
    def get_inscripciones_by_usuario(self, usuario_id):
        db = Database()
        cursor = db.execute_query(
            """
            SELECT inscripciones.ID, inscripciones.Usuario, inscripciones.Curso, inscripciones.Progreso, 
                cursos.Titulo AS CursoTitulo, cursos.Descripcion AS CursoDescripcion, cursos.Imagen AS CursoImagen
            FROM inscripciones
            JOIN cursos ON inscripciones.Curso = cursos.ID
            WHERE inscripciones.Usuario = %s
            """,
            (usuario_id,)
        )

        inscripciones_data = cursor.fetchall()
        inscripciones = []
        for inscripcion_data in inscripciones_data:
            inscripcion = {
                'id': inscripcion_data['ID'],
                'usuario': inscripcion_data['Usuario'],
                'curso': {
                    'id': inscripcion_data['Curso'],
                    'titulo': inscripcion_data['CursoTitulo'],
                    'descripcion': inscripcion_data['CursoDescripcion'],
                    'imagen': inscripcion_data['CursoImagen'],
                },
                'progreso': inscripcion_data['Progreso']
            }
            inscripciones.append(inscripcion)
        cursor.close()
        db.close()
        return inscripciones
