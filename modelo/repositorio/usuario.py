from modelo.entidad.usuario import Usuario
from modelo.conexion import execute, commit

class RepositorioUsuario:
    def crearUsuario(self, usuario:Usuario) -> None:
        sql = f"""
                INSERT INTO usuario (nombre, apellido, celular, direccion, correo, pass_word)
                VALUES ('{usuario.nombre}', '{usuario.apellido}', '{usuario.celular}', '{usuario.direccion}', '{usuario.correo}', '{usuario.pass_word}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def mostrarUsuarios(self) -> list:
        sql = f"""
                SELECT * FROM usuario
            """
        cursor = execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        
        usuarios = []
        for res in resultados:
            usuarios.append(
                Usuario(
                    id_usuario=res[0], nombre=res[1], apellido=res[2],
                    celular=res[3], direccion=res[4], correo=res[5], pass_word=res[6]
                )
            )
        return usuarios

    def buscarUsuario(self, id_usuario:int) -> Usuario:
        sql = f"""
                SELECT * FROM usuario
                WHERE id_usuario = {id_usuario}
            """
        cursor = execute(sql)
        res = cursor.fetchone()
        cursor.close()
        
        if not res:
            raise Exception('El usuario no existe')
        
        return Usuario(
            id_usuario=res[0], nombre=res[1], apellido=res[2],
                    celular=res[3], direccion=res[4], correo=res[6], pass_word=res[6]
        )
    
    def actualizarUsuario(self, usuario:Usuario):
        sql = f"""
                UPDATE usuario
                SET nombre='{usuario.nombre}', apellido='{usuario.apellido}',
                    celular='{usuario.celular}', direccion='{usuario.direccion}', 
                    correo='{usuario.correo}', pass_word='{usuario.pass_word}'
                WHERE id_usuario = {usuario.id_usuario}
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def eliminarUsuario(self, id_usuario):
        sql = f"""
                DELETE FROM usuario
                WHERE id_usuario = {id_usuario}
            """
        cursor = execute(sql)
        cursor.close()
        commit() 