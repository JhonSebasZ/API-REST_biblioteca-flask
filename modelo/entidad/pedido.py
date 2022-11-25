from datetime import date

class Pedido:
    def __init__(self, estado:str, valor_total:float, id_usuario:int, id_pago:int) -> None:
        self.fecha = date.today()
        self.estado = estado
        self.valor_total = valor_total
        self.id_usuario = id_usuario
        self.id_pago = id_pago