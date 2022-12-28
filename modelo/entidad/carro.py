class Carro:
    def __init__(self, id_articulo:int, valor_total=None) -> None:
        self.valor_total = valor_total
        self.id_articulo = id_articulo
        
    def toDic(self):
        return {
            "valor_total": self.valor_total,
            "id_articulo": self.id_articulo
        }