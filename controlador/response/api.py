class ApiResponse:
    def __init__(self, data=None, mensaje=None) -> None:
        self.data = data
        self.mensaje = mensaje
    
    def toDic(self):
        return{
            'data': self.data,
            'error': self.mensaje != None,
            'mensaje': self.mensaje
        }