import os
os.system ("cls")


asientos = ['X' if i > 0 else ' ' for i in range(101)] 
precios = [0, 120000, 80000, 50000] 
asistentes = {} 


def clearscreen():
    
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrarmenu():
     
    print("----- Menú -----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


def comprarentradas():
    
    print("----- Comprar entradas -----")
    cantidad = int(input("Ingrese la cantidad de entradas que deseas comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        print("Ha ocurrido un error, seleccione numeros desde el 1 al 3.")
        cantidad = int(input("Ingrese la cantidad de entradas que deseas comprar (1-3): "))

    entradas_compradas = []
    for i in range(cantidad):
        clearscreen()
        print("----- Comprar entradas ({} de {}) -----".format(i + 1, cantidad))
        print("Asientos que se encuentran disponibles:")
        mostrarasientos()
        asiento = int(input("Ingrese el número de asiento que desea: "))
        while asiento < 1 or asiento > 100 or asientos[asiento] == 'X':
            print("Error: El asiento no se encuentra disponible.")
            asiento = int(input("Ingrese el número de asiento que desea: "))

        asientos[asiento] = 'X'
        entradas_compradas.append(asiento)

    clearscreen()
    print("Entradas compradas con éxito.")
    for asiento in entradas_compradas:
        run = input("Ingrese su RUN para el asiento {}: ".format(asiento))
        asistentes[asiento] = run


def mostrarasientos():
    
    for i in range(1, 101):
        if i % 10 == 1:
            print()
        print("{:3}: {}".format(i, asientos[i]), end=" ")
    print()


def mostrarubicacionesdisponibles():
    
    print("----- Ubicaciones que se encuentran disponibles -----")
    mostrarasientos()


def verlistadoasistentes():
    
    print("----- Lista de asistentes -----")
    for asiento, run in sorted(asistentes.items(), key=lambda x: x[1]):
        print("RUN: {}, Asiento: {}".format(run, asiento))


def mostrargananciastotales():
    
    print("----- Ganancias totales -----")
    total = sum(precios[int(i / 25)] for i in range(1, 101) if asientos[i] == 'X')
    print("Ganancias totales: ${}".format(total))



while True:
    clearscreen()
    mostrarmenu()
    opcion = input("Ingrese una opción, por favor: ")
   
    if opcion == '1':
        comprarentradas()
    elif opcion == '2':
        mostrarubicacionesdisponibles()
    elif opcion == '3':
        verlistadoasistentes()
    elif opcion == '4':
        mostrargananciastotales()
    elif opcion == '5':
        break
    else:
 
      print("Opcion invalida, intentelo de nuevo.")

    input("Presiona Enter para continuar") 

