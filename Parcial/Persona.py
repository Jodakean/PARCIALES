class Persona:
    '''Método de inicialización de atributos'''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
     
    def mayor(self):
        '''Método para saber si es mayor de edad'''
        if (self.edad >= 18):
            print("Y es mayor de edad","(",self.edad,")")
        else:
            print("Y no es mayor de edad","(",self.edad,")")
    
    def display(self):
        '''Método para mostrar el nombre'''
        print("El nombre es",self.nombre)
    
p = Persona("Andres", 21)
p.display() 
p.mayor()