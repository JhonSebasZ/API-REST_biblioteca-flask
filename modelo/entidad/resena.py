from datetime import date

class Resena:
    def __init__(self, comentario:str, calificacion:int, id_usuraio:int, id_libro:int) -> None:
        self.comentario = comentario
        self.fecha = date.today()
        self.calificacion = calificacion
        self.id_usuario = id_usuraio
        self.id_libro = id_libro
        
    def toDict(self):
        return {
            'comentario': self.comentario,
            'fecha': self.fecha,
            'calificacion': self.calificacion,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro
        }