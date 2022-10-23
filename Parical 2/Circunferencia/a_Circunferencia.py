from a_Circunferencia import Punto

class Circunferecnia_centrada:
    
    def __init__(self, radio):
        self.PI = 3.1416
        self.radio = radio
        self.centro = Punto()
        
    def set_Radio(self, radio):
        self.radio = radio
    
    def Diametro(self):
        return print("El diametro es: "(2 * self.radio))
    
    def Longitud(self):
        return print("La longitud es: "(2 * self.PI * self.radio))
    
    def Area(self):
        return print("El Area es: "(self.PI * (self.radio * self.radio)))
        
    def TrasladarCincunferenciaCentrada(self, x, y):
        self.coord_x = x
        self.coord_y = y