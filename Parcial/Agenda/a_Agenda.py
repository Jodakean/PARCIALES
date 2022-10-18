from a_Contacto import Contacto

class Agenda:
    
    def __init__(self):
        '''Lista de contactos'''
        self.contactos = []
        
    def nuevo_Contacto(self):
        '''Método para un nuevo contacto'''
        nombre = input('Ingrese nombre: ')
        telefono = input('Ingrese Teléfono: ')
        email = input('Ingrese Email: ')
        return Contacto(nombre, telefono, email)
    
    def contiene_Contacto(self, telefono):
        '''Método para buscar un telefono en la base lista de contactos'''
        for contacto in self.contactos:
            if (contacto.telefono == telefono):
                return True
        return False
    
    def agregar_Contacto(self, Contacto):
        '''Método para agragar un contacto a la lista'''
        self.contactos.append(Contacto)
        print("\nContacto agregado.\n")

    def lista_Contactos(self):
        '''Mostrar lista de contactos'''
        for contacto in self.contactos:
            print("Nombre: ",contacto.nombre)
            print("Teléfono: ",contacto.telefono)
            print("Email: ",contacto.email)
            print("##################################\n")
    
    def mostrar_Contacto(self, contacto):
        '''Mostrar un SOLO contacto'''
        print("Nombre: ",contacto.nombre)
        print("Teléfono: ",contacto.telefono)
        print("Email: ",contacto.email)
        print("##################################\n")