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
    
    # validacion palabras claves
    if data.get('palabras_claves') is not None:
        if not isinstance(data.get('palabras_claves'), str):
            api = ApiResponse(mensage='Las palabras claves deden de ser un str')
            return api.toDic() 
    
    # validacion categoria
    if data.get('categoria') is None:
        api = ApiResponse(mensage='La categoria del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('categoria'), str):
        api = ApiResponse(mensage='La categoria del libro dede de ser un str')
        return api.toDic()
    
    # validacion de las unidades
    if data.get('unidades') is None:
        api = ApiResponse(mensage='Las unidades del libro es obligatio')
        return api.toDic()
    if not isinstance(data.get('unidades'), int):
        api = ApiResponse(mensage='Las unidades del libro dede de ser un int')
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
            titulo=data.get('titulo'),
            autor=data.get('autor'),
            palabras_claves=data.get('palabras_claves'),
            categoria=data.get('categoria'),
            unidades=data.get('unidades'),
            valor=data.get('valor')  
        ) 
    
        repositorio.crear(libro)
        api = ApiResponse(data=True)
        status = 201
    except Exception as ex:
        api = ApiResponse(mensage=f'{ex}')
    
    return api.toDic(), status