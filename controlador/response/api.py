class ApiResponse:
    def __init__(self, data=None, mensage=None) -> None:
        self.data = data
        self.mensage = mensage
    
    def toDic(self):
        return{
            'data': self.data,
            'error': self.mensage != None,
            'mensage': self.mensage
        }