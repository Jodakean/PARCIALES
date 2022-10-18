class Triangulo:
    '''Método de inicialización de los lados'''
    def __init__(self, lado1, lado2, lado3) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_Triangulo(self):
        '''Método para determinar el tipo de triángulo  '''
        if(self.lado1 == self.lado2 and self.lado2 == self.lado3):
            print("El triángulo es equilátero")
        elif(self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3):
            print("El triángulo es isóceles")
        else:
            print("El  triángulo es escaleno")

    def lado_Mayor(self):
        '''Método para saber que lado es mayor'''
        if(self.lado1 > self.lado2 and self.lado1 > self. lado3):
            print("El lado mayor es", self.lado1)   
        elif(self.lado2 > self.lado1 and self.lado2 > self. lado3):
            print("El lado mayor es", self.lado2)   
        elif(self.lado3 > self.lado2 and self.lado3 > self. lado1):
            print("El lado mayor es", self.lado3)
        else:
            print("No hay SOLO un lado mayor", "(",self.lado1, self.lado2, self.lado3,")")

t = Triangulo(9, 10, 5)
t.tipo_Triangulo()
t.lado_Mayor()