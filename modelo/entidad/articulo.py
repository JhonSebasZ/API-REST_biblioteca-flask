class Articulo:
    def __init__(self, cantidad:int, id_libro=None, libro=None) -> None:
        self.cantidad = cantidad
        self.id_libro = id_libro
        self.libro = libro
        
    def toDic(self):
        return {
            'cantidad': self.cantidad,
            'id_libro': self.id_libro,
            'libro': self.libro
        }