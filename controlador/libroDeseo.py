from aplicacion import app
from controlador.response.api import ApiResponse
from modelo.entidad.libroDeseo import LibroDeseo
from modelo.repositorio.libroDeseo import RepositorioLibroDeseo
from flask import request

repo = RepositorioLibroDeseo()

@app.route('/biblioteca/agregar/deseos/<id>', methods=['POST'])
def agregar(id):
    try:
        libro = LibroDeseo(id)
        repo.agregar(libro)
        api = ApiResponse(data=True)
        return api.toDic()
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
        return api.toDic()
    

@app.route('/biblioteca/libros/deseos', methods=['GET'])
def mostraLibros():
    try:
        data = repo.mostrarLibros()
        api = ApiResponse(data=data)
        return api.toDic()
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
        return api.toDic()

@app.route('/biblioteca/libros/deseos/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    try:
        repo.eliminar(id)
        api = ApiResponse(data=True)
        return api.toDic()
    except Exception as ex:
        api = ApiResponse(mensaje=str(ex))
        return api.toDic()
        