from a_Agenda import Agenda

if(__name__=='__main__'):
    
    agenda = Agenda()
    opcion = 1
    
    while(0 < opcion and opcion < 6):
        print('***AGENDA***')
        print('1. Nuevo Contacto')
        print('2. Lista de contactos')
        print('3. Buscar contacto')
        print('4. Editar contacto')
        print('5. Cerrar Agenda')
        
        opcion = int(input('\nElija una opción: '))
        
        while(opcion < 1 or opcion > 5):
            opcion = int(input('Elija la opción correcta entre 1 y 7'))
            
        if(opcion == 1):
            print('\nNuevo contacto')
            contacto = agenda.nuevo_Contacto()
            if (agenda.contiene_Contacto(contacto.telefono)):
                print("El contacto con telefono {0} ya exisite en la agenda".format(contacto.telefono))
            else:
                agenda.agregar_Contacto(contacto)
        elif(opcion == 2):
            print("\nLista de contactos")
            agenda.lista_Contactos()
        elif(opcion == 3):
            print("\nBuscar contacto")
            contacto = agenda.nuevo_Contacto()
            if(agenda.contiene_Contacto(contacto.telefono)):
                print("El contacto con telefono {0} ya está en la agenda".format(contacto.telefono))
                agenda.mostrar_Contacto(contacto)            
            else:
                print("El contacto con el telefono {0} no exite", format(contacto.telefono))
        elif(opcion == 4):
            print("\nEditar contacto")
        elif(opcion == 5):
            print("\nAdiós....")
            break    