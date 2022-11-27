class Usuario:
    def __init__(self, nombre:str, apellido:str, celular:str, direccion:str, correo:str, pass_word:str, id_usuario=None) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.direccion = direccion
        self.correo  = correo
        self.pass_word = pass_word
        self.id_usuario = id_usuario
        
    def toDic(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'celular': self.celular,
            'direccion': self.direccion,
            'correo': self.correo,
            'pass_word': self.pass_word
        }