class LibroDeseo:
    def __init__(self, id_libro:int) -> None:
        self.id_libro = id_libro
    
    def toDic(self):
        return {
            'id_libro': self.id_libro,
        }