class Libro:
    def __init__(self, titulo:str, autor:str, categoria:str, unidades:int, valor:int, palabras_claves=None, id_libro=None) -> None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves = palabras_claves
        self.unidades = unidades
        self.categoria = categoria
        self.valor = valor