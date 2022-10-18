class alumno:
    '''Método de inicialización de atributos'''
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def display(self):
        '''Método para mostrar la información'''
        print("El nombre del alumno es",self.nombre,"y la nota es",self.nota)

a = alumno("Kevin", 4)
a.display()