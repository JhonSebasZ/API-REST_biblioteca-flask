from aplicacion import app
from modelo.entidad.libro import Libro
from modelo.repositorio.libro import RepositorioLibro
from controlador.response.api import ApiResponse
from flask import request

repositorio = RepositorioLibro()

@app.route('/biblioteca/libros', methods=['POST'])
def crearLibro():
    status = 400
    # data = request.json
    data = request.get_json(force=True)
    
    #  validadion id_libro
    if data.get('id_libro') is None:
        api = ApiResponse(mensage='El id del libro es obligatorio')
        return api.toDic()
    if not isinstance(data.get('id_libro'), int):
        api = ApiResponse(mensage='El id del libro dede de ser un int')
        return api.toDic()
    
    # validacion titulo
    if data.get('titulo') is None:
        api = ApiResponse(mensage='El titulo del libro es obligatorio')
        return api.toDic()
    if not isinstance(data.get('titulo'), str):
        api = ApiResponse(mensage='El titulo del libro dede de ser un str')
        return api.toDic()
    
    # validacion autor
    if data.get('autor') is None:
        api = ApiResponse(mensage='El autor del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('autor'), str):
        api = ApiResponse(mensage='El autor del libro dede de ser un str')
        return api.toDic()
    
    # validacion categoria
    if data.get('categoria') is None:
        api = ApiResponse(mensage='La categoria del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('categoria'), str):
        api = ApiResponse(mensage='La categoria del libro dede de ser un str')
        return api.toDic()
    
    # validacion del valor
    if data.get('valor') is None:
        api = ApiResponse(mensage='El valor del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('valor'), int):
        api = ApiResponse(mensage='El valor del libro dede de ser un int')
        return api.toDic()
    
    try:
        libro = Libro(
            id_libro=data.get('id_libro'),
            titulo=data.get('titulo'),
            autor=data.get('autor'),
            palabras_claves=data.get('palabras_claves'),
            categoria=data.get('categoria'),
            valor=data.get('valor')  
        ) 
    
        repositorio.crear(libro)
        api = ApiResponse(data=True)
        status = 201
    except Exception as ex:
        api = ApiResponse(mensage=f'{ex}')
    
    return api.toDic(), status

@app.route('/biblioteca/libros', methods=['GET'])
def mostrarLibros():
    try:
        data = repositorio.mostrarLibros()
        libros = [libro.toDic() for libro in data]
        api = ApiResponse(data=libros)
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(mensage=str(ex))
        return api.toDic(), 400

@app.route('/biblioteca/libros/<parametro>/<busqueda>', methods=['GET'])
def buscarLibros(parametro, busqueda):
    try:
        data = repositorio.buscarLibro(parametro=parametro, busqueda=busqueda)
        libros = [libro.toDic() for libro in data]
        api = ApiResponse(data=libros)
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(mensage=str(ex))
        return api.toDic(), 404

@app.route('/biblioteca/libros/actualizar/<id>', methods=['PUT'])
def actualizarLibro(id):
    data = request.get_json(force=True)
    
    # validacion titulo
    if data.get('titulo') is None:
        api = ApiResponse(mensage='El titulo del libro es obligatorio')
        return api.toDic()
    if not isinstance(data.get('titulo'), str):
        api = ApiResponse(mensage='El titulo del libro dede de ser un str')
        return api.toDic()
    
    # validacion autor
    if data.get('autor') is None:
        api = ApiResponse(mensage='El autor del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('autor'), str):
        api = ApiResponse(mensage='El autor del libro dede de ser un str')
        return api.toDic()

    # validacion categoria
    if data.get('categoria') is None:
        api = ApiResponse(mensage='La categoria del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('categoria'), str):
        api = ApiResponse(mensage='La categoria del libro dede de ser un str')
        return api.toDic()
    
    # validacion del valor
    if data.get('valor') is None:
        api = ApiResponse(mensage='El valor del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('valor'), int):
        api = ApiResponse(mensage='El valor del libro dede de ser un int')
        return api.toDic()
    
    try:
        libro = Libro(
            id_libro=id,
            titulo=data.get('titulo'),
            autor=data.get('autor'),
            palabras_claves=data.get('palabras_claves'),
            categoria=data.get('categoria'),
            valor=data.get('valor') 
        )
        repositorio.actualizar(libro=libro)
        api = ApiResponse(data=True)
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(mensage=str(ex))
        return api.toDic(), 209

@app.route('/biblioteca/libros/eliminar/<id>', methods=['DELETE'])
def eliminarLibro(id):
    try:
        repositorio.eliminar(id)
        api = ApiResponse(data=True)
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(mensage=str(ex))
        return api.toDic(), 409