class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.candtidad = cantidad
    
    def depositar(self, deposito):
        self.candtidad = self.candtidad + deposito
        print("Deposito hecho correctamente.")
        return(deposito)
        
    def extraer(self, extraer):
        self.candtidad = self.candtidad - extraer
        print("Extracción hecha correctamente.")
    
    def mostrar_total(self):
        print("Su cantidad total es: ", self.candtidad)
