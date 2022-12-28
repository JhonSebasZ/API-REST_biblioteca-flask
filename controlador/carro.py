from aplicacion import app
from modelo.entidad.articulo import Articulo
from modelo.repositorio.carro import RepositorioCarro
from controlador.response.api import ApiResponse
from MySQLdb import IntegrityError
from flask import request

repo = RepositorioCarro()

@app.route("/biblioteca/agregarCarro", methods=["POST"])
def addArticuloCarro():
    try:
        data = request.json
        articulo = Articulo(data.get("cantidad"), data.get("id_libro"))
        repo.addArticuloCarro(articulo)
        api = ApiResponse(data=True)
        return api.toDic()
    except IntegrityError:
        api = ApiResponse(mensaje='El libro ya esta en el carro')
        return api.toDic()

@app.route("/biblioteca/articulos/carro", methods=["GET"])
def mostrarArticulos():
    data = repo.obtenerArticulos()
    articulos = [articulo.toDic() for articulo in data]
    api = ApiResponse(data=articulos)
    return api.toDic()

@app.route("/biblioteca/carro/modificar/articulo", methods=["PUT"])
def modificarArticulo():
    data = request.json
    repo.modificarArticulo(id_libro=data.get('id_libro'), cantidad=data.get('cantidad'))
    api = ApiResponse(data=True)
    return api.toDic()

@app.route("/biblioteca/articulo/eliminar/<id>", methods=["DELETE"])
def eliminarArticulo(id):
    repo.eliminarArticulo(id_libro=id)
    api = ApiResponse(data=True)
    return api.toDic()

@app.route("/biblioteca/realizarCompra", methods=["DELETE"])
def limpiarCarro():
    repo.limpiarCarro()
    api = ApiResponse(data=True)
    return api.toDic()