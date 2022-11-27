from datetime import datetime

class Resena:
    def __init__(self, comentario:str, calificacion:int, id_usuraio:int, id_libro=None, fecha=None) -> None:
        self.comentario = comentario
        self.calificacion = calificacion
        self.id_usuario = id_usuraio
        self.id_libro = id_libro
        if fecha is None:
            self.fecha = datetime.now()
        else:
            self.fecha = fecha
        
    def toDict(self):
        return {
            'comentario': self.comentario,
            'fecha': self.fecha,
            'calificacion': self.calificacion,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro
        }