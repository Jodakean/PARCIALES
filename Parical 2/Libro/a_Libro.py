from a_Pagina import Pagina

class Libro:
    
    def __init__(self, titulo, isbn, autor, año):
        
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.añoPublicación = año
    
    def set_Titulo(self, Titulo):
        self.titulo = Titulo
    
    def set_Isbn(self, Isbn):
        self.isbn = Isbn
    
    def set_Autor(self, Autor):
        self.autor = Autor
    
    def set_Año(self, Año):
        self.año = Año

    def get_Titulo(self):
        return self.titulo
    
    def get_Isbn(self):
        return self.isbn
    
    def get_Autor(self):
        return self.autor
        
    def get_Año(self):
        return self.año