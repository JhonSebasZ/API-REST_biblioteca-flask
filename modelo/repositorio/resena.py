from modelo.entidad.resena import Resena
from modelo.conexion import execute, commit

class RepositorioResena():
    
    def crearResena(self, resena:Resena) -> None:
        sql = f"""
                INSERT INTO resena (fecha, comentario, calificacion, id_libro)
                VALUES ('{resena.fecha}', '{resena.comentario}', {resena.calificacion}, {resena.id_libro})
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def eliminarResena(self, id_libro:int, fecha) -> None:
        sql = f"""
                DELETE FROM resena
                WHERE id_libro = {id_libro}
                AND fecha = '{fecha}'
            """
        cursor = execute(sql)
        cursor.close