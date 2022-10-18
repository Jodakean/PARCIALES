from a_Cliente import Cliente

class Banco:
    def __init__(self):
        self.Clientes=[]
   
    def Clinte(self):
        nombre = input('Ingrese nombre: ')
        cantidad = input('Ingrese Cantidad: ')
        return Cliente(nombre, cantidad)
        
    def agregar_Cliente(self, Cliente):
        self.Clientes.append(Cliente)
        print("\nCliente agregado.\n")
    
    def depo(self):
        deposito = input("Ingrese cantidad de deposito: ")
        depo_Total = Cliente.depositar(deposito) + depo_Total
        return(depo_Total) 
        
    def ex(self):
        extraer = input("Ingrese cantidad de extracción: ")
        Cliente.extraer(extraer)
    
    def deposito_total(self):
        depo_Total = Banco.depo
        print("El deposito total es de: ", depo_Total)