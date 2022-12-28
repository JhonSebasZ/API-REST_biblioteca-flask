from modelo.entidad.libro import Libro
from modelo.entidad.resena import Resena
from modelo.conexion import execute, commit

class RepositorioLibro:
    def crear(self, libro:Libro) -> None:
        palabras_claves = ','.join(libro.palabras_claves) if libro.palabras_claves != None else 'NULL'
        sql = f"""
                INSERT INTO libro (titulo, autor, palabras_claves, categoria, valor, imagen, descripcion)
                VALUES ('{libro.titulo}', '{libro.autor}', '{palabras_claves}', '{libro.categoria}', {libro.valor}, '{libro.imagen}', '{libro.descripcion}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def mostrarLibros(self) -> list:
        sql = "SELECT id_libro, titulo, imagen, descripcion FROM libro"
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
    
    def buscarLibro(self, parametro:str, busqueda:str) -> list:
        sql = f"""
                SELECT * FROM libro 
                WHERE {parametro} = '{busqueda}'
            """
        cursor = execute(sql)
        librosRes = cursor.fetchall()
        cursor.close()
        
        libros = []
        for libro in librosRes:
            resenas = list()
            sql = f"""
                SELECT * FROM resena 
                WHERE id_libro = '{libro[0]}'
            """
            cursor = execute(sql)
            resenasRes = cursor.fetchall()
            cursor.close()
            for res in resenasRes:
                resenas.append(Resena(comentario=res[1], calificacion=res[2], fecha=res[0]).toDict())
                
            palabras_claves = libro[3].split(',')
            libros.append(
                Libro(id_libro=libro[0], titulo=libro[1],
                    autor=libro[2], palabras_claves=palabras_claves,
                    categoria=libro[4], valor=libro[5], imagen=libro[6], 
                    descripcion=libro[7], resenas=resenas)
            )
        return libros
    
    def actualizar(self, libro:Libro) -> None:
        sql = f"""
                UPDATE libro
                SET titulo = '{libro.titulo}',
                    autor = '{libro.autor}',
                    palabras_claves = '{libro.palabras_claves}',
                    categoria = '{libro.categoria}',
                    valor = '{libro.valor}',
                    imagen= '{libro.imagen}',
                    descripcion = '{libro.descripcion}'
                WHERE id_libro = {libro.id_libro}
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def eliminar(self, id_libro:int) -> None:
        sql = f"""
                DELETE FROM libro
                WHERE id_libro = {id_libro}
            """
        cursor = execute(sql)
        cursor.close()
        commit()