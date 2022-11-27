from aplicacion import app
from modelo.entidad.usuario import Usuario
from modelo.repositorio.usuario import RepositorioUsuario
from controlador.response.api import ApiResponse
from flask import request
from MySQLdb import IntegrityError

repo = RepositorioUsuario()

@app.route('/biblioteca/usuarios', methods=['POST'])
def crearUsuario():
    estado = 400
    data = request.get_json(force=True)
    
    # validacion nombre
    if data.get('nombre') is None:
        api = ApiResponse(mensaje='El nombre del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('nombre'), str):
        api = ApiResponse(mensaje='El nombre del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion apellido
    if data.get('apellido') is None:
        api = ApiResponse(mensaje='El apellido del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('apellido'), str):
        api = ApiResponse(mensaje='El apellido del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion celular
    if data.get('celular') is None:
        api = ApiResponse(mensaje='El celular del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('celular'), str):
        api = ApiResponse(mensaje='El celular del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion direccion
    if data.get('direccion') is None:
        api = ApiResponse(mensaje='La direccion del usuario es obligatoria')
        return api.toDic(), estado
    if not isinstance(data.get('direccion'), str):
        api = ApiResponse(mensaje='La direccion del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion correo
    if data.get('correo') is None:
        api = ApiResponse(mensaje='El correo del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('correo'), str):
        api = ApiResponse(mensaje='El correo del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacio pass_word
    if data.get('pass_word') is None:
        api = ApiResponse(mensaje='La contraseña del usuario es obligatoria')
        return api.toDic(), estado
    if not isinstance(data.get('pass_word'), str):
        api = ApiResponse(mensaje='La contraseña del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    try:
        usuario = Usuario(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            celular=data.get('celular'),
            direccion=data.get('direccion'),
            correo=data.get('correo'),
            pass_word=data.get('pass_word') 
        )
        repo.crearUsuario(usuario=usuario)
        api = ApiResponse(data=True)
        estado = 201
    except IntegrityError:
        api = ApiResponse(mensaje='Correo existente')
        estado = 400
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
    
    return api.toDic(), estado

@app.route('/biblioteca/usuarios', methods=['GET'])
def mostrarUsuarios():
    estado = 200
    try:
        data = repo.mostrarUsuarios()
        usuarios = [usuario.toDic() for usuario in data]
        api = ApiResponse(data=usuarios)
    except Exception as ex:
        estado = 400
        api = ApiResponse(mensaje=str(ex))
    return api.toDic(), estado

@app.route('/biblioteca/usuarios/<id>', methods=['GET'])
def buscarUsuario(id):
    estado = 200
    try:
        data = repo.buscarUsuario(id)
        usuario = data.toDic()
        api = ApiResponse(data=usuario)
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
        estado = 204
    return api.toDic(), estado

@app.route('/biblioteca/usuarios/actualizar/<id_usuario>', methods=['PUT'])
def actualizarUsuario(id_usuario):
    estado = 400
    data = request.get_json(force=True)
    
    # validacion nombre
    if data.get('nombre') is None:
        api = ApiResponse(mensaje='El nombre del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('nombre'), str):
        api = ApiResponse(mensaje='El nombre del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion apellido
    if data.get('apellido') is None:
        api = ApiResponse(mensaje='El apellido del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('apellido'), str):
        api = ApiResponse(mensaje='El apellido del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion celular
    if data.get('celular') is None:
        api = ApiResponse(mensaje='El celular del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('celular'), str):
        api = ApiResponse(mensaje='El celular del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion direccion
    if data.get('direccion') is None:
        api = ApiResponse(mensaje='La direccion del usuario es obligatoria')
        return api.toDic(), estado
    if not isinstance(data.get('direccion'), str):
        api = ApiResponse(mensaje='La direccion del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacion correo
    if data.get('correo') is None:
        api = ApiResponse(mensaje='El correo del usuario es obligatorio')
        return api.toDic(), estado
    if not isinstance(data.get('correo'), str):
        api = ApiResponse(mensaje='El correo del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    # validacio pass_word
    if data.get('pass_word') is None:
        api = ApiResponse(mensaje='La contraseña del usuario es obligatoria')
        return api.toDic(), estado
    if not isinstance(data.get('pass_word'), str):
        api = ApiResponse(mensaje='La contraseña del usuario debe de ser de tipo str')
        return api.toDic(), estado
    
    try:
        usuario = Usuario(
            id_usuario=id_usuario,
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            celular=data.get('celular'),
            direccion=data.get('direccion'),
            correo=data.get('correo'),
            pass_word=data.get('pass_word') 
        )
        repo.actualizarUsuario(usuario=usuario)
        api = ApiResponse(data=True)
        estado = 200
    except IntegrityError:
        api = ApiResponse(mensaje='Correo existente')
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
    
    return api.toDic(), estado

@app.route('/biblioteca/usuarios/eliminar/<id>', methods=['DELETE'])
def eliminarUsuario(id):
    estado = 200
    try:
        repo.eliminarUsuario(id)
        api = ApiResponse(data=True)
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
        estado = 400
    return api.toDic(), estado

