
class Pagina:
    
    def __init__(self, contenido, pagina):
        self.contenido = contenido
        self.pagina = pagina
    
    def set_Contenido(self, Contenido):
        self.contenido = Contenido
        
    def set_Numero(self, Numero):
        self.pagina = Numero
        
    def get_Contenido(self):
        return self.contenido
    
    def get_Numero(self):
        return self.pagina