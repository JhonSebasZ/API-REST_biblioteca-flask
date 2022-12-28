class Libro:
    def __init__(self, titulo:str, autor:str, categoria:str, valor:int, imagen:str, descripcion:str, palabras_claves=[], resenas=[], id_libro=None) -> None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.valor = valor
        self.palabras_claves = palabras_claves
        self.resenas = resenas
        self.imagen = imagen
        self.descripcion = descripcion
        
    def toDic(self):
        return {
            'id_libro': self.id_libro,
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'valor': self.valor,
            'palabras_claves': self.palabras_claves,
            'resenas': self.resenas,
            'imagen': self.imagen,
            'descripcion': self.descripcion
        }