from modelo.entidad.articulo import Articulo
from modelo.conexion import execute, commit

class RepositorioCarro():
    
    def addArticuloCarro(self, articulo:Articulo) -> None:        
        sql = f"""
                INSERT INTO carro (id_libro, cantidad)
                VALUES ({articulo.id_libro}, {articulo.cantidad})
            """
        cursor = execute(sql)
        commit()
        cursor.close()
    
    def obtenerArticulos(self) -> list:
        sql = """
                SELECT car.cantidad, li.id_libro, li.titulo, li.autor, li.valor, li.imagen
                FROM carro car
                JOIN libro li
                WHERE car.id_libro = li.id_libro
            """
        cursor = execute(sql)
        resul = cursor.fetchall()
        cursor.close()
        articulos = []
        if resul:
            for art in resul:
                libro = {
                    'titulo': art[2],
                    'autor': art[3],
                    'valor': art[4],
                    'imagen': art[5]
                }
                articulos.append(
                    Articulo(cantidad=art[0], id_libro=art[1], libro=libro)
                )
        return articulos
    
    def modificarArticulo(self, id_libro:int, cantidad:int) -> None:        
        sql = f"""
                UPDATE carro
                SET cantidad = {cantidad}
                WHERE id_libro = {id_libro}
            """
        cursor = execute(sql)
        commit()
        cursor.close()
    
    def eliminarArticulo(self, id_libro) -> None:
        sql = f"""
                DELETE FROM carro
                WHERE id_libro = {id_libro}
            """
        cursor = execute(sql)
        cursor.close()
    
    def limpiarCarro(self) -> None:
        sql = "DELETE FROM carro"
        cursor = execute(sql)
        cursor.close()