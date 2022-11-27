from aplicacion import app
from modelo.entidad.resena import Resena
from modelo.repositorio.resena import RepositorioResena
from controlador.response.api import ApiResponse
from flask import request

repo = RepositorioResena()

@app.route('/biblioteca/resenas', methods=['POST'])
def crearResena():
    estado = 400
    data = request.get_json(force=True)
    
    try:
        resena = Resena(
            comentario=data.get('comentario'),
            calificacion=data.get('calificacion'),
            id_usuraio=data.get('id_usuario'),
            id_libro=data.get('id_libro')
        )
    
        repo.crearResena(resena=resena)
        api = ApiResponse(data=True)
        estado = 201
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
    return api.toDic(), estado

@app.route('/biblioteca/resenas/eliminar', methods=['DELETE'])
def eliminarResena():
    estado = 200
    data = request.json
    id_libro = data.get('id_libro')
    id_usuario = data.get('id_usuario')
    fecha = data.get('fecha')
    try:
        repo.eliminarResena(id_libro=id_libro, id_usuario=id_usuario, fecha=fecha)
        api = ApiResponse()
    except Exception as ex:
        estado = 400
        api = ApiResponse(mensaje=str(ex))
    return api.toDic(), estado