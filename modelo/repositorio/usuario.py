from modelo.entidad.usuario import Usuario
from modelo.conexion import execute, commit

class PepositorioUsuario:
    def crear(self, usuario:Usuario) -> None:
        sql = f"""
                INSERT INTO usuario (nombre, apellido, celular, direccion, correo, pass_word)
                VALUES ('{usuario.nombre}', '{usuario.apellido}', '{usuario.celular}', '{usuario.direccion}', '{usuario.corre}', '{usuario.pass_word}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()
        