from modelo.entidad.libroDeseo import LibroDeseo
from modelo.conexion import execute, commit

class RepositorioLibroDeseo:
    
    def agregar(self, libro:LibroDeseo) -> None:
        sql = f"""
                INSERT INTO libroDeseo 
                VALUES ({libro.id_libro})
            """
        cursor = execute(sql)
        commit()
        cursor.close()
    
    def mostrarLibros(self) -> list:
        sql = """SELECT l.id_libro, l.titulo, l.imagen, l.descripcion 
                FROM libro l
                JOIN libroDeseo ld
                ON l.id_libro = ld.id_libro
            """
        cursor = execute(sql)
        resLibros = cursor.fetchall()
        cursor.close()
        
        libros = []
        for libro in resLibros:
            libros.append({
                'id_libro': libro[0],
                'titulo': libro[1],
                'imagen': libro[2],
                'descripcion': libro[3]
            })
        return libros
    
    def eliminar(self, id:int) -> None:
        sql = f"""
                DELETE FROM libroDeseo
                WHERE id_libro = {id}
            """
        cursor = execute(sql)
        commit()
        cursor.close()
        