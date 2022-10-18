class Calculadora:
    def __init__(self):
        self.n1 = int(input("Ingrese el primer número:"))
        self.n2 = int(input("Ingrese el segundo número:"))
        
    def suma(self) -> int:
        suma = self.n1 + self.n2
        print("La suma de los números es:", suma)
    
    def resta(self) -> int:
        resta = self.n1 - self.n2
        print("La resta de los números es:", resta)
        
    def multiplicacion(self) -> int:
        multiplicacion = self.n1 * self.n2
        print("La multiplicación de los números es:", multiplicacion)
    
    def division(self) -> float:
        divison = self.n1 / self.n2
        print("La división de los números es:", divison)
        
c = Calculadora()
c.suma()
c.resta()
c.multiplicacion()
c.division()
