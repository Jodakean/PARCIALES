from a_Banco import Banco

if(__name__=='__main__'):
    
    banco = Banco()
    opcion = 1
    
    while(0 < opcion and opcion < 6):
        print('***BANCO***')
        print('1. Nuevo Cliente')
        print('2. Depositar')
        print('3. Extraer')
        print('4. Mostrar total deposito')
        print('5. Cerrar')
        
        opcion = int(input('\nElija una opción: '))
        
        while(opcion < 1 or opcion > 5):
            opcion = int(input('Elija la opción correcta entre 1 y 5'))
            
        if(opcion == 1):
            print('\nNuevo Cliente')
            Cliente = banco.Clinte()
            banco.agregar_Cliente(Cliente)
        elif(opcion == 2):
            print("\nDepositar")
            banco.depo()
        elif(opcion == 3):
            print("\nExtraer")
            banco.ex()
        elif(opcion == 4):
            print("\nMostrar total de depositos")
            banco.deposito_total()
        elif(opcion == 5):
            print("\nAdiós....")
            break    