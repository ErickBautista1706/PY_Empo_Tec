from models.db import Database

class ProgresoLecciones:
    def get_progresos_by_usuario(self, usuario_id):
        db = Database()
        cursor = db.execute_query(
            """
            SELECT progresolecciones.ID, progresolecciones.Usuario, progresolecciones.Leccion, progresolecciones.Estado,
                lecciones.Titulo AS LeccionTitulo, lecciones.Curso AS LeccionCurso
            FROM progresolecciones
            JOIN lecciones ON progresolecciones.Leccion = lecciones.ID
            WHERE progresolecciones.Usuario = %s
            """,
            (usuario_id,)
        )
        
        progresos_data = cursor.fetchall()
        progresos = []
        
        for progreso_data in progresos_data:
            progreso = {
                'id': progreso_data['ID'],
                'usuario': progreso_data['Usuario'],
                'leccion': {
                    'id': progreso_data['Leccion'],
                    'titulo': progreso_data['LeccionTitulo'],
                    'curso_id': progreso_data['LeccionCurso']
                },
                'estado': progreso_data['Estado']
            }
            progresos.append(progreso)
        
        cursor.close()
        db.close()
        return progresos
