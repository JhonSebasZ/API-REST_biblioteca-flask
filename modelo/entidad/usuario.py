class Usuario:
    def __init__(self, nombre:str, apellido:str, celular:str, direccion:str, correo:str, pass_word:str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.direccion = direccion
        self.correo  = correo
        self.pass_word = pass_word