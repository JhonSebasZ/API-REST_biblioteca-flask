class Libro:
    def __init__(self, id_libro:int, titulo:str, autor:str, categoria:str, valor:int, palabras_claves=[], resenas=[]) -> None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.valor = valor
        self.palabras_claves = palabras_claves
        self.resenas = resenas
        
    def toDic(self):
        return {
            'id_libro': self.id_libro,
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'valor': self.valor,
            'palbas_claves': self.palabras_claves,
            'resenas': self.resenas
        }