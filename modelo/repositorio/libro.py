from modelo.entidad.libro import Libro
from modelo.conexion import execute, commit

class RepositorioLibro:
    def crear(self, libro:Libro) -> None:
        palabras_claves = libro.palabras_claves if libro.palabras_claves != None else 'NULL'
        sql = f"""
                INSERT INTO libro (titulo, autor, palabras_claves, categoria, unidades, valor)
                VALUES ('{libro.titulo}', '{libro.autor}', '{palabras_claves}', '{libro.categoria}', {libro.unidades}, {libro.valor})
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def buscarLibroTitulo(self, parametro:str, busqueda:str) -> list:
        sql = f"""
                SELECT * FROM libro 
                WHERE '{parametro}' = '{busqueda}'
            """
        cursor = execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        
        libros = []
        for resultado in resultados:
            libros.append(
                Libro(id_libro=resultado[0], titulo=resultado[1],
                    autor=resultado[2], palabras_claves=resultado[3],
                    categoria=resultado[4], unidades=resultado[5],
                    valor=resultado[6])
            )
        return libros
    
    def actualizar(self, libro:Libro) -> None:
        sql = f"""
                UPDATE libro
                SET titulo = '{libro.titulo}',
                    autor = '{libro.autor}',
                    palabras_claves = '{libro.palabras_claves}',
                    categoria = '{libro.categoria}',
                    unidades = '{libro.unidades}',
                    valor = '{libro.valor}'
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